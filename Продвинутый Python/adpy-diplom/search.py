import json
import time

from tqdm import tqdm

from db.offset import get_offset, update_offset
from db.writer import db_writer
from matches.match import score_users
from user import User
from utils.params import ask_params, update_params


def get_top_matches(users):
    users_scores = dict()
    for user in tqdm(users, desc=''):
        users_scores[user] = user.score
    users_scores_sorted = sorted(users_scores.items(), key=lambda x: x[1], reverse=True)
    users_scores_list = users_scores_sorted[:10]
    return users_scores_list


def get_top_photos(photos_list):
    profile_photos = dict()
    for photo in photos_list:
        profile_photos[photo['id']] = [photo['likes']['count'], photo['sizes'][-1]['src']]
    profile_photos_sorted = sorted(profile_photos.items(), key=lambda x: x[1][0], reverse=True)
    profile_photos_list = profile_photos_sorted[:3]
    profile_photos_ids = dict()
    for photo in profile_photos_list:
        profile_photos_ids[str(photo[0])] = photo[1][1]
    return profile_photos_ids


@db_writer
def prepare_result(top_matches):
    result = list()
    for match in tqdm(top_matches, desc='Подготовка результата: '):
        photos_list = match[0].get_photos()
        top_photos = get_top_photos(photos_list)
        match_dict = {
            'id': str(match[0].user_id),
            'url': f'http://vk.com/id{match[0].user_id}',
            'photos': top_photos
        }
        result.append(match_dict)
        time.sleep(0.4)
    return result


def print_write_result(prepared_result):
    json_dict = dict()
    for match in prepared_result:
        print(f'Ссылка на профиль: {match["url"]}')
        photo_list = list()
        for photo in match['photos'].values():
            print(f'Фотография: {photo}')
            photo_list.append(photo)
        json_dict.update({f'{match["url"]}': photo_list})
    with open('top-10.json', mode='w', encoding='utf8') as ff:
        json.dump(json_dict, ff)


def get_search_result():
    user_id, sex, age_from, age_to = ask_params()
    user = User(user_id)
    user.get_user_data()
    if user.error is 5:
        print('Неверный токен. Попробуйте снова.')
    elif user.error is 18:
        print('Этот пользователь был удален или забанен.')
    elif user.error is 113:
        print('Такого пользователя не существует. Попробуйте снова.')
    else:
        update_params(user)
        print(f'Поиск совпадений для {user.user_id}')
        offset = get_offset()
        search_results = user.search_users(sex, age_from, age_to, offset)[1]
        update_offset(offset)
        print('Оценка пользователей')
        score_users(user, search_results)
        print('Выбор наилучших совпадений')
        top_matches = get_top_matches(search_results)
        result = prepare_result(top_matches)
        print('Сохранение в базу данных...')
        print('Успешно!')
        print_write_result(result)

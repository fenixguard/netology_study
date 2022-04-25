import re
import time

from tqdm import tqdm

from matches.default import INTERESTS_SCORE, FRIENDS_SCORE, GROUPS_SCORE, \
    MUSIC_SCORE, BOOKS_SCORE, TV_SCORE, MOVIES_SCORE, PATTERN


def check_mutual_friends(users):
    for item in users:
        item.score += FRIENDS_SCORE * item.common_count


def check_mutual_groups(user, users):
    user_groups = set(user.get_groups())
    for position, item in tqdm(enumerate(users), desc='Проверка общих групп: '):
        item_groups = set(item.get_groups())
        mutual_groups = user_groups & item_groups
        if mutual_groups:
            item.score += GROUPS_SCORE * len(mutual_groups)
        time.sleep(0.35)


def check_common_interests(user, users):
    pattern = PATTERN.sub('', user.interests).lower().replace(', ', '|')
    for item in users:
        common_interests = re.findall(pattern, item.interests.lower())
        if common_interests and '' not in common_interests:
            item.score += INTERESTS_SCORE * len(common_interests)


def check_common_music(user, users):
    pattern = PATTERN.sub('', user.music).lower().replace(', ', '|')
    for item in users:
        common_music = re.findall(pattern, item.music.lower())
        if common_music and '' not in common_music:
            item.score += MUSIC_SCORE * len(common_music)


def check_common_tv(user, users):
    pattern = PATTERN.sub('', user.tv).lower().replace(', ', '|')
    for item in users:
        common_tv = re.findall(pattern, item.tv.lower())
        if common_tv and '' not in common_tv:
            item.score += TV_SCORE * len(common_tv)


def check_common_movies(user, users):
    pattern = PATTERN.sub('', user.movies).lower().replace(', ', '|')
    for item in users:
        common_movies = re.findall(pattern, item.movies.lower())
        if common_movies and '' not in common_movies:
            item.score += MOVIES_SCORE * len(common_movies)


def check_common_books(user, users):
    pattern = PATTERN.sub('', user.books).lower().replace(', ', '|')
    for item in users:
        common_books = re.findall(pattern, item.books.lower())
        if common_books and '' not in common_books:
            item.score += BOOKS_SCORE * len(common_books)


def score_users(user, users):
    print('Проверка общих друзей...')
    check_mutual_friends(users)
    check_mutual_groups(user, users)
    print('Проверка общих интересов, музыки, кино, телепередач, книг...')
    check_common_interests(user, users)
    check_common_music(user, users)
    check_common_movies(user, users)
    check_common_tv(user, users)
    check_common_books(user, users)

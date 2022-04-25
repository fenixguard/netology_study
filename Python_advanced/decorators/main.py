import json
from xml.etree import ElementTree
from utils.loggers import logger, params_logger


@logger
def create_wordlist_xml(path):
    """Функция наполнения списка слова из файла .xml"""
    word_list = list()
    tree = ElementTree.parse(path)
    root = tree.getroot()
    for child_element in root:
        for child in child_element:
            for sub_child in child:
                if sub_child.tag == 'description':
                    temp_list = list()
                    temp_list.extend(sub_child.text.split())
                    for t in temp_list:
                        if len(t) > 6:
                            word_list.append(t.capitalize())
    return word_list


@logger
def create_wordlist_json(path):
    """Функция наполнения списка слова из файла .json"""
    word_list = list()
    with open(path, "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
        for item in data['rss']['channel']['items']:
            temp_list = list()
            temp_list.extend(item['description'].split())
            for t in temp_list:
                if len(t) > 6:
                    word_list.append(t.capitalize())
    return word_list


@params_logger("log_params.txt")
def count_word():
    """Функция подсчета слов"""
    word_count = dict()
    for word in word_list:
        try:
            word_count[word] = word_list.count(word)
        except KeyError:
            pass  # Исключаем повторы
    return word_count


@params_logger("log_params.txt")
def sorted_word():
    """Функция сортировки словаря"""
    stats_sorted = sorted(word_count.items(), key=lambda x: -x[1])
    return stats_sorted


def print_result():
    """Функция вывода результата"""
    for stat in stats_sorted[:10]:
        print(f"{stat[0]}: {stat[1]}")


def main():
    print("Выберите какой формат файла хотите обработать, поддерживаемые форматы json, xml")
    print("-" * 40)
    number = int(input("Если хотите обработать json - введите 1\nЕсли хотите обработать xml - введите 2\n"))
    print('-' * 40)
    print("Слово: количество повторений")
    print('-' * 40)
    assert number == 1 or number == 2, 'Вы ввели неверную цифру, введите 1 - json или 2 - xml.'
    if number == 1:
        return create_wordlist_json('newsafr.json')
    if number == 2:
        return create_wordlist_xml('newsafr.xml')


if __name__ == '__main__':
    word_list = main()
    word_count = count_word()
    stats_sorted = sorted_word()
    print_result()

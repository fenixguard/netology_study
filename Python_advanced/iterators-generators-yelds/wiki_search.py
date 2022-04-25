import json
import time
from datetime import datetime
from hashlib import md5

import wikipedia
from tqdm import tqdm


class WikiSearch:

    def __init__(self, input_file, output_file):
        self.start = -1
        with open(input_file, mode='r', encoding='utf8') as ff:
            open_file = json.load(ff)
        self.countries = [country_name['name']['official'] for country_name in open_file]
        self.output_file = output_file
        self.end = len(self.countries)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        try:
            wiki_page = wikipedia.page(self.countries[self.start]).url
        except wikipedia.WikipediaException:
            wiki_page = wikipedia.page(self.countries[self.start] + ' country').url
        with open(self.output_file, mode='a', encoding='utf8') as fe:
            fe.write(f"{self.countries[self.start]} - {wiki_page}\n")

        return self.countries[self.start], wiki_page


def get_md5(input_file):
    with open(input_file, mode='r', encoding='utf8') as ff:
        for line in ff:
            yield md5(line.encode()).hexdigest()


if __name__ == '__main__':
    print(f'Начало получения URL {datetime.utcnow()}')
    wiki_url_pages = WikiSearch('countries.json', 'url_pages.txt')
    print(f'В документе было найдено {wiki_url_pages.end} стран')
    time.sleep(1)
    for country, url in tqdm(wiki_url_pages, desc='Получение URL стран', unit='countries'):
        continue
    print(f'Конец получения URL {datetime.utcnow()}')

    print(f'Начало получения MD5 {datetime.utcnow()}')
    for item in get_md5('countries.json'):
        print(item)

    print(f'Конец получения MD5 {datetime.utcnow()}')

import os
import requests
from glob import glob1

STORAGE_LINK = os.getenv('STORAGE_LINK')

TRANSLATE_API_KEY = os.getenv('STORAGE_LINK')
TRANSLATE_URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

STORAGE_API_KEY = os.getenv('STORAGE_LINK')
STORAGE_URL = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'

supported_languages = {
    "азербайджанский": "az",
    "албанский": "sq",
    "амхарский": "am",
    "английский": "en",
    "арабский": "ar",
    "армянский": "hy",
    "африкаанс": "af",
    "баскский": "eu",
    "башкирский": "ba",
    "белорусский": "be",
    "бенгальский": "bn",
    "бирманский": "my",
    "болгарский": "bg",
    "боснийский": "bs",
    "валлийский": "cy",
    "венгерский": "hu",
    "вьетнамский": "vi",
    "гаитянский": "ht",
    "галисийский": "gl",
    "голландский": "nl",
    "горномарийский": "mrj",
    "греческий": "el",
    "грузинский": "ka",
    "гуджарати": "gu",
    "датский": "da",
    "иврит": "he",
    "идиш": "yi",
    "индонезийский": "id",
    "ирландский": "ga",
    "итальянский": "it",
    "исландский": "is",
    "испанский": "es",
    "казахский": "kk",
    "каннада": "kn",
    "каталанский": "ca",
    "киргизский": "ky",
    "китайский": "zh",
    "корейский": "ko",
    "коса": "xh",
    "кхмерский": "km",
    "лаосский": "lo",
    "латынь": "la",
    "латышский": "lv",
    "литовский": "lt",
    "люксембургский": "lb",
    "малагасийский": "mg",
    "малайский": "ms",
    "малаялам": "ml",
    "мальтийский": "mt",
    "македонский": "mk",
    "маори": "mi",
    "маратхи": "mr",
    "марийский": "mhr",
    "монгольский": "mn",
    "немецкий": "de",
    "непальский": "ne",
    "норвежский": "no",
    "панджаби": "pa",
    "папьяменто": "pap",
    "персидский": "fa",
    "польский": "pl",
    "португальский": "pt",
    "румынский": "ro",
    "русский": "ru",
    "себуанский": "ceb",
    "сербский": "sr",
    "сингальский": "si",
    "словацкий": "sk",
    "словенский": "sl",
    "суахили": "sw",
    "сунданский": "su",
    "таджикский": "tg",
    "тайский": "th",
    "тагальский": "tl",
    "тамильский": "ta",
    "татарский": "tt",
    "телугу": "te",
    "турецкий": "tr",
    "удмуртский": "udm",
    "узбекский": "uz",
    "украинский": "uk",
    "урду": "ur",
    "финский": "fi",
    "французский": "fr",
    "хинди": "hi",
    "хорватский": "hr",
    "чешский": "cs",
    "шведский": "sv",
    "шотландский": "gd",
    "эстонский": "et",
    "эсперанто": "eo",
    "яванский": "jv",
    "японский": "ja",
}


def translate_it(input_path, output_path, from_lang, to_lang):
    with open(input_path, mode='r', encoding='utf-8') as ff:
        text = ff.read()

    params = {
        'key': TRANSLATE_API_KEY,
        'text': text,
        'lang': f'{from_lang}-{to_lang}',
    }

    response = requests.get(TRANSLATE_URL, params=params)
    json_dict = response.json()

    with open(output_path, mode='w', encoding='utf-8') as fe:
        fe.write(''.join(json_dict['text']))


def upload_to_storage():
    print("+" * 65)
    print("Происходит загрузка файлов на Яндекс.Диск")
    print("+" * 65)

    upload_files = glob1('after', '*.txt')
    for file in upload_files:

        headers = {
            "Accept": "application/json",
            "Authorization": "OAuth " + STORAGE_API_KEY,
            "Host": "cloud-api.yandex.net"
        }

        params = {
            'path': f'/netology/{file}',
            'overwrite': True,
        }

        response_1 = requests.get(STORAGE_URL, headers=headers, params=params)
        assert str(response_1.status_code).startswith("2"), f"Ошибка {str(response_1.status_code)}"

        json_dict = response_1.json()
        upload_link = json_dict['href']

        with open(f"after/{file}", 'rb') as fh:
            up_file = {'file': fh}

            response_2 = requests.put(upload_link, headers=headers, files=up_file)
            assert str(response_2.status_code).startswith("2"), f"Ошибка {str(response_2.status_code)}"
            print(f"Файл {file} был успешно загружен на Яндекс.Диск")
            print("-" * 65)


def main():
    input_paths = glob1('before', '*.txt')
    for input_path in input_paths:

        from_lang = input_path[:-4].lower()

        supp_lang = input("Показать список поддерживаемых языков и их аббревеатуры? (Да/Нет) ")
        if supp_lang.capitalize() == 'Да':
            for language, abbreviation in supported_languages.items():
                print(f"{language.capitalize()}: {abbreviation}")
            print("-" * 25)
        main_flag = True
        while main_flag:
            to_lang = input(
                f"Введите язык (английский, русский и т.д) на который необходимо перевести файл '{input_path}', "
                f"если поле пустое, то язык будет выбран русский: ")
            if to_lang != '':
                try:
                    to_lang = supported_languages[to_lang.lower()]
                    main_flag = False
                except KeyError:
                    print(
                        "Вы ввели неверно язык или такого языка нет в списке поддерживаемых, проверьте правильность "
                        "ввода!")
                    continue
            else:
                to_lang = 'ru'

        output_path = f"{input_path[:-4]}_translate_to_{to_lang.upper()}.txt"

        translate_it(input_path=f"before/{input_path}",
                     output_path=f"after/{output_path}",
                     from_lang=from_lang,
                     to_lang=to_lang)

    upload_to_storage()


if __name__ == '__main__':
    main()
    print(f"Просмотреть файлы можно по ссылке: {STORAGE_LINK}")

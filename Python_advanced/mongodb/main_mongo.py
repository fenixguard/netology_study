import csv
import datetime

from pymongo import MongoClient, ASCENDING


def read_data(csv_file, db):
    """
    Загрузить данные в бд из CSV-файла
    """
    events = db['events']

    with open(csv_file, encoding='utf8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.DictReader(csvfile)
        entries = list()
        for entry in reader:
            temp = entry['Дата'].split('.')
            date = datetime.datetime(year=2020, month=int(temp[1]), day=int(temp[0]))
            artist = entry['Исполнитель']
            place = entry['Место']
            place = place.replace('.', ' ')
            price = int(entry['Цена'])

            event = {
                'artist': artist,
                'price': price,
                'place': place,
                'date': date
            }
            entries.append(event)
        return events.insert_many(entries)


def find_cheapest(db):
    """
    Отсортировать билеты из базы по возрастанию цены
    Документация: https://docs.mongodb.com/manual/reference/method/cursor.sort/
    """

    for event in db.events.find().sort('price', ASCENDING):
        print(f"Исполнитель: {event['artist']}\n"
              f"Место: {event['place']}\n"
              f"Дата: {event['date']}\n"
              f"Цена: {event['price']}\n"
              f"-----------------------------------"
              )


def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке, например "Seconds to"),
    и вернуть их по возрастанию цены
    """
    print(f"Билеты по запросу '{name}'")
    print('-' * 35)
    ticket = str()
    for event in db.events.find({'artist': {'$regex': name}}).sort('price', ASCENDING):
        ticket += (f"Исполнитель: {event['artist']}\n"
                   f"Место: {event['place']}\n"
                   f"Дата: {event['date']}\n"
                   f"Цена: {event['price']}\n"
                   f"-----------------------------------\n"
                   )
    if ticket:
        return ticket
    else:
        return 'Не найдено!'


def find_by_date(date, db):
    date_start = datetime.datetime(2020, date[1], date[0])
    date_end = datetime.datetime(2020, date[3], date[2])
    print(f"Билеты с {date[0]}-{date[1]}-2020 по {date[2]}-{date[3]}-2020")
    print('-' * 35)
    ticket = str()
    for event in db.events.find({'date': {'$gte': date_start, '$lte': date_end}}).sort('date', ASCENDING):
        ticket += (f"Исполнитель: {event['artist']}\n"
                   f"Место: {event['place']}\n"
                   f"Дата: {event['date']}\n"
                   f"Цена: {event['price']}\n"
                   f"-----------------------------------\n"
                   )
    if ticket:
        return ticket
    else:
        return 'Не найдено!'


def main():
    client = MongoClient()
    netology_db = client['netology']

    csv_file = 'artists.csv'

    read_data(csv_file, db=netology_db)

    find_cheapest(db=netology_db)

    print(find_by_name('Seconds to', db=netology_db))

    print(find_by_date(date=[1, 7, 30, 7], db=netology_db))


if __name__ == '__main__':
    main()

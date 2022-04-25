import csv
import re

from application.contact import Contact
from application.phone_book import PhoneBook

IDENTITY_DATA = re.compile(
    r'^(?P<lastname>.*?)\W+(?P<firstname>.*?)\W+(?P<surname>.*?)\W+(?P<organization>.*?)\W+(?P<position>.*?),(?P<phone>.*?),(?P<email>.*?)$')


def input_data():
    phone_book = PhoneBook()
    with open("phonebook_raw.csv", mode='r', encoding='utf8') as ff:
        rows = csv.reader(ff, delimiter="\n")
        contacts_list = list(rows)

        for contact in contacts_list:
            person = Contact(IDENTITY_DATA.findall(contact[0])[0])
            phone_book.add_contact(contact=person)
    return phone_book


def write_data(contacts_list):
    with open("phonebook.csv", mode="w", encoding='utf8') as fe:
        writer = csv.writer(fe, delimiter=',')
        writer.writerows(contacts_list)


if __name__ == '__main__':
    phone_book = input_data()
    contacts_list = phone_book.get_contacts_list()
    write_data(contacts_list=contacts_list)

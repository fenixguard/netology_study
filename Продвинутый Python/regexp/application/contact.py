import re


class Contact:

    def __init__(self, person):
        self.lastname = person[0]
        self.firstname = person[1]
        self.surname = person[2]
        self.organization = person[3]
        self.position = person[4]
        self.phone = create_phone_number(phone_number=person[5])
        self.email = person[6]

    def update_contact(self, update_contact):
        self.lastname = self.lastname or update_contact.lastname
        self.firstname = self.firstname or update_contact.firstname
        self.surname = self.surname or update_contact.surname
        self.organization = self.organization or update_contact.organization
        self.position = self.position or update_contact.position
        self.phone = self.phone or update_contact.phone
        self.email = self.email or update_contact.email


def create_phone_number(phone_number):
    number = re.sub(r'\D', '', phone_number)
    if len(number) > 11:
        return f"+7({number[1:4]}){number[4:7]}-{number[7:9]}-{number[9:11]} доб.{number[11:16]}"
    elif len(number) == 11:
        return f"+7({number[1:4]}){number[4:7]}-{number[7:9]}-{number[9:11]}"
    elif len(number) == 10:
        return f"+7({number[0:3]}){number[3:6]}-{number[6:8]}-{number[8:10]}"
    elif phone_number == 'phone':
        return 'phone'
    else:
        return ''



class Contact:

    def __init__(self, first_name, second_name, phone_number, favorite_contact=False, **kwargs):
        self.first_name = first_name
        self.second_name = second_name
        self.phone_number = phone_number
        self.favorite_contact = favorite_contact
        self.additional_information = ''
        if kwargs:
            for key, value in kwargs.items():
                self.additional_information += f'\t\t{key}: {value}\n'
        else:
            self.additional_information = '\t\tОтсутствует\n'

    def __str__(self):
        return '\n'.join([f'Имя: {self.first_name}',
                          f'Фамилия: {self.second_name}',
                          f'Телефон: {self.phone_number}',
                          'В избранных: да' if self.favorite_contact else 'В избранных: нет',
                          'Дополнительная информация:',
                          f'{self.additional_information}'])


class PhoneBook:

    def __init__(self, name_book):
        self.name_book = name_book
        self.contacts = list()
        print(f"Вы создали телефонную книгу под именем {self.name_book}")
        print("-" * 25)

    def show_all(self):
        if self.contacts:
            print(f"Телефонная книга '{self.name_book}' содержит {len(self.contacts)} контактов")
            print("-" * 25)
            for contact in self.contacts:
                print(f"{contact}")
            print("-" * 25)
        else:
            print(f"В телефонной книге '{self.name_book}' нет контактов!")
            print("-" * 25)

    def add_contact(self, contact):
        if contact in self.contacts:
            print("Контакт был добавлен ранее")
            print("-" * 25)
        else:
            self.contacts.append(contact)
            print(f"Контакт {contact.first_name} {contact.second_name} добавлен")
            print("-" * 25)

    def delete_contact(self, phone_number):
        for contact in self.contacts:
            if contact.phone_number == phone_number:
                self.contacts.remove(contact)
                print(f"Контакт '{contact.first_name} {contact.second_name}' с номером {contact.phone_number} удален")
                print("-" * 25)
                return None
        print(f"Контакт с номером {phone_number} отсутствует в телефонной книге")
        print("-" * 25)

    def show_all_favorite(self):
        favorite_contacts = [contact for contact in self.contacts if contact.favorite_contact]
        if not favorite_contacts:
            print("В телефонной книге нет избранных контактов")
            print("-" * 25)
        else:
            print(f"Избранных контактов {len(favorite_contacts)}:")
            print("-" * 25)
            for favorite in favorite_contacts:
                print(f"{favorite}")
            print("-" * 25)

    def get_contact(self, first_name, second_name):
        if not self.contacts:
            print(f"Телефонная книга '{self.name_book}' пустая")
            return None
        for contact in self.contacts:
            if contact.first_name == first_name and contact.second_name == second_name:
                print(contact)
                return None
        print(f"{first_name} {second_name} отсутствует")


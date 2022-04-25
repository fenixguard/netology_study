from application.base_classes import Contact, PhoneBook

if __name__ == '__main__':
    John = Contact('John', 'Travolta', '2145987563', email='travolta@gmail.com', telegram='@Travolta',
                   address='New York, NY, 10120, USA')
    Davy = Contact('Davy', 'Jones', '8546123578', favorite_contact=True, email='davijones@gmail.com',
                   telegram='@davijones')
    Olivia = Contact('Olivia', 'Wild', '9854693214', favorite_contact=True)
    Tom = Contact('Tom', 'Cruise', '4589621547', email='mission_impossible@gmail.com', telegram='@possible',
                  twitter='Cruise_Strong')
    Steven = Contact('Steven', 'Spielberg', '1478952365', favorite_contact=True, email='super_8@gmail.com',
                     telegram='@steven')

    phone_book = PhoneBook('Домашняя')

    PhoneBook.get_all(phone_book)

    PhoneBook.add_contact(phone_book, John)
    PhoneBook.add_contact(phone_book, Davy)
    PhoneBook.add_contact(phone_book, Olivia)
    PhoneBook.add_contact(phone_book, Tom)
    PhoneBook.add_contact(phone_book, Steven)

    PhoneBook.get_all(phone_book)

    PhoneBook.delete_contact(phone_book, '1478952365')
    PhoneBook.delete_contact(phone_book, '1478952365')
    PhoneBook.get_all_favorite(phone_book)

    PhoneBook.get_contact(phone_book, 'Olivia', 'Wild')
    PhoneBook.get_contact(phone_book, 'Barak', 'Obama')


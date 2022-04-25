class PhoneBook:
    def __init__(self):
        self.contacts = dict()

    def add_contact(self, contact):
        lastname = contact.lastname
        if lastname in self.contacts:
            self.contacts[lastname].update_contact(contact)
        else:
            self.contacts[lastname] = contact

    def get_contacts_list(self):
        contact_list = list()
        for contact in self.contacts.values():
            contact_list.append([contact.lastname,
                                 contact.firstname,
                                 contact.surname,
                                 contact.organization,
                                 contact.position,
                                 contact.phone,
                                 contact.email])
        return contact_list

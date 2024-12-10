class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'Имя: {self.name}, Телефон: {self.phone}, Email: {self.email}'


class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                break

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def list_contacts(self):
        for contact in self.contacts:
            print(contact)


class User:
    def __init__(self, username):
       self.username = username
       self.contact_list = ContactList()  # «Компоновщик» (Composite) — паттерн, который объединяет несколько объектов в древовидную структуру

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contact_list.add_contact(contact)

    def remove_contact(self, name):
        self.contact_list.remove_contact(name)

    def show_contacts(self):
        print(f'\nКонтакты пользователя {self.username}:')
        self.contact_list.list_contacts()


user = User("Петя")

user.add_contact("Иван", "123456789", "ivan@example.com")
user.add_contact("Мария", "987654321", "maria@example.com")
user.show_contacts()

user.remove_contact("Иван")
user.show_contacts()


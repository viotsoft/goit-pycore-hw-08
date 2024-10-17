import pickle


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"Contact (Name: {self.name}, Phone: {self.phone})"


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def __repr__(self):
        return f"AddressBook(Contacts: {self.contacts})"


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook() # Повернення нової адресної книги, якщо файл не знайдено

def main():
    book = load_data()

    while True:
        action = input("Choose an action: 1) Add contact 2) Show contacts 3) Exit: ")

        if action == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            contact = Contact(name, phone)
            book.add_contact(contact)
            print(f"Contact {contact} added")

        elif action == '2':
            print("Address Book.")
            for contact in book.contacts:
                print(contact)

        elif action == '3':
            save_data(book)
            print("Address book saved. Exiting.")
            break

        else:
            print("Invalid action. Please try again.")

if __name__=="__main__":
    main()

import sys

# Initialize the contact book as an empty list
contact_book = []


def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contact_book.append(contact)
    print("Contact added successfully!\n")


def view_contacts():
    if not contact_book:
        print("No contacts available.\n")
    else:
        print("Contact List:")
        for idx, contact in enumerate(contact_book, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")
        print()


def search_contact():
    query = input("Enter name or phone number to search: ").lower()
    results = [contact for contact in contact_book if query in contact['name'].lower() or query in contact['phone']]

    if not results:
        print("No matching contacts found.\n")
    else:
        print("Search Results:")
        for contact in results:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print()


def update_contact():
    query = input("Enter the name or phone number of the contact to update: ").lower()
    for contact in contact_book:
        if query in contact['name'].lower() or query in contact['phone']:
            print("Contact found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")

            contact['name'] = input("Enter new name: ")
            contact['phone'] = input("Enter new phone number: ")
            contact['email'] = input("Enter new email address: ")
            contact['address'] = input("Enter new address: ")
            print("Contact updated successfully!\n")
            return
    print("No matching contact found to update.\n")


def delete_contact():
    query = input("Enter the name or phone number of the contact to delete: ").lower()
    for contact in contact_book:
        if query in contact['name'].lower() or query in contact['phone']:
            contact_book.remove(contact)
            print("Contact deleted successfully!\n")
            return
    print("No matching contact found to delete.\n")


def main():
    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the contact book. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")


if __name__ == "__main__":
    main()

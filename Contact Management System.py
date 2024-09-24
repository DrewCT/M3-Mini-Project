import re
import json

contacts = {}

def display_menu():
    print("\nWelcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")
    
def add_contact():
    print("\nAdding a new contact:")
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    additional_info = input("Enter additional info (optional): ")
    
    if validate_phone(phone) and validate_email(email):
        contacts[phone] = {
            "name": name,
            "phone": phone,
            "email": email,
            "additional_info": additional_info
        }
        print(f"Contact for {name} added successfully!")
    else:
        print("Invalid phone number or email address.")

def edit_contact():
    phone = input("\nEnter the phone number of the contact to edit: ")
    if phone in contacts:
        name = input("Enter new name (leave blank to keep current): ")
        email = input("Enter new email (leave blank to keep current): ")
        additional_info = input("Enter new additional info (leave blank to keep current): ")

        if name:
            contacts[phone]['name'] = name
        if validate_email(email):
            contacts[phone]['email'] = email
        if additional_info:
            contacts[phone]['additional_info'] = additional_info
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    phone = input("\nEnter the phone number of the contact to delete: ")
    if phone in contacts:
        del contacts[phone]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def search_contact():
    phone = input("\nEnter the phone number of the contact to search: ")
    if phone in contacts:
        print(f"\nDetails for {contacts[phone]['name']}:")
        print(f"Phone: {contacts[phone]['phone']}")
        print(f"Email: {contacts[phone]['email']}")
        print(f"Additional Info: {contacts[phone]['additional_info']}")
    else:
        print("Contact not found.")

def display_all_contacts():
    if contacts:
        print("\nAll contacts:")
        for contact in contacts.values():
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Additional Info: {contact['additional_info']}")
    else:
        print("\nNo contacts available.")

def export_contacts():
    with open("contacts.txt", "w") as file:
        json.dump(contacts, file)
    print("Contacts exported to contacts.txt successfully!")

def import_contacts():
    try:
        with open("contacts.txt", "r") as file:
            imported_contacts = json.load(file)
            contacts.update(imported_contacts)
        print("Contacts imported successfully!")
    except FileNotFoundError:
        print("No file found to import from.")

def validate_phone(phone):
    return re.match(r"^\+?\d{10,15}$", phone) is not None

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        try:
            if choice == '1':
                add_contact()
            elif choice == '2':
                edit_contact()
            elif choice == '3':
                delete_contact()
            elif choice == '4':
                search_contact()
            elif choice == '5':
                display_all_contacts()
            elif choice == '6':
                export_contacts()
            elif choice == '7':
                import_contacts()
            elif choice == '8':
                print("Exiting the Contact Management System.")
                break
            else:
                print("Invalid option. Please select a valid menu option.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()
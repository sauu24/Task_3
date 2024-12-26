import json

# File to store contacts
CONTACTS_FILE = 'contacts.json'

# Load contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']}")

# Edit a contact
def edit_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter contact number to edit: ")) - 1
        if 0 <= index < len(contacts):
            contacts[index]['name'] = input("Enter New Name: ") or contacts[index]['name']
            contacts[index]['phone'] = input("Enter New Phone Number: ") or contacts[index]['phone']
            contacts[index]['email'] = input("Enter New Email: ") or contacts[index]['email']
            save_contacts(contacts)
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            contacts.pop(index)
            save_contacts(contacts)
            print("Contact deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

# Main Menu
def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


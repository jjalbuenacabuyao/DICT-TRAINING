contacts = []

def add_contacts(name: str, phone_number: str, email: str) -> None:
    user_profile = {
        "name": name,
        "phone_number": phone_number,
        "email": email
    }

    contacts.append(user_profile)


def display_contacts():
    for contact in contacts:
        name = contact["name"]
        phone_number = contact["phone_number"]
        email = contact["email"]

        print(f"Name: {name}\nPhone number: {phone_number}\nEmail: {email}")
        print()


def search_contact(contact_name: str):
    for contact in contacts:
        if contact_name == contact["name"]:
            name = contact["name"]
            phone_number = contact["phone_number"]
            email = contact["email"]

            print(f"Name: {name}\nPhone number: {phone_number}\nEmail: {email}")

        else:
            print("Contact not found.")


def edit_contact(contact_name: str):
    for contact in contacts:
        if contact["name"] == contact_name:
            edited_number = input("Enter new phone number: ")
            edited_email = input("Enter a new email: ")

            contact["phone_number"] = edited_number
            contact["email"] = edited_email
        else:
            print("Contact not found")


def remove_contact(name: str):
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print(f"{name} deleted successfully")
            return
        
    print("Contact not found")


while True:
    print("""
Menu:
    a - Add new Contact
    b - Display all contact
    c - Search for a contact
    d - Edit a contact
    e - Remove a contact
    f - Exit the program
""")
    
    command = input("Enter command: ").lower()

    if command == "a":
        print("ADD NEW CONTACT")
        name = input("Enter the name: ").title()
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")

        add_contacts(name, phone_number, email)
        print(f"{name} added successfully")
    
    elif command == "b":
        display_contacts()
    
    elif command == "c":
        print("SEARCH CONTACT")
        name = input("Enter the name of the person you want to search: ").title()

        search_contact(name)
    
    elif command == "d":
        print("EDIT CONTACT")
        name = input("Enter the name of the person you want to edit: ").title()

        edit_contact(name)

    elif command == "e":
        print("DELETE CONTACT")
        name = input("Enter the name of the person you want to delete: ").title()

        remove_contact(name)

    elif command == "f":
        print("Exiting program....")
        break

    else:
        print("Imvalid command")

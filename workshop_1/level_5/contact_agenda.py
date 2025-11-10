agenda = []

# add_contact: create a contact dict and append it to the agenda, then print confirmation
def add_contact(name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
    }
    agenda.append(contact)
    print(f"Contact {name} added successfully.")

# menu: text shown to the user with available actions
menu = (""
        "1. Add a new contact.\n"
        "2. View all contacts.\n"
        "3. Update a contact.\n"
        "4. Delete a contact.\n"
        "5. Search for a contact.\n"
        "6. Exit\n")

# attribute_available: check if a given attribute value is unique in the agenda
def attribute_available(value, attribute):
    for contact in agenda:
        if contact[attribute] == value:
            return False
    return True

# update_attribute: find contact by name and update the specified attribute
def update_attribute(value, attribute, name):
    for contact in agenda:
        if contact["name"] == name:
            contact[attribute] = value
            print(f"Contact {name} updated successfully.")
            break

# delete_contact: remove a contact by name and print confirmation
def delete_contact(name):
    for contact in agenda:
        if contact["name"] == name:
            print(f"Contact {name} deleted successfully.")
            agenda.remove(contact)
            break

# main loop: display menu and handle user choices until exit
while True:
    print("Welcome to Contact Agenda")
    option = input(menu)

    if option == "1":
        # Option 1 - Add: validate inputs and uniqueness, then add contact
        while True:
            flag = True
            name = input("Enter the name: ").capitalize()
            if name == "":
                print("Please enter a valid name.")
                flag = False
            else:
                flag = attribute_available(name, "name")
            if flag:
                break
            else:
                print("This name is not available.")
        while True:
            flag = True
            phone = input("Enter the phone number: ")
            if phone == "":
                print("Please enter a valid phone number.")
                flag = False
            else:
                flag = attribute_available(phone, "phone")
            if flag:
                break
            else:
                print("This phone number is not available.")
        while True:
            flag = True
            email = input("Enter the email: ")
            if email == "":
                email = "No apply"
            else:
                flag = attribute_available(email, "email")
            if flag:
                break
            else:
                print("This email is not available.")
        add_contact(name, phone, email)
    elif option == "2":
        # Option 2 - View: iterate over agenda and print each contact
        for contact in agenda:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    elif option == "3":
        # Option 3 - Update: locate contact, ask which field to change, validate and update
        name = input("Enter the contact name: ").capitalize()
        if not attribute_available(name, "name"):
            print("What do you want to change? ")
            subchoice = input("1. Name\n2. Phone\n3. Email\n4. Exit\n")
            if subchoice == "1":
                new_name = input("Enter the new name: ").capitalize()
                if new_name == "":
                    print("Invalid name")
                else:
                    flag = attribute_available(name, "name")
                    if flag:
                        update_attribute(new_name, "name", name)
                    else:
                        print("This name is not available.")
            elif subchoice == "2":
                new_phone = input("Enter the new phone number: ")
                if new_phone == "":
                    print("Invalid phone number")
                else:
                    flag = attribute_available(new_phone, "phone")
                    if flag:
                        update_attribute(new_phone, "phone", name)
                    else:
                        print("This phone number is not available.")
            elif subchoice == "3":
                new_email = input("Enter the new email address: ")
                if new_email == "":
                    print("Invalid email address")
                else:
                    flag = attribute_available(new_email, "email")
                    if flag:
                        update_attribute(new_email, "email", name)
                    else:
                        print("This email is not available.")
            else:
                print("Invalid choice")
        else:
            print("This contact doesn't exist")
    elif option == "4":
        # Option 4 - Delete: verify contact exists then remove it
        name = input("Enter the contact name: ").capitalize()
        if not attribute_available(name, "name"):
            delete_contact(name)
        else:
            print("This contact doesn't exist")
    elif option == "5":
        # Option 5 - Search: look up contact by name and display if found
        flag = True
        name = input("Enter the contact name: ").capitalize()
        for contact in agenda:
            if contact["name"] == name:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
                flag = False
                break
        if flag:
            print("This contact doesn't exist")
    elif option == "6":
        # Option 6 - Exit: print farewell and break the loop
        print("Thanks for using the agenda")
        break
    else:
        # Invalid option: notify the user
        print("Invalid option")
contacts = []

while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contact = {
            "name": name,
            "phone": phone
        }

        contacts.append(contact)
        print("Contact added successfully.")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nAll Contacts:")
            for contact in contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print()

    elif choice == "3":
        name = input("Enter name to search: ")

        found = False

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                found = True

        if found == False:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")

        found = False

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                contacts.remove(contact)
                print("Contact deleted.")
                found = True
                break

        if found == False:
            print("Contact not found.")

    elif choice == "5":
        print("Thank you for using Contact Book.")
        break

    else:
        print("Invalid choice.")

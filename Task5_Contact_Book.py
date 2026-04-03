# Task 5 - Contact Book
# CodSoft Python Internship - Azhaan Azam

contacts = []

def add_contact():
    print("\n➕ Add New Contact")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    print(f"✅ Contact '{name}' added successfully!")

def view_contacts():
    if len(contacts) == 0:
        print("\n📒 No contacts found! Add some contacts first.")
    else:
        print("\n📒 Your Contacts:")
        print("-" * 40)
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. 👤 {contact['name']} | 📞 {contact['phone']}")
        print("-" * 40)

def search_contact():
    print("\n🔍 Search Contact")
    keyword = input("Enter name or phone number to search: ").lower()
    found = []
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            found.append(contact)
    if len(found) == 0:
        print("❌ No contact found!")
    else:
        print(f"\n✅ Found {len(found)} contact(s):")
        print("-" * 40)
        for contact in found:
            print(f"👤 Name:    {contact['name']}")
            print(f"📞 Phone:   {contact['phone']}")
            print(f"📧 Email:   {contact['email']}")
            print(f"🏠 Address: {contact['address']}")
            print("-" * 40)

def update_contact():
    view_contacts()
    if len(contacts) == 0:
        return
    try:
        num = int(input("\nEnter contact number to update: "))
        if 1 <= num <= len(contacts):
            contact = contacts[num - 1]
            print(f"\n✏️ Updating '{contact['name']}' (press Enter to keep current value)")
            name = input(f"Name [{contact['name']}]: ")
            phone = input(f"Phone [{contact['phone']}]: ")
            email = input(f"Email [{contact['email']}]: ")
            address = input(f"Address [{contact['address']}]: ")
            if name: contact['name'] = name
            if phone: contact['phone'] = phone
            if email: contact['email'] = email
            if address: contact['address'] = address
            print("✅ Contact updated successfully!")
        else:
            print("❌ Invalid contact number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def delete_contact():
    view_contacts()
    if len(contacts) == 0:
        return
    try:
        num = int(input("\nEnter contact number to delete: "))
        if 1 <= num <= len(contacts):
            removed = contacts.pop(num - 1)
            print(f"🗑️ Contact '{removed['name']}' deleted successfully!")
        else:
            print("❌ Invalid contact number!")
    except ValueError:
        print("❌ Please enter a valid number!")

print("===== Contact Book =====")

while True:
    print("\nMenu:")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

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
        print("\n👋 Goodbye! Your contacts are safe!")
        break
    else:
        print("❌ Invalid choice! Please enter 1-6.")
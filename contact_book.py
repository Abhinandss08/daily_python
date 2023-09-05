'''
Create a contact book:
A python program to add, view ,search and delete contacts from a contact book.
Contact list must contain name, email and phone number from user.
The prgrm needs to be running until the user decides to terminate the program.
Add - To add contact details to contact book
View - To view the entire contact in the contact book one by one.
Search - For searching a contact by name and display the contact details.
Delete - To delete a contact from the contact book………
'''

# Empty list to add contacts, by declaring on top of methods as a
# global variable gives access to the proceeding functions
contact_book = []


# To add contacts to the contact book
def addContact():
    name_ = input('Enter your name\t')
    email_ = input('Enter your email\t')
    phone = input('Enter your phone number\t')
    # Creating a dictionary of data
    contact = {'Name': name_, 'Email': email_, 'Phone': phone}
    # Adding data to the existing contact book
    contact_book.append(contact)
    print(f'{name_} is added to the contact list')
    print('_________________________________________________________')


def viewContact():
    # Checks whether contact book empty or not
    if not contact_book:
        print('Contact list is empty')
    else:
        # Enumerate fn is used for a count and the value from the
        # contact book list [iterable]
        for index, contact in enumerate(contact_book, start=1):
            print(f"{index}.Name:{contact['Name']}, Email:{contact['Email']}"
                  f", Phone:{contact['Phone']}")
        print('_________________________________________________________')


def searchContact():
    search_name = input('Enter the name you want to search\t')
    # Empty list to store the contact that matches data
    found_contacts = []

    # Iterating over the list to get the dictionary at each index position
    for contact in contact_book:
        # Checking whether the name matches the dictionary
        # value in each iteration
        if search_name.lower() in contact['Name'].lower():
            # Append dictionary to the empty list
            found_contacts.append(contact)

    # Checks whether the dictionary is empty or not
    if found_contacts:
        # If not empty start a counter and print values from the
        # dictionary using enumerate fn
        for index, contact in enumerate(found_contacts, start=1):
            print(f"{index}.Name:{contact['Name']}, "
                  f"Email:{contact['Email']}, Phone:{contact['Phone']}")
            print('_________________________________________________________')
    # Dictionary is empty, which implies false condition
    else:
        print('Name nowhere to be found')
        print('_________________________________________________________')


def deleteContact():
    delete_name = input('Enter the name you want to delete\t')
    # Set as a flag variable, later to verify name is present or not
    # The code initializes delete_status to False, assuming
    # initially that the name to be deleted is not found.
    delete_status = False

    # Iterating over the list to get the dictionary at each index position
    for contact in contact_book:
        # Checking whether the name matches the dictionary
        # value in each iteration
        if delete_name.lower() == contact['Name'].lower():
            # Removes dictionary from the contact_book list
            contact_book.remove(contact)
            print(f"{delete_name} is deleted from contact_book")
            print('_________________________________________________________')
            # When name is found out flag variable is changed
            delete_status = True
            break
    # If flag variable is changed name is present, else not present
    # Checks whether delete_status is still False
    if not delete_status:
        print(f'{delete_name} can not be found')
        print('_________________________________________________________')


# For continuous execution of program unless user decided to terminate it
while True:
    choice = int(input('1.Add Contact\n2.View contact\n3.Search contact\n'
                       '4.Delete contact\n5.Quit\nEnter your choice\t'))
    if choice == 1:
        addContact()
    elif choice == 2:
        viewContact()
    elif choice == 3:
        searchContact()
    elif choice == 4:
        deleteContact()
    elif choice == 5:
        break
    else:
        print('Invalid choice')
        print('_________________________________________________________')

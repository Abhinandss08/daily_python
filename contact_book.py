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


while True:
    choice = int(input('1.Add Contact\n2.View contact\n3.Search contact\n'
                       '4.Delete contact\n5.Quit\nEnter your choice\t'))
    if choice == 1:
        addContact()
    elif choice == 2:
        viewContact()
    elif choice == 5:
        break
    else:
        print('Invalid choice')
        print('_________________________________________________________')

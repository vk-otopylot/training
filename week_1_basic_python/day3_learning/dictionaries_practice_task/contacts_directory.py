contacts = {}

# person_no = int(input('How many person you want to add to the contacts: '))
#
# for i in range(person_no):
#     name = input('Enter the name of the person: ')
#     m_no = int(input('Enter the mobile number of the person: '))
#     contacts[name] = m_no
#
# p_name = input('Enter the name of the person you want to get mobile no: ')
#
# print(contacts[p_name])


# Using while loop

while True:
    choice = input('Enter your choice: \n1.Add Contact\n2.Remove Contact\n3.Delete all\n4.Display all\n5.Search\n6.Exit\n')
    if choice == '6':
        break

    elif choice == '1':
        name = input('Enter the name of the person: ')
        m_no = int(input('Enter the mobile number of the person: '))
        contacts[name] = m_no
        print('Contact added successfully!!!')

    elif choice == '2':
        name = input('Enter the name of the person: ')
        if name not in contacts.keys():
            print('This Person is not in contact')
        else:
            del contacts[name]
            print('Contact deleted successfully')

    elif choice == '3':
        if len(contacts) == 0:
            print('No contact in your directory')
        else:
            contacts.clear()
            print('All contact deleted')

    elif choice == '4':
        if len(contacts) == 0:
            print('No contact in your directory')
        else:
            for key, value in contacts.items():
                print(f'{key}: {value}')

    elif choice == '5':
        name = input('Enter the name of the person: ')
        if name not in contacts.keys():
            print('This Person is not in contact')
        else:
            print(contacts[name])

    else:
        print('Invalid choice')
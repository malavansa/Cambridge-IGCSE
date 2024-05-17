members = []
member_fee = 75
donation = 200
while True:
    print('Menu: 1. Add records 2. Exit')
    option = int(input('Enter the option: you must select the number'))
    if option == 1:
        first_name = input('Enter the first name: ')
        last_name = input('Enter the last name: ')
        full_name = first_name + ' ' + last_name
        members.append(full_name)

    else:
        break
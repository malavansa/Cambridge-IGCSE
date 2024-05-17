from datetime import datetime
import re
members = {}
membership_amount = 75
def ask_number(min, max):
    while True:
        number = int(input('Enter the choice: '))
        if number >= min and number <= max:
            return number
        else:
            print("please put correct choice")
        
def is_volunteer(option):
    if option == 1:
        return True
    else:
        return False

def get_name():
    while True:
        name = input('Enter your first name: ')
        if name.replace(' ', ''):
            return name
        else:
            print("Name shouldn't be blank")
        
def get_joined_date():
    while True:
        date = input("Enter the date ('YYYY-MM-DD')")
        date = re.findall('\d{4}-\d{2}-\d{2}', date)
        if date:
            try:
                date = datetime.strptime(date[0], "%Y-%m-%d")
            except Exception as er:
                print("please give correct year or month or day")
            else:
                return date
        else:
            print('please enter the date in correct format')
        
def get_payment(option):
    
    is_paid = False
    if option == 1:
        is_paid = True
        return is_paid
    else:
        return False

def add_records():
    full_name = get_name()
    last_name = get_name()
    full_name = full_name + ' ' + last_name
    members[full_name] = {}
    print('Do you wish to pay now? \n1. Yes \n2. True')
    payment_option = ask_number(1, 2)
    payment_info = get_payment(payment_option)
    if payment_info:
        members[full_name]['is_paid'] = payment_info
        members[full_name]['membership_fee'] = 75
   
        print('Do you wish to work as a volunteer? \nOptions: 1. Yes 2. No')
        volunteer_status = ask_number(1, 2)
        
        members[full_name]['volunteer'] = is_volunteer(volunteer_status)
        if is_volunteer(volunteer_status):
            print("If you are a volunteer, please select area from")
            print("Options: \n1. working at the pier entrance gate \n2. working in the gift shop \n3. painting and decorating")
            area = ask_number(1, 3)
            if area == '1':
                members[full_name]['volunteer_area'] = 'working at the pier entrance gate'
            elif area == '2':
                members[full_name]['volunteer_area'] = 'working in the gift shop'
            else:
                members[full_name]['volunteer_area'] = 'painting and decorating'
    else:
        join_date = get_joined_date()
        members[full_name]['joined_date'] = join_date.date()

def reports_view():
    print(f'Total members: {len(members)}')

while True:
    print('Enter the options: ')
    print('1. Add records \n2. Reports View \n3.Exit')
    option = ask_number(1, 3)
    if option == 1:
        add_records()
    elif option == 2:
        reports_view()
    else:
        break
print(members)


    
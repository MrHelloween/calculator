import calculator


def menu():
    print('''1. calculator \n2. Exit''')

    number_menu = int(input('Choose a number: '))
    if number_menu == 1:
        under_the_menu_calculator(number_menu)
    elif number_menu == 2:
        print('The calculator has finished its work')


def under_the_menu_calculator(number_menu):
    if number_menu == 1:
        print(''' 
1. addition(+)
2. subtraction(-)
3. multiplication(*)
4. division(/)
5. exponentiation(**)
6. square
7. back 
        ''')

    under_the_menu_number = int(input('Select an operation: '))
    exit = ''
    if under_the_menu_number == 6:
        while exit.lower() != 't':
            a = int(input('Enter number: '))
            result = operation(under_the_menu_number, a, )
            print(f'Result operation: {result:,.2f}')
            exit = input('if you want to exit enter T/t if not F/f: ')
        under_the_menu_calculator(1)
    elif under_the_menu_number == 7:
        menu()
    else:
        while exit.lower() != 't':
            a = int(input('Enter the first number: '))
            b = int(input('Enter the second digit: '))
            result = operation(under_the_menu_number, a, b)
            print(f'Result operation: {result:,.2f}')
            exit = input('if you want to exit enter T/t if not F/f: ')
        under_the_menu_calculator(1)


def operation(num, a, b=None):
    if num == 1:
        return calculator.addition(a, b)
    elif num == 2:
        return calculator.subtraction(a, b)
    elif num == 3:
        return calculator.multiplication(a, b)
    elif num == 4:
        return calculator.division(a, b)
    elif num == 5:
        return calculator.exponentiation(a, b)
    elif num == 6:
        return calculator.sqrt(a)


menu()

import calculator


def menu(number_menu):
    if number_menu == 1:
        under_the_menu_calculator(number_menu)


def under_the_menu_calculator(number_menu):
    if number_menu == 1:
        print(''' 
        1. addition(+)
        2. subtraction(-)
        3. multiplication(*)
        4. division(/)
        ''')
    under_the_menu_number = int(input('Select an operation: '))
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second digit: '))
    result = operation(under_the_menu_number, a, b)
    print(f'Result operation: {result:,.2f}')


def operation(num, a, b):
    if num == 1:
        return calculator.addition(a, b)
    elif num == 2:
        return calculator.subtraction(a, b)
    elif num == 3:
        return calculator.multiplication(a, b)
    elif num == 4:
        return calculator.division(a, b)


print('''1. calculator''')

number_menu = int(input('Choose a number: '))
menu(number_menu)

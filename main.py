import calculator
import BMI
import Word_count


def main():
    number_menu = menu()
    under_the_menu_number = under_the_menu_calculator(number_menu)
    test(under_the_menu_number)


def menu():
    print('''1. calculator \n2. BMI  \n3. Word count \n4. Exit''')

    number_menu = int(input('Choose a number: '))
    if number_menu == 4:
        print('The calculator has finished its work')
    else:
        return number_menu


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
        return under_the_menu_number
    elif number_menu == 2:

        return 2
    elif number_menu == 3:
        print('''1. File with text \n2. Enter text''')
        num_menu = int(input('Enter num: '))
        count_words(num_menu)
        return  None

def test(num):
    try:
        exit = ''
        if num == 6:
            while exit.lower() != 't':
                a = int(input('Enter number: '))
                result = operation(num, a, )
                print(f'Result operation: {result:,.2f}')
                exit = input('if you want to exit enter T/t if not F/f: ')
            main()
        elif num == 7:
            menu()
        elif num == 2:
            while exit.lower() !='t':
                weight = int(input('Enter weight (in kilograms): '))
                height = int(input('Enter height (in centimeters): '))
                result = BMI.bmi(weight, height)
                print(f'BMI: {result}')
                exit = input('if you want to exit enter T/t if not F/f: ')
            main()
        else:
            while exit.lower() != 't':
                a = int(input('Enter the first number: '))
                b = int(input('Enter the second digit: '))
                result = operation(num, a, b)
                print(f'Result operation: {result:,.2f}')
                exit = input('if you want to exit enter T/t if not F/f: ')
            main()
    except:
        pass


def operation(num, a, b=None):
    try:
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
    except ZeroDivisionError:
        print('Error: division by zero')
    except:
        print('Error')


def count_words(num_menu):
    if num_menu == 1:
        text_txt = input('Enter name file with text: ')
        text_line = Word_count.get_text(text_txt)
        list_words_count = Word_count.get_words(text_line)
        result = Word_count.get_the_word_count(list_words_count)
        filter_words_count = Word_count.filter(result)
        print(filter_words_count)
    elif num_menu == 2:
        text = input('Enter text: ')
        list_words_count = Word_count.get_words(text)
        result = Word_count.get_the_word_count(list_words_count)
        filter_words_count = Word_count.filter(result)
        print(filter_words_count)


if __name__ == '__main__':
    main()

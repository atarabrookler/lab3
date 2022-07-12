import math

current_result = 0.0
sum_of_calculations = 0
number_of_calculations = 0


def display_calculator_menu_and_choose():
    # calculator menu
    print('Calculator Menu')
    print('---------------')
    print('0. Exit Program')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exponentiation')
    print('6. Logarithm')
    print('7. Display Average')
    print()


def retrieving_number():
    # retrieving and storing numbers
    number = input()
    if number == 'RESULT':
        return current_result
    return float(number)



def execute_menu(choice, num1, num2):
    global current_result, number_of_calculations
    if choice == 1:
        current_result = num1 + num2
    elif choice == 2:
        current_result = num1 - num2
    elif choice == 3:
        current_result = num1 * num2
    elif choice == 4:
        current_result = num1 / num2
    elif choice == 5:
        current_result = num1 ** num2
    elif choice == 6:
        current_result = math.log(num2, num1)
    number_of_calculations += 1


def new_main():
    global current_result, sum_of_calculations, number_of_calculations
    midst_of_calculation = True
    need_to_display_menu = True
    while midst_of_calculation:
        while need_to_display_menu:
            print(f'Current Result: {current_result}')
            print()
            need_to_display_menu = False
            operator = display_calculator_menu_and_choose()
        # selection from menu
        print('Enter Menu Selection: ', end='')
        operator = int(input())
        need_to_display_menu = True
        if 1 <= operator and operator <= 6:
            print('Enter first operand: ', end='')
            first_num = retrieving_number()
            print('Enter second operand: ', end='')
            second_num = retrieving_number()
        if operator == 0:
            print('Thanks for using this calculator. Goodbye!')
            exit()
            midst_of_calculation = False
        elif 1 <= operator and operator <= 6:
            execute_menu(operator, first_num, second_num)
        elif operator == 7:
            if number_of_calculations == 0:
                print('Error: No calculations yet to average!')
                need_to_display_menu = False
            else:
                average_of_calculations = sum_of_calculations / number_of_calculations
                print(f'Sum of calculations: {sum_of_calculations}')
                print(f'Number of calculations: {number_of_calculations}')
                print(f'Average of calculations: {average_of_calculations:.2f}')
                need_to_display_menu = False
        else:
            print('Error: Invalid selection!')
            need_to_display_menu = False
        sum_of_calculations += current_result


new_main()

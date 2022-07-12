import math
# initialize variables
current_result = 0.0
sum_of_calculations = 0
number_of_calculations = 0


def display_calculator_menu_and_choose():
    """Function: display_calculator_menu_and_choose
    Parameters: --
    Description: displays the calculator's menu
    Return: returns None"""
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
    """Function: retrieving_number
    Parameters: --
    Description: retrieves numbers from user
    Returns: number input from user"""
    # retrieving and storing numbers
    number = input()
    if number == 'RESULT':
        return current_result
    return float(number)



def execute_menu(choice, num1, num2):
    """Function: execute_menu
    Parameters:
    choice- users menu choice selection
    num1- number input by user
    num2- number input by user
    Description: calculates the mathematical function the user requested
    Returns: None"""
    global current_result, number_of_calculations
    if choice == 1: # addition
        current_result = num1 + num2
    elif choice == 2: # subtraction
        current_result = num1 - num2
    elif choice == 3: # multiplication
        current_result = num1 * num2
    elif choice == 4: # division
        current_result = num1 / num2
    elif choice == 5: # power
        current_result = num1 ** num2
    elif choice == 6: # logarithm
        current_result = math.log(num2, num1)
    number_of_calculations += 1


def new_main():
    #initializing variables
    global current_result, sum_of_calculations, number_of_calculations
    midst_of_calculation = True
    need_to_display_menu = True
    # ongoing calculation
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
        # cases where there is a need to preform a mathematical calculation
        if 1 <= operator and operator <= 6:
            print('Enter first operand: ', end='')
            first_num = retrieving_number()
            print('Enter second operand: ', end='')
            second_num = retrieving_number()
        # exiting menu
        if operator == 0:
            print('Thanks for using this calculator. Goodbye!')
            exit()
            midst_of_calculation = False
        # cases of mathematical calculations
        elif 1 <= operator and operator <= 6:
            execute_menu(operator, first_num, second_num)
        # display average menu selection
        elif operator == 7:
            # no calculations yet
            if number_of_calculations == 0:
                print('Error: No calculations yet to average!')
                need_to_display_menu = False
            # calculate average
            else:
                average_of_calculations = sum_of_calculations / number_of_calculations
                # print statistics
                print(f'Sum of calculations: {sum_of_calculations}')
                print(f'Number of calculations: {number_of_calculations}')
                print(f'Average of calculations: {average_of_calculations:.2f}')
                need_to_display_menu = False
        # invalid user input
        else:
            print('Error: Invalid selection!')
            need_to_display_menu = False
        sum_of_calculations += current_result


new_main()

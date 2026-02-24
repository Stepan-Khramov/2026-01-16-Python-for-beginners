#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Brief description of the script and its purpose.

This module does X and Y.

Example:
    $ python your_script_name.py
"""

import sys
# Import other standard library or third-party packages here

def main():
    """Main function of the script."""
    print("Script execution started.")
    
#=========================================================================================
# Homework code. Begin.
#=========================================================================================
    
    num_1 = float(input())
    num_2 = float(input())
    oper  = input()

    if num_2 == 0:
        print('Деление на 0!')
    elif oper not in ('+', '-', '/', '*', 'mod', 'pow', 'div'):
        print('Ошибка ввода')
    elif oper == '+':
        print(num_1 + num_2)
    elif oper == '-':
        print(num_1 - num_2)
    elif oper == '/':
        print(num_1 / num_2)
    elif oper == '*':
        print(num_1 * num_2)
    elif oper == 'mod':
        print(num_1 % num_2)
    elif oper == 'pow':
        print(num_1 ** num_2)
    elif oper == 'div':
        print(num_1 // num_2)
    
#=========================================================================================
# Homework code. End.
#=========================================================================================

    print("Script execution finished.")
    return 0

if __name__ == "__main__":
    # This block allows the script to be run directly from the command line
    # or imported as a module without executing the main function automatically.
    # sys.exit() is used to ensure the script exits with the status code
    # returned by the main function.
    sys.exit(main())
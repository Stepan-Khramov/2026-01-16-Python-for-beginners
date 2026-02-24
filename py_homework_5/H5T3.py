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
    
    qnt_row, qnt_col, el_row, el_col = list(map(int, input().split()))

    lst = []
    line = []
    if  (((el_row >= 0) & (el_row < qnt_row)) & ((el_col >= 0) & (el_col < qnt_col))) or\
        (((el_row >= 0) & (el_row < qnt_row)) & ((el_col < 0) & (abs(el_col) <= qnt_col))) or\
        (((el_row < 0) & (abs(el_row) <= qnt_row)) & ((el_col >= 0) & (el_col < qnt_col))) or\
        (((el_row < 0) & (abs(el_row) <= qnt_row)) & ((el_col < 0) & (abs(el_col) <= qnt_col))):
        for i in range(0,qnt_row):
            while len(line) != qnt_col:
                line = list(map(int, input().split()))
                if len(line) == qnt_col:
                    lst.append(line)
                else:
                    print('One more time.')
            line = []
        print(lst[el_row][el_col])
    else:
        print('Позиция выходит за пределы списка')




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
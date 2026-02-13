#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Brief description of the script and its purpose.

This module does X and Y.

Example:
    $ python your_script_name.py
"""

import sys
import datetime
# Import other standard library or third-party packages here

def main():
    """Main function of the script."""
    print("Script execution started.")
    
#=========================================================================================
# Homework code. Begin.
#=========================================================================================

    qnt_row, to_date = input().split(',')
    qnt_row= int(qnt_row)
    tmp1 = list(map(int, to_date.strip(' ').split('.')))
    to_date = datetime.date(*(list(map(int, to_date.strip(' ').split('.'))))[::-1])

    lst = []
    for row in range(qnt_row):
        lst.append(input().split(','))
        lst[row][1]= datetime.date(*(list(map(int, lst[row][1].strip(' ').split('.'))))[::-1])

    for row in lst:
        if to_date.year - row[1].year - ((to_date.month, to_date.day) < (row[1].month, row[1].day)) >= 18:
            print(f'{row[0].split()[0]} {row[0].split()[1][0]}.{row[0].split()[2][0]}. может участвовать в выборах')
        else:
            print(f'{row[0].split()[0]} {row[0].split()[1][0]}.{row[0].split()[2][0]}. НЕ может участвовать в выборах')
     


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
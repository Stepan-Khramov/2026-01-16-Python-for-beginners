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

    dob = datetime.date(*(list(map(int, input().split('.'))))[::-1])
    match dob.strftime('%A'):
        case 'Monday':
            print('Понедельник')
        case 'Tuesday':
            print('Вторник')
        case 'Wednesday':
            print('Среда')
        case 'Thursday':
            print('Четверг')
        case 'Friday':
            print('Пятница')
        case 'Saturday':
            print('Суббота')
        case 'Sunday':
            print('Воскресенье')

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
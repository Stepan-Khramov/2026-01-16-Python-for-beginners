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
#1 import locale
# Python 3.14 # from dateutil.relativedelta import relativedelta

# Import other standard library or third-party packages here

def main():
    """Main function of the script."""
    print("Script execution started.")
    
#=========================================================================================
# Homework code. Begin.
#=========================================================================================
    #1 locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8') 

    days_map = {
    "Monday": "понедельник",
    "Tuesday": "вторник",
    "Wednesday": "среда",
    "Thursday": "четверг",
    "Friday": "пятница",
    "Saturday": "суббота",
    "Sunday": "воскресенье"
     }

    bd = input()
    bd = datetime.datetime.strptime(bd, '%d.%m.%Y').date()
    some_date = input()
    some_date = datetime.datetime.strptime(some_date, '%d.%m.%Y').date()

    bd_week_day = days_map.get(bd.strftime('%A'))
    #2 match bd.strftime('%A'):
    #2     case 'Monday':
    #2         bd_week_day = 'понедельник'
    #2     case 'Tuesday':
    #2         bd_week_day = 'вторник'
    #2     case 'Wednesday':
    #2         bd_week_day = 'среда'
    #2     case 'Thursday':
    #2         bd_week_day = 'четверг'
    #2     case 'Friday':
    #2         bd_week_day = 'пятница'
    #2     case 'Saturday':
    #2         bd_week_day = 'суббота'
    #2     case 'Sunday':
    #2         bd_week_day = 'воскресенье'
    
    # Python 3.14 # age_years = relativedelta(some_date, bd).years
    age_years = some_date.year - bd.year
    if (some_date.month, some_date.day) < (bd.month, bd.day):
        age_years -= 1
    
    print(f'{age_years}\n{bd_week_day} ')


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
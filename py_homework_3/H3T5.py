#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Brief description of the script and its purpose.

This module does X and Y.

Example:
    $ python your_script_name.py
"""

import sys
import re
import datetime
# Import other standard library or third-party packages here

def main():
    """Main function of the script."""
    print("Script execution started.")
    
    # formated_dates = ''
    # txt = str(input())
    # found_dates = ' '.join(re.findall(r'\d{2}[/\-.]\d{2}[/\-.]\d{4}|\d{4}[/\-.]\d{2}[/\-.]\d{2}', txt))
    # if len(found_dates) == 0:
    #     print('В тексте дат нет')
    # else:
    #     tmp_formated_dates = re.sub(r'(\d{2,4})[/\-.](\d{2})[/\-.](\d{2,4})', r"\3.\2.\1", found_dates)
    #     formated_dates = (re.sub(r'(\d{4})\.(\d{2})\.(\d{2})', r"\3.\2.\1", tmp_formated_dates)).split()
    #     for row in formated_dates: 
    #         print(row)

    found_dates = []
    formated_dates = ''
    txt = str(input())
    found_dates_tmp = re.findall(r'((0[1-9]|[12][0-9]|3[01]|[12][0-9]{3})[/\-.](0[1-9]|1[0-2])[/\-.]([12][0-9]{3}|0[1-9]|[12][0-9]|3[01]))', txt)
    if len(found_dates_tmp) == 0:
        print('В тексте дат нет')
    else:
        for i in range(len(found_dates_tmp)):
            found_dates.append(found_dates_tmp[i][0]) 
        tmp_formated_dates = re.sub(r'(\d{2,4})[/\-.](\d{2})[/\-.](\d{2,4})', r"\3.\2.\1", ' '.join(found_dates))
        formated_dates = (re.sub(r'(\d{4})\.(\d{2})\.(\d{2})', r"\3.\2.\1", tmp_formated_dates)).split()
        for row in formated_dates: 
            print(row)


    print("Script execution finished.")
    return 0

if __name__ == "__main__":
    # This block allows the script to be run directly from the command line
    # or imported as a module without executing the main function automatically.
    # sys.exit() is used to ensure the script exits with the status code
    # returned by the main function.
    sys.exit(main())
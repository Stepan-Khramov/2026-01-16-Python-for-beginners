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
   
    num = int(input())

    summ = 0
    if num == 2:
        print(2)
    elif num > 2:
        for i in range(2,num+1):
            simple_num = True
            for j in range(2,i):
                if i % j == 0:
                    simple_num = False
                    break
            if simple_num:
                summ += i
        print(summ)
    else:
        print(0)

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
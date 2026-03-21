#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Brief description of the script and its purpose.

This module does X and Y.

Example:
    $ python your_script_name.py
"""

import sys
import string

# Import other standard library or third-party packages here

def main():
    """Main function of the script."""
    print("Script execution started.")
    
#=========================================================================================
# Homework code. Begin.
#=========================================================================================
    txt_res = ''
    txt_tmp = str(input())
    translator = str.maketrans('', '', string.punctuation)
    txt_tmp = txt_tmp.translate(translator).split()
    for el in txt_tmp:
        if el in txt_res:
            pass
        else:
            txt_res = txt_res + str(el) + ' '
    txt_res = txt_res[:-1]

    print (txt_res)


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
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
    
    txt_tmp = str(input())

    el_count = 1
    rslt = ''
    for i in range(0, len(txt_tmp)):
        if len(txt_tmp) == 1:
            rslt += txt_tmp[i] + str(el_count)
        elif ((i < (len(txt_tmp)-2)) and (txt_tmp[i] == txt_tmp[i+1])):
            el_count += 1
        elif ((i < (len(txt_tmp)-2))) and ((txt_tmp[i] != txt_tmp[i+1])):
            rslt += txt_tmp[i] + str(el_count)
            el_count = 1
        elif (i == (len(txt_tmp)-2)) and (txt_tmp[i] == txt_tmp[i+1]):
            rslt += txt_tmp[i] + str(el_count+1)
        elif (i == (len(txt_tmp)-2)) and (txt_tmp[i] != txt_tmp[i+1]):
            rslt += txt_tmp[i] + str(el_count)
            el_count = 1
            rslt += txt_tmp[i+1] + str(el_count)

    print(rslt)




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
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
    txt = []
    line = '@'
    while len(line) != 0:
        line = input()
        txt.append(line)
    name = str(input())
    txt = txt[:-1]

    for i in range(len(txt)-1,-1,-1):
        if f'@{name}' not in txt[i][0:len(name)+1]:
            del txt[i]
        else:
            txt[i] = txt[i][len(f'@{name}')+1:]
            txt[i] = txt[i].capitalize()
    
    txt.sort()
    for line in txt:
        print(line)

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
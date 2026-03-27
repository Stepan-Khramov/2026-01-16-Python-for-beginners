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

    matrix = []
    diag_summ = 0
    num = int(input())

    for i in range(0,num):
        tmp_ln = (str(input()).split(', '))
        tmp_ln[i], tmp_ln[0-i-1] = tmp_ln[0-i-1], tmp_ln[i]
        diag_summ += (int(tmp_ln[i]) + int(tmp_ln[0-i-1]))
        matrix.append(tmp_ln)

    for line in matrix:
        print(' '.join(line))
    print(diag_summ)

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
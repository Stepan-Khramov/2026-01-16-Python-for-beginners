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

    mtx_size = int(input())
    direction = str(input())
    mtx = [[None] * mtx_size for i in range(mtx_size)]
    row = 0
    col = 0
    row_inc = 1
    col_inc = 0
    for i in range(1, mtx_size**2+1):
        mtx[row][col] = i
        next_row = row + row_inc
        next_col = col + col_inc
        if (mtx_size > next_row >= 0) and (mtx_size > next_col >= 0) and (mtx[next_row][next_col] is None):
            row = next_row
            col = next_col
        else:
            row_inc, col_inc = -col_inc, row_inc
            row, col = row + row_inc,  col + col_inc
    if direction == 'clockwise':
        mtx = list(zip(*mtx))
    for line in mtx:
        print('\t'.join(map(str, line)))


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
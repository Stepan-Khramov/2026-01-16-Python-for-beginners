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

    pos1 = str(input())
    pos2 = str(input())
    col1, row1 = ord(pos1[0]) - ord('a') + 1, int(pos1[1])
    col2, row2 = ord(pos2[0]) - ord('a') + 1, int(pos2[1])

    d_col = abs(col1 - col2)
    d_row = abs(row1 - row2)

    print((d_col == 1 and d_row == 2) or (d_col == 2 and d_row == 1))




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
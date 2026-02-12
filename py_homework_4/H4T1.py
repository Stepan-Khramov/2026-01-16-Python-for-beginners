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

#=========================================================================================
# Homework code. Begin.
#=========================================================================================

# ===== Var 1=====
# sys.setrecursionlimit(2000) 
# ===== Var 1=====

def sqr_num(def_num, def_sqr):
# ===== Var 1=====
#     if def_sqr == 1:
#         print (def_result)
#         return True
#     elif def_sqr == 0:
#         print (1)
#         return True
#     if def_num == 0:
#         print (0)
#         return True
#     def_result = def_result * def_num
#     return sqr_num(def_num, def_sqr-1, def_result)
# ===== Var 1=====
    print (def_num**def_sqr)
    return True

# ===========================================
def main():
    """Main function of the script."""
    print("Script execution started.")
# ===========================================


    lst = []
    line = []
    pair_qnt = int(input())
    for i in range(0,pair_qnt):
        while len(line) != 2:
            line = list(map(int, input().split()))
            if len(line) == 2:
                lst.append(line)
            else:
                print('Try one more time.')
        line = []

    for row in lst:
# ===== Var 1=====
    #     sqr_num(row[0], row[1], row[0])
# ===== Var 1=====
        sqr_num(row[0], row[1])


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
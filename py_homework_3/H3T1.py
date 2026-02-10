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
    
    # lst = list(map(int, input().split()))
    # indx_min = lst.index(min(lst))
    # indx_max = lst.index(max(lst))
    # if indx_min < indx_max:
    #     sum1 = sum(lst[lst.index(min(lst))+1:lst.index(max(lst))])
    # else:
    #     sum1 = sum(lst[lst.index(max(lst))+1:lst.index(min(lst))])
    # print(sum1)

    lst = []
    line = []
    col_sum_lst = []
    qnt_row, qnt_col = list(map(int, input().split()))
    for i in range(0,qnt_row):
        while len(line) != qnt_col:
            line = list(map(int, input().split()))
            if len(line) == qnt_col:
                lst.append(line)
            else:
                print('One more time.')
        line = []
    col_sum_lst = [0]*qnt_col

    for row in lst:
        for i in range(0,qnt_col):
            col_sum_lst[i] += row[i]

    print(str(col_sum_lst).strip('[]').replace(',',''))
                
    print("Script execution finished.")
    return 0

if __name__ == "__main__":
    # This block allows the script to be run directly from the command line
    # or imported as a module without executing the main function automatically.
    # sys.exit() is used to ensure the script exits with the status code
    # returned by the main function.
    sys.exit(main())
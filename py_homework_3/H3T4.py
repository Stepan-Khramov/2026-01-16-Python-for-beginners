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
    
    # lst = list(map(int, input().split()))
    # indx_min = lst.index(min(lst))
    # indx_max = lst.index(max(lst))
    # if indx_min < indx_max:
    #     sum1 = sum(lst[lst.index(min(lst))+1:lst.index(max(lst))])
    # else:
    #     sum1 = sum(lst[lst.index(max(lst))+1:lst.index(min(lst))])
    # print(sum1)

    pxl_lines = [0]
    pxl_line = ''
    pxl_lst = []
    pxl_dict = dict()
    line = ''
    qnt_row = int(input())
    pxl_lines[0] = (input())
    pxl_line += pxl_lines[0]
    line_lenth = len(pxl_lines[0].split())
    for i in range(1,qnt_row):
        while len(line.split()) != line_lenth:
            line = str(input())
            if len(line.split()) == line_lenth:
                pxl_lines.append(line)
                pxl_line += ('\t' + line)
            else:
                print('One more time.')
        line = ''

    # for line in pxl_lines:
    #     pxl_lst.append(line.split('\t'))
    pxl_lst = pxl_line.split('\t')

    for pixel in pxl_lst:
        if pixel not in pxl_dict:
            pxl_dict[pixel] = 1
        else: 
            pxl_dict[pixel] += 1

    for key, value in pxl_dict.items():
        if value == max(pxl_dict.values()):
            print(key)
    

    print("Script execution finished.")
    return 0

if __name__ == "__main__":
    # This block allows the script to be run directly from the command line
    # or imported as a module without executing the main function automatically.
    # sys.exit() is used to ensure the script exits with the status code
    # returned by the main function.
    sys.exit(main())
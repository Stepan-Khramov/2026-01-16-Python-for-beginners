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

    text = str(input())
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    wrd_lst = text.lower().replace(',', '').replace('.', '').split()
    qnt_lst = [0]*len(wrd_lst)

    for i in range(0, len(wrd_lst)):
        qnt_lst[i] = wrd_lst.count(wrd_lst[i])

    print( f"{wrd_lst[qnt_lst.index(max(qnt_lst))]}, {max(qnt_lst)}")
                
    print("Script execution finished.")
    return 0

if __name__ == "__main__":
    # This block allows the script to be run directly from the command line
    # or imported as a module without executing the main function automatically.
    # sys.exit() is used to ensure the script exits with the status code
    # returned by the main function.
    sys.exit(main())
#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Brief description of the script and its purpose.

This module does X and Y.

Example:
    $ python your_script_name.py
"""

import sys
import random
import string

# Import other standard library or third-party packages here

def main():
    """Main function of the script."""
    print("Script execution started.")
    
#=========================================================================================
# Homework code. Begin.
#=========================================================================================
    pwd = []
    len = int(input())
    seed = int(input())

    random.seed(seed)

    chars = string.ascii_letters + string.digits

    pwd = ''.join(random.choice(chars) for i in range(len))

    # for i in range(len):
    #     pwd.append(random.choice(chars))
    # pwd = ''.join(pwd)

    print(pwd)


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
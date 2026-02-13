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
# Import other standard library or third-party packages here

def main():
    """Main function of the script."""
    print("Script execution started.")
    
#=========================================================================================
# Homework code. Begin.
#=========================================================================================

    qnt_row, qnt_col, rnd_init, rnd_rng_min, rnd_rng_max = list(map(int, input().split()))

    lst = []
    random.seed(rnd_init)
    for row in range(qnt_row):
        row = []
        sum = 0
        for col in range(qnt_col):
            sum += (random.randint(rnd_rng_min, rnd_rng_max))
        print(sum)
        

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
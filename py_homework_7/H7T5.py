#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Brief description of the script and its purpose.

This module does X and Y.

Example:
    $ python your_script_name.py
"""

import sys
import pandas as pd
import os
# Import other standard library or third-party packages here

def main():
    """Main function of the script."""
    print("Script execution started.")
    
#=========================================================================================
# Homework code. Begin.
#=========================================================================================

    df = pd.read_csv('athlete_events.csv')
    
    sports_1992 = df[(df.Year == 1992)]['Sport'].unique().tolist()
    sports_2016 = df[(df.Year == 2016)]['Sport'].unique().tolist()

    result = sorted(list(set(sports_1992) - set(sports_2016)))
    
    for line in result:
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
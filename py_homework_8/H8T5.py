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
import pandas as pd


def main():
    """Main function of the script."""
    print("Script execution started.")
    
#=========================================================================================
# Homework code. Begin.
#=========================================================================================

    df = pd.read_csv('athlete_events.csv')

    min_weight_champ = int(df[(df.Medal == 'Gold') & (df.Sex == 'M')]['Weight'].dropna(how = 'any').unique().min())
    sport = str(df[(df.Medal == 'Gold') & (df.Sex == 'M') & (df.Weight == min_weight_champ)]['Sport'].unique()).strip("'[]")

    print(sport)

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
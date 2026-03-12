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

    max_sport_types = df.groupby(['City', 'Year', 'Games']).agg({'Sport': 'nunique'}).max()
    sport_types_game_list = df.groupby(['City', 'Year', 'Games']).agg({'Sport': 'nunique'}).sort_values(['Sport', 'Games'])
    result = sport_types_game_list[sport_types_game_list.Sport == int(max_sport_types.iloc[0])].iloc[0].name[0]
    print(result)

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
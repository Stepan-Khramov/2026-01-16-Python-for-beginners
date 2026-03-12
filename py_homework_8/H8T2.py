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

    max_height = max(df[(df.Season == 'Winter') & (df.Sex == 'M')].Height)
    max_year = max(df[(df.Season == 'Winter') & (df.Sex == 'M') & (df.Height == (max_height))].Year)
    tall_man = df[(df.Season == 'Winter') & (df.Sex == 'M') & (df.Height == (max_height))].head(1)
    print(f'Рост: {str(tall_man['Height'].tolist()).strip('[]')}, Год: {str(tall_man['Year'].tolist()).strip('[]')}, Имя: {str(tall_man['Name'].tolist()).strip("[]'")}')
    
    low_height = min(df[(df.Season == 'Winter') & (df.Sex == 'M')].Height)
    max_year = max(df[(df.Season == 'Winter') & (df.Sex == 'M') & (df.Height == (low_height))].Year)
    short_man = df[(df.Season == 'Winter') & (df.Sex == 'M') & (df.Height == (low_height)) & (df.Year == (max_year))].head(1)
    print(f'Рост: {str(short_man['Height'].tolist()).strip('[]')}, Год: {str(short_man['Year'].tolist()).strip('[]')}, Имя: {str(short_man['Name'].tolist()).strip("[]'")}')
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
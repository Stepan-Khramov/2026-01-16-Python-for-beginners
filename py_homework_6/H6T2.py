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
# Import other standard library or third-party packages here

def main():
    """Main function of the script."""
    print("Script execution started.")
    
#=========================================================================================
# Homework code. Begin.
#=========================================================================================

    df = pd.read_csv('athlete_events.csv')

    # print(df.head)

    # Олимпийские игры 1994 года, пол мужской
    print(df[(df.Year == 1994) & (df.Sex == 'M')]['Age'].min())
    # 15

    # Олимпийские игры 1992 года, пол мужской
    print(df[(df.Year == 1992) & (df.Sex == 'M')]['Age'].min())
    # 11

    # Олимпийские игры 1996 года, пол женский
    print(df[(df.Year == 1996) & (df.Sex == 'F')]['Age'].min())
    # 12

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
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

    # Найдите самую тяжелую (по весу) спортсменку игр 2008 года. 
    # В каком виде спорта она участвовала (столбец Event)?
    # Скопируйте в ответ название
    res = df[(df.Year == 2008) & (df.Sex == 'F')].sort_values(by='Weight', ascending=False)['Event'].head(1)
    print(res)
    # Weightlifting Women's Super-Heavyweight

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
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

    # Найдите среднее арифметическое для роста девушек баскетболисток 
    # (название соревнования должно начинаться со слова «Basketball»),
    # которые участвовали в играх 1988 года. Округлите ответ до двух знаков после точки.

    count = 0
    event_1 = round(df[(df.Year == 1988) & (df.Sex == 'F') & df.Event.str.startswith('Basketball')]['Height'].mean(), 2)
    print(event_1)


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
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

    # Какую долю составляют (не в процентах) соревнования по мужской спортивной гимнастике среди всех участников игр 1904 года?
    # Округлите ответ до двух знаков после точки
    # Подсказка: вам необходимы соревнования «Gymnastics Men's Individual All-Around, Apparatus Work»
    # res = df[(df.Year == 1904) & (df.Event == "Gymnastics Men's Individual All-Around, Apparatus Work")]["ID"].value_counts()
    event_1 = df[(df.Year == 1904)]["Event"].value_counts()["Gymnastics Men's Individual All-Around, Apparatus Work"]
    print(event_1)
    all_events = df['Year'].value_counts()[1904]
    print(all_events)
    res = event_1 / all_events
    print(round(res, 2))
    # 0.09


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
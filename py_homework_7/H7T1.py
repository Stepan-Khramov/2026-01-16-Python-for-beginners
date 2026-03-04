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
    # print(f'Загружено {df.shape[0]} строк и {df.shape[1]} столбцов.')
    # print(df.head)
    
        # 'Name': ['Aleksey Yuryevich Nemov', 'Aleksey Petrovich Bondarenko', 'Darya Vitalyevna Pishchalnikova'],
        # 'Events amount': [(df['Name'] == 'Aleksey Yuryevich Nemov').sum(), (df['Name'] == 'Aleksey Petrovich Bondarenko').sum(), (df['Name'] == 'Darya Vitalyevna Pishchalnikova').sum()],
    var_1 = len(df[df.Name == 'Aleksey Yuryevich Nemov']['Games'].unique())
    var_2 = len(df[df.Name == 'Aleksey Petrovich Bondarenko']['Games'].unique())
    var_3 = len(df[df.Name == 'Darya Vitalyevna Pishchalnikova']['Games'].unique())
# var_1 = var_1['Games'].unique()

    print(f'Aleksey Yuryevich Nemov - {var_1}')
    print(f'Aleksey Petrovich Bondarenko - {var_2}')
    print(f'Darya Vitalyevna Pishchalnikova - {var_3}')
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
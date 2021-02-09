#!/usr/bin/env python3

# https://github.com/drebrb/masstouch

import os
from tqdm import trange
import touch
from datetime import datetime
import calendar
import numpy as np

def run():
    if os.name == 'nt':
        import winshell
        os.chdir(winshell.desktop()) 

    file_name = input("File name: ")
    file_type = input("Save as type: ")

    response = input("Save to " + "'" + os.getcwd() + "'" + "? [Y/n]: ")

    if response in('n', 'N', 'no', 'No', 'NO', 'nO'):
        save_path = input("Save to: ")
        os.chdir(save_path)

    while True:
        print()
        print("Create files in one of the following ways..")
        print()
        print("          *********************************************** ")
        print("Options: | Numerical(n) | Alphabetical(a) | Date(d)      |")
        print("         | ------------ | --------------- | ------------ |")
        print("E.g.     | (0 - 'inf')  | (A - Z)         | (YYYY-MM-DD) |")
        print("         |                                               |")
        print("          *********************************************** ")
        print()
        option = input("Enter option: ")

        if option in('n', 'N', 'Numerical', 'numerical'):
            start = int(input("Start with: "))
            end = int(input("End with: "))

            for i in trange(start, end + 1):
                touch.touch(file_name + "(" + str(i) + ")" + "." + file_type)
            break
 
        if option in('a', 'A', 'Alphabetical', 'alphabetical'):
            start = input("Start with: ")
            end = input("End with: ")

            for i in trange(ord(start), ord(end) + 1):
                touch.touch(file_name + "(" + chr(i) + ")" + "." + file_type)
            break

        if option in('d', 'D', 'Date', 'date'):
            year = datetime.now().year

            print()
            print("************************************************************************")
            print(calendar.calendar(year))
            print("************************************************************************")
            print()

            start = np.datetime64(input("Start with: "))
            end = np.datetime64(input("End with: "))
 
            print()
            print("                *********************************************************** ")
            print("               |          All Days           |         Mon, Wed, Fri       |")
            print("               | --------------------------- | --------------------------- |")
            print("Choose Day(s): | M | T | W | Th | F | Sa | S | M | T | W | Th | F | Sa | S |")
            print("               | --------------------------- | --------------------------- |")
            print("E.g.           | 1 | 1 | 1 | 1  | 1 | 1  | 1 | 1 | 0 | 1 | 0  | 1 | 0  | 0 |")
            print("               |                                                           |")
            print("                *********************************************************** ")
            print()
            mask = input("..: ")
 
            first_day = np.busday_offset(start, 0, roll='forward', weekmask=mask)
            last_day = np.busday_offset(end, 0, roll='preceding', weekmask=mask)
            count = np.busday_count(first_day, last_day, weekmask=mask)
 
            for i in trange(count + 1):
                touch.touch(file_name + str(first_day) + "." + file_type)
                first_day += np.timedelta64(7, 'D')
            break

        else:
            print(option, "is not a valid option")

    while True:
        response = input("Create more files? [Y/n]: ")
 
        if response in('n', 'N', 'No', 'no', 'NO', 'nO'):
            exit(0)
        else:
            run()

if __name__ == '__main__':
    run()

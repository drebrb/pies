#!/usr/bin/env python3

# https://github.com/drebrb/masstouch

import os
from tqdm import trange
import touch
import calendar
from datetime import datetime
import numpy as np

if os.name == 'nt':
    import winshell
    os.chdir(winshell.desktop())

def run():
    file_name = input("File name: ")
    file_type = input("Save as type: ")

    while True:
        response = input("Save to " + "'" + os.getcwd() + "'" + "? [Y/n]: ")

        if response in('', 'y', 'Y', 'yes', 'Yes', 'YES', 'YEs', 'YeS', 'yES', 'yeS', 'yEs'):
            break

        if response in('n', 'N', 'no', 'No', 'NO', 'nO'):
            save_path = input("Save to: ")
            os.chdir(save_path)
            break

    print()
    print("Create files in one of the following ways..")
    print()
    print("          *********************************************** ")
    print("Options: | Numerical(n) | Alphabetical(a) | Date(d)      |")
    print("         | ------------ | --------------- | ------------ |")
    print("E.g.     | (*int, *int) | (A, Z)          | (YYYY-MM-DD) |")
    print("         |                                               |")
    print("          *********************************************** ")
    print()

    while True:
        option = input("Enter option: ")

        if option in('n', 'N', 'Numerical', 'numerical'):
            start = int(input("Start with: "))
            end = int(input("End with: "))

            for i in trange(start, end + 1):
                touch.touch(file_name + " " + "(" + str(i) + ")" + "." + file_type)

            break
 
        if option in('a', 'A', 'Alphabetical', 'alphabetical'):
            start = input("Start with: ")
            end = input("End with: ")

            for i in trange(ord(start), ord(end) + 1):
                touch.touch(file_name + " " + "(" + chr(i) + ")" + "." + file_type)
 
            break

        if option in('d', 'D', 'Date', 'date'):
            print()
            print("************************************************************************")
            print(calendar.calendar(datetime.now().year))
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

            day = input("..: ")
 
            first_day = np.busday_offset(start, 0, roll='forward', weekmask=day)
            last_day = np.busday_offset(end, 0, roll='preceding', weekmask=day)
            count = np.busday_count(first_day, last_day, weekmask=day)
 
            for i in trange(count + 1):
                touch.touch(file_name + " " + str(first_day) + "." + file_type)
                first_day += np.timedelta64(7, 'D')
 
            break

    while True:
        response = input("Create more files? [Y/n]: ")

        if response in('', 'y', 'Y', 'yes', 'Yes', 'YES', 'YEs', 'YeS', 'yES', 'yeS', 'yEs'):
            run()

        if response in('n', 'N', 'No', 'no', 'NO', 'nO'):
            exit(0)

if __name__ == '__main__':
    run()

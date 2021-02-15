#!/usr/bin/env python3

# https://github.com/drebrb/masstouch

import os
from tqdm import trange, tqdm
import touch
from datetime import datetime
import calendar
import numpy as np

if os.name == 'nt':
    import winshell
    os.chdir(winshell.desktop())

print("Report bugs to 'https://github.com/drebrb/masstouch'")

def run():
    file_name = input("\nFile name: ")
    
    print("""
+---------+----------+---------------+
| Word(1) | Excel(2) | PowerPoint(3) |
+---------+----------+---------------+ 
| Text(4) | HTML(5)  | Markdown(6)   |
+---------+----------+---------------+
""")

    while True:
        choice = input("Save as type: ")

        if choice == "1":
            file_type = "docx"
            break

        if choice == "2":
            file_type = "xlsx"
            break

        if choice == "3":
            file_type = "pptx"
            break

        if choice == "4":
            file_type = "txt"
            break

        if choice == "5":
            file_type = "html"
            break

        if choice == "6":
            file_type = "md"
            break

    while True:
        response = input("\nSave to " + "'" + os.getcwd() + "'" + "? [Y/n]: ")

        if response in('', 'y', 'Y', 'yes', 'Yes', 'YES', 'YEs', 'YeS', 'yES', 'yeS', 'yEs'):
            break

        if response in('n', 'N', 'no', 'No', 'NO', 'nO'):
            save_path = input("\nSave to: ")
            os.chdir(save_path)
            break

    print("""
Create files in one of the following ways..

+--------------+-----------------+--------------+
| Numerical(n) | Alphabetical(a) | Date(d)      |
+--------------+-----------------+--------------+
| (*int, *int) | (A, Z)          | (YYYY-MM-DD) |
+--------------+-----------------+--------------+
""")

    while True:
        option = input("Enter option: ")

        if option in('n', 'N', 'Numerical', 'numerical'):
            start, end = map(int, input("\nEnter first and last #: ").split())
            print()

            for i in trange(start, end + 1, colour='green'):
                touch.touch(file_name + "_V" + str(i).zfill(2) + "." + file_type)

            break
 
        if option in('a', 'A', 'Alphabetical', 'alphabetical'):
            start, end = map(ord, input("\nEnter First and last letter: ").split())
            print()

            for i in trange(start, end + 1, colour='green'):
                touch.touch(file_name + "_" + chr(i) + "." + file_type)
 
            break

        if option in('d', 'D', 'Date', 'date'):
            print("""
************************************************************************
""")
            print(calendar.calendar(datetime.now().year))
            print("""
************************************************************************""")

            print("""
+-----------------------+
| Start      End        |
+-----------+-----------+
| YYYY-MM-DD YYYY-MM-DD |
+-----------+-----------+
""")

            start, end = map(np.datetime64, input("Enter dates: ").split())

            print("""
+---------+----------------------+
| Days    | Mo Tu We Th Fr Sa Su |
| On  = 1 |  1  1  1  1  1  1  1 |
| Off = 0 |  0  0  0  0  0  0  0 |
+---------+----------------------+
""")

            days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
            input_days = [x[0] for x in filter(lambda d: d[1] != 0, zip(days, (int(val) for val in input("Enter days : ").split())))]

            print()

            for day in tqdm((input_days), position=0, colour='green'):
                first = np.busday_offset(start, 0, roll='forward', weekmask=day)
                last = np.busday_offset(end, 1, roll='preceding', weekmask=day)
                delta = np.timedelta64(7, 'D')
                arange = np.arange(first, last, delta)
                array = np.array(arange)
 
                for a in tqdm(array, position=2, leave=False, desc=day, colour='blue'):
                    touch.touch(str(a) + "_" + file_name + "." + file_type)

            break

    while True:
        response = input("\nCreate more files? [Y/n]: ")

        if response in('', 'y', 'Y', 'yes', 'Yes', 'YES', 'YEs', 'YeS', 'yES', 'yeS', 'yEs'):
            run()

        if response in('n', 'N', 'No', 'no', 'NO', 'nO'):
            exit(0)

if __name__ == '__main__':
    run()

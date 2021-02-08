#!/usr/bin/env python3

# https://github.com/drebrb/masstouch

import os
import touch
from tqdm import trange
from datetime import datetime
import calendar
import numpy as np

class masstouch():
    def create_files():
        file_name = input("File name: ")
        file_type = input("Save as type: ")
        cwd = os.getcwd()
        print("Save to...?")
        print("'" + cwd + "'", end= " ")
        response = input("[Y/n]: ")
        if response in('n', 'N', 'no', 'No', 'NO', 'nO'):
            location = input("Save to: ")
            os.chdir(location)
        while True:
            sort_type = input("Sort by.. Numerical(n), Alphabetical(a), Date(d)..: ")
            if sort_type in('n', 'N'):
                start_num = int(input("Start #: "))
                end_num = int(input("End #: "))
                a = start_num
                b = end_num + 1
                if end_num <= 0:
                    exit(1)
                elif end_num == 1:
                    touch.touch(file_name + "." + file_type)
                    break
                for i in trange(a, b):
                    touch.touch(file_name + " " + "(" + str(i) + ")" + "." + file_type)
                break
            elif sort_type in('a', 'A'):
                start_let = input("Start letter: ")
                end_let = input("End letter: ")
                a = ord(start_let)
                b = ord(end_let) + 1
                for i in trange(a, b):
                    touch.touch(file_name + " " + "(" + chr(i) + ")" + "." + file_type)
                break
            elif sort_type in('d', 'D'):
                year = datetime.now().year

                print("*************************************************************************")
                print(calendar.calendar(year))
                print("*************************************************************************")

                start = np.datetime64(input("Start date(YYYY-MM-DD): "))
                end = np.datetime64(input("End   date(YYYY-MM-DD): "))
                day = input("Days  Su|M|T|W|Th|F|Sa: ") 

                def monday():
                    first_monday = np.busday_offset(start, 0, roll='forward', weekmask='Mon')
                    last_monday = np.busday_offset(end, 0, roll='forward', weekmask='Mon')
                    delta = np.busday_count(first_monday, last_monday, weekmask='Mon') 

                    for i in trange(delta):
                        touch.touch(file_name + " " + str(first_monday) + "." + file_type)
                        first_monday += np.timedelta64(7, 'D')

                if day in('m', 'M', 'Mon', 'mon', 'monday', 'Monday'):
                    monday()
                break
            else:
                print("'" + sort_type + "'", "is not a valid option.")
        while True:
            response = input("Create more files? [Y/n]: ")
            if response in('n', 'N', 'no', 'No', 'NO', 'nO'):
                exit(0)
            else:
                masstouch.create_files()

if __name__ == '__main__':
    masstouch.create_files()

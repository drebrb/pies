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
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    file_name = input("File name: ")
    
    print()
    print("               ************************************ ")
    print("File types:   | Word(1) | Excel(2) | PowerPoint(3) |")
    print("              | ---------------------------------- |") 
    print("              | Text(4) | HTML(5)  | Markdown(6)   |")
    print("              |                                    |")
    print("               ************************************ ")
    print()

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
        
    print()

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
    print("               *********************************************** ")
    print("Options:      | Numerical(n) | Alphabetical(a) | Date(d)      |")
    print("              | ------------ | --------------- | ------------ |")
    print("E.g.          | (*int, *int) | (A, Z)          | (YYYY-MM-DD) |")
    print("              |                                               |")
    print("               *********************************************** ")
    print()

    while True:
        option = input("Enter option: ")

        if option in('n', 'N', 'Numerical', 'numerical'):
            print()
            start = int(input("Start with: "))
            end = int(input("End with  : "))
            print()

            for i in trange(start, end + 1):
                touch.touch(file_name + " " + "(" + str(i) + ")" + "." + file_type)

            print()

            break
 
        if option in('a', 'A', 'Alphabetical', 'alphabetical'):
            print()
            start = input("Start with: ")
            end = input("End with  : ")
            print()

            for i in trange(ord(start), ord(end) + 1):
                touch.touch(file_name + " " + "(" + chr(i) + ")" + "." + file_type)
 
            print()

            break

        if option in('d', 'D', 'Date', 'date'):
            print()
            print("************************************************************************")
            print(calendar.calendar(datetime.now().year))
            print("************************************************************************")
            print()

            start = np.datetime64(input("Start with: "))
            end = np.datetime64(input("End with  : "))
 
            print()
            print("                *************************** ")
            print("Choose Day(s)  |          All Days         |")
            print("               | ------------------------- |")
            print("E.g.           | S | M | T | W | T | F | S |")
            print("               | ------------------------- |")
            print("(1=On, 0=Off)  | 1 | 1 | 1 | 1 | 1 | 1 | 1 |")
            print("               |                           |")
            print("                *************************** ")
            print("S M T W T F S")

            sun, mon, tue, wed, thu, fri, sat = map(int, input().split())
            
            print()    

            if sun == 1:
                first_sunday = np.busday_offset(start, 0, roll='forward', weekmask='Sun')
                last_sunday = np.busday_offset(end, 0, roll='preceding', weekmask='Sun')
                sun_count = np.busday_count(first_sunday, last_sunday, weekmask='Sun') + 1
                
                for i in trange(sun_count, desc="Sunday"):
                    touch.touch(file_name + " " + datetime.strptime(str(first_sunday), '%Y-%m-%d').strftime('%m-%d-%Y') + "." + file_type)
                    first_sunday += np.timedelta64(7, 'D')
 
            if mon == 1:
                first_monday = np.busday_offset(start, 0, roll='forward', weekmask='Mon')
                last_monday = np.busday_offset(end, 0, roll='preceding', weekmask='Mon')
                mon_count = np.busday_count(first_monday, last_monday, weekmask='Mon') + 1
                
                for i in trange(mon_count, desc="Monday"):
                    touch.touch(file_name + " " + datetime.strptime(str(first_monday), '%Y-%m-%d').strftime('%m-%d-%Y') + "." + file_type)
                    first_monday += np.timedelta64(7, 'D')
 
            if tue == 1:
                first_tuesday = np.busday_offset(start, 0, roll='forward', weekmask='Tue')
                last_tuesday = np.busday_offset(end, 0, roll='preceding', weekmask='Tue')
                tue_count = np.busday_count(first_tuesday, last_tuesday, weekmask='Tue') + 1
                
                for i in trange(tue_count, desc="Tuesday"):
                    touch.touch(file_name + " " + datetime.strptime(str(first_tuesday), '%Y-%m-%d').strftime('%m-%d-%Y') + "." + file_type)
                    first_tuesday += np.timedelta64(7, 'D')
 
            if wed == 1:
                first_wednesday = np.busday_offset(start, 0, roll='forward', weekmask='Wed')
                last_wednesday = np.busday_offset(end, 0, roll='preceding', weekmask='Wed')
                wed_count = np.busday_count(first_wednesday, last_wednesday, weekmask='Wed') + 1
                
                for i in trange(wed_count, desc="Wednesday"):
                    touch.touch(file_name + " " + datetime.strptime(str(first_wednesday), '%Y-%m-%d').strftime('%m-%d-%Y') + "." + file_type)
                    first_wednesday += np.timedelta64(7, 'D')
 
            if thu == 1:
                first_thursday = np.busday_offset(start, 0, roll='forward', weekmask='Thu')
                last_thursday = np.busday_offset(end, 0, roll='preceding', weekmask='Thu')
                thu_count = np.busday_count(first_thursday, last_thursday, weekmask='Thu') + 1
                
                for i in trange(thu_count, desc="Thursday"):
                    touch.touch(file_name + " " + datetime.strptime(str(first_thursday), '%Y-%m-%d').strftime('%m-%d-%Y') + "." + file_type)
                    first_thursday += np.timedelta64(7, 'D')
 
            if fri == 1:
                first_friday = np.busday_offset(start, 0, roll='forward', weekmask='Fri')
                last_friday = np.busday_offset(end, 0, roll='preceding', weekmask='Fri')
                fri_count = np.busday_count(first_friday, last_friday, weekmask='Fri') + 1
                
                for i in trange(fri_count, desc="Friday"):
                    touch.touch(file_name + " " + datetime.strptime(str(first_friday), '%Y-%m-%d').strftime('%m-%d-%Y') + "." + file_type)
                    first_friday += np.timedelta64(7, 'D')
 
            if sat == 1:
                first_saturday = np.busday_offset(start, 0, roll='forward', weekmask='Sat')
                last_saturday = np.busday_offset(end, 0, roll='preceding', weekmask='Sat')
                sat_count = np.busday_count(first_saturday, last_saturday, weekmask='Sat') + 1
                
                for i in trange(sat_count, desc="Saturday"):
                    touch.touch(file_name + " " + datetime.strptime(str(first_saturday), '%Y-%m-%d').strftime('%m-%d-%Y') + "." + file_type)
                    first_saturday += np.timedelta64(7, 'D')
            
            print()
            
            break

    while True:
        response = input("Create more files? [Y/n]: ")

        if response in('', 'y', 'Y', 'yes', 'Yes', 'YES', 'YEs', 'YeS', 'yES', 'yeS', 'yEs'):
            run()

        if response in('n', 'N', 'No', 'no', 'NO', 'nO'):
            exit(0)

if __name__ == '__main__':
    run()

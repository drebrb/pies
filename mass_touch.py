#!/usr/bin/env python3

# https://github.com/drebrb/masstouch

import os
import touch
from tqdm import trange

def create_files():
    file_name = input("File name: ")
    extension = input("Save as type: ")
    quantity = int(input("Number of copies: "))
    if quantity <= 0:
        exit(1)
    a = 1
    b = quantity + 1

    cwd = os.getcwd()
    print("Save to..?")
    print("'" + cwd + "'", end= " ")
    response = input("[Y/n]: ")
    if response in('n', 'N', 'no', 'No', 'NO', 'nO'):
        location = input("Save to: ")
        os.chdir(location)

    if quantity == 1:
        touch.touch(file_name + "." + extension)
        exit(0)
    elif quantity < 10:
        fill = 1
    elif quantity >= 10 and quantity < 100:
        fill = 2
    elif quantity >= 100 and quantity < 1000:
        fill = 3
    elif quantity >= 1000 and quantity < 10000:
        fill = 4
    elif quantity >= 10000 and quantity < 100000:
        fill = 5
    elif quantity >= 100000:
        fill = 6
    else:
        fill = 1

    for i in trange(a, b):
        touch.touch(file_name + str(i).zfill(fill) + "." + extension)

if __name__ == '__main__':
    create_files()
    

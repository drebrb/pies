#!/usr/bin/env python3

import touch

def create_files():
    file_name = input("File name: ")
    extension = input("Save as type: ")
    quantity = int(input("Number of copies: "))
    a = 1
    b = quantity + 1

    if quantity < 10:
        fill = 1
    elif quantity < 100:
        fill = 2
    elif quantity >= 100:
        fill = 3

    for i in range(a, b):
        touch.touch(file_name + str(i).zfill(fill) + "." + extension)

if __name__ == '__main__':
    create_files()
    

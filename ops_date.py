#!/usr/bin/env python3

from datetime import datetime
import calendar
import numpy as np
from tqdm import tqdm
import touch

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

day_input = (int(val) for val in input("Enter days : ").split())
NAMES = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

print()

for val, name in tqdm(zip(day_input, NAMES), position=2, colour='green', total=len(NAMES)):
    if not val:
        continue
    first = np.busday_offset(start, 0, roll='forward', weekmask=name)
    last = np.busday_offset(end, 1, roll='preceding', weekmask=name)
    delta = np.timedelta64(7, 'D')
    arange = np.arange(first, last, delta)
    array = np.array(arange)
    
    for a in tqdm((array), position=0, leave=False, desc=name, colour='blue'):
        pass

print()

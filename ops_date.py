#!/usr/bin/env python3

import numpy as np
from tqdm import tqdm

print("""
+---------+----------------------+
| Days    | Mo Tu We Th Fr Sa Su |
| On  = 1 |  1  1  1  1  1  1  1 |
| Off = 0 |  0  0  0  0  0  0  0 |
+---------+----------------------+
""")

day_input = (int(val) for val in input("Enter days : ").split())
days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

print()

for val, day in tqdm(zip(day_input, days), position=2, colour='green', total=len(days)):
    if not val:
        continue
    first = np.busday_offset(np.datetime64('2022-01-01'), 0, roll='forward', weekmask=day)
    last = np.busday_offset(np.datetime64('1002022-01-01'), 1, roll='preceding', weekmask=day)
    delta = np.timedelta64(7, 'D')
    arange = np.arange(first, last, delta)
    array = np.array(arange)

    for a in tqdm(array, position=0, leave=False, desc=day, colour='blue'):
        pass

#!/usr/bin/python

import sys

current_time = sys.argv[1] 

for l in sys.stdin:
    data = l.split()
    mm, hh, task = data[0], data[1], data[2]

    hh_stdin, mm_stdin = (int(n) for n in current_time.split(':'))
    if mm == '*' and hh == '*':
        print(f'{current_time} today - {task}')
        continue
    
    if hh != '*':
        hh_task = int(hh)
        if hh_task < hh_stdin:
            if mm == '*': mm = mm_stdin
            if mm == 0: mm = '00'
            print(f'{hh}:{mm} tomorrow - {task}')
        elif hh_task > hh_stdin:
            if mm == '*': mm = '00'
            print(f'{hh}:{mm} today - {task}')
        else:
            if mm == '*':
                print(f'{hh}:{mm_stdin} today - {task}')
            else:
                mm_task = int(mm)
                if mm_task < mm_stdin:
                    print(f'{hh}:{mm} tomorrow - {task}')
                else: print(f'{hh}:{mm} today - {task}')
    elif mm != '*':
        mm_task = int(mm)
        if mm_task < mm_stdin:
            print(f'{int(hh_stdin) + 1}:{mm} today - {task}')
        else:
            print(f'{hh_stdin}:{mm} today - {task}')


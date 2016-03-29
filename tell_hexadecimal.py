# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 03:05:02 2016

@author: User
"""


def hexadecimal(num):
    s=0
    p=n=len(num)
    overten={'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    while n:
        try:
            if num[n-1] in overten:
                a=overten[num[n-1]]
            else:
                a=int(num[n-1])
            s+=a*16**(p-n)
            n-=1
        except ValueError as ve:
            return('invalid input, %s\n%s'%(num[n-1], ve))
    return s

while 1:
    num=input('input num: ')
    print(hexadecimal(num))

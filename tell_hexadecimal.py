# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 03:05:02 2016

@author: User
"""


class Hexadecimal(object):
    """return hexadecimal number"""
    def __init__(self, num):
        self.num=num
        self.overten=(('A', 10), ('B', 11), ('C', 12), ('D', 13), ('E', 14), ('F', 15))
        self.flag=flag

    def __call__(self, flag):
        if flag:
            return self.hexadecimal_to_decimal()
        else:
            return self.decimal_to_hexadecimal()

    def hexadecimal_to_decimal(self):
        """convert hexadecimal into decimal"""
        s=0
        overten={k:v for k, v in self.overten}
        for i, val in enumerate(self.num):
            try:
                if val in overten:
                    val=overten[val]
                s=s*16
                s+=int(val)
            except ValueError as ve:
                return('invalid input, %s\n%s'%(val, ve))
        return s

    def decimal_to_hexadecimal(self):
        """convert decimal to hexadecimal"""
        overten={v:k for k, v in self.overten}
        try:
            num=int(self.num)
        except ValueError as ve:
            return('invalid input, %s\n%s'%(self.num, ve))
        hexanum=[]
        while num>0:
            rem=num%16 #remainder
            if rem>=10:
                rem=overten[rem]
            hexanum.append(str(rem))
            num=int(num/16) #quotient
        hexanum.reverse()
        s=''.join([x for x in hexanum])
        return s


while 1:
    num=input('input num: ')
    flag=input('if decimal input, 0+Emter, else, 1+Enter: ')
    hexa=Hexadecimal(num)
    print(hexa(int(flag)))

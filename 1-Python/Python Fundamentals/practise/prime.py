# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 19:53:59 2025

@author: sam77
"""


'''Array with n elements expcted to find
 sum of values that are present in non-prime
 indices of the array.'''
 
 
def sum_at_non_prime():
    n=int(input("Enter number of digits"))
    arr=[n]
    addition=0
    for i in range(n):
        num=int(input(f'enter {i}th number'))
        arr[i]=num
        addition=addition+num   
    return addition
sum_at_non_prime()   


###############################
#################################3


def salam(hello):   
    def wrapper():
        print("salam bhai")
        return hello()
    return wrapper
    

@salam
def hello():
    print("hello bhai")
hello()
    



























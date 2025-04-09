# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 08:14:05 2025

@author: sam77
"""

#test 9 april,2025
employee_details=[]
def collect_employee_details():
    employee_details=[]
    num=int(input("Enter number of employees:- "))
    if num<=0:
        print("Inavlid Input")
        return 0
    for i in range(num):
        name=input(f"Enter name of employee{i+1}:- ")
        
        age=int(input(f"Enter age of employee{i+1}:- "))
        if age<21 or age>58:
            print("Inavlid Input")
            return 0
        Band=input(f"Enter Band of employee{i+1}:- ")
        Band=Band.upper()
        if Band!='A' and Band!='B' and Band!='C'and Band!='D':
            print("Inavlid Input")
            return 0
        Designation=input(f"Enter Designation of employee{i+1}:- ")
        employee_details.append([name,age,Band,Designation])
    print(employee_details)
        
collect_employee_details()   


#################################################
#################################################

def longest_negative_sum(int_list, length):
    count=0
    summation=0
    neg_list=[]
    neg_lists=[]
    for i in int_list:
        if i <0:
            neg_list.append(i)
            count=count+1
            summation=summation+i
        elif i>0:
            neg_lists.append([neg_list])
            return -1
    for neg_list in neg_lists:
        if len(neg_list)
    return summation
    
    
    
d_list=["a","b"]
d2_list=["1","2"]

final_list=[[]]
i=0
list2=["hello","brother"]
final_list=final_list.append(list2)
final_list
final_list=[[d_list],[d2_list]]
final_list

a=input("enter")
b=input("enter2")
mylist=a
mylist=b
mylist    
     
longest_negative_sum(my_list,length)
    
            
 
        
 
    
 
def longest_negative_sum(int_list, length):
    if not int_list:
        return -1

    neg_lists = []
    neg_list = []

    for i in int_list:
        if i < 0:
            neg_list.append(i)
        else:
            if neg_list:
                neg_lists.append(neg_list)
                neg_list = []
    
    if neg_list:
        neg_lists.append(neg_list)

    if not neg_lists:
        return -1

    max_len = max(len(l) for l in neg_lists)
    total_sum = 0
    for l in neg_lists:
        if len(l) == max_len:
            total_sum += sum(l)

    return total_sum

longest_negative_sum([1, 2, 3, 4],4)
longest_negative_sum([-1, -2, -3, 4, -1, -2],6)
longest_negative_sum([1, 2, 3, 4],4)
longest_negative_sum([-1, -2, 0, -1, -2, 0, -1, -2],8)



    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
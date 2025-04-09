# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 09:28:42 2025

@author: sam77
"""

print("hello world")

x=1
print(x)
print(type(x))

x=1000000000000000.500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
print(x)
print(type(x))
 
age1=input("tell me ur age?")
age2=input("tell me ur other age?")
age=age1+age2
print(age)

print(type(age))

age1=int(input("what is ur age?"))
age2=int(input("The other age?"))
finalage1_2=age1+age2
print(finalage1_2)

age3=float(input("Age is?"))
age4=float(input("Other age is?"))
finalage3_4=age3+age4
print(finalage3_4)


int_value=100
print(type(int_value))
string_value="2.56"
print(type(string_value))
float_value=float(int_value)
print("float value of int is",float_value)
print(type(float_value))

float_value2=float(string_value)
print(float_value2)
print(type(float_value2))

c1=1
c2=2j
print("c1:",c1,"c2:",c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

all_ok=True
print(all_ok)
all_ok=False
print(all_ok)
print(type(all_ok))


status=bool(input("What is the status?"))
print(status)



int=6
print(int)

complex= 3+4j
real_part=complex.real
imaginary_part=complex.imag
print("complex part:- ",real_part)
print("real part :- ",imaginary_part)




#power
a=2
b=3
print(a**b)

#none datatype
winner=None
print(winner is None)
print(winner is not None)
print(winner)
print(None)
print(type(None))


#if-else

num=int(input("what is the number buddy?"))
if num<0:
    print("Input is negative")
else:
    print("Input is positive")
    
    
    
#el-if
savings=float(input("Enter bank balance?"))

if savings==0:
    print("sorry no savings")
elif savings<1000:
    print("low on savings")
elif savings<10000:
    print("moderate savings")
elif savings<100000:
    print("Nice sum")
else:
    print("Filed")
 
    
 
#while counter
count=1
while count <= 10:
    print(count)
    count+=1
    
    
#for counter
for _ in range (0,10):
    print(".",end=" ")
    
#break
num=int(input("what is the number?"))

for i in range(0,6):
    if i==num:
        break
    print(i," ", end=" ")
    print("done")
    
    
#odd numbers

start,end=3,21

for num in range(start,end+1,step):
    if num%2!=0:
        print(num)
        
        
#even numbers

start,end=4,15
chal=2
for i in range (start,end+1,chal):
    
        print(i)


#functions

x="awesome"
def my_function():
    x="awe"
    print("python is "+x)
my_function()
print("python is "+x)

x = "awesome"

def my_function():
    print("Python is "+x)

my_function()


def my_function():
    print("Hello, world!")

my_function()


x="a"
def my_funtion():
    
    x="b"
    print("python is"+x)
    
my_function()




#21 Feb

#sorting colors

input_colors="red-yello-blue-green"
def sorting_alphabetically():
    splitted_colors=input_colors.split('-')
    sorted_colors=sorted(splitted_colors)
    return sorted_colors
    
    
sorted_colors=sorting_alphabetically()
print(sorted_colors)





#negative indexing

n= [10, 20, 30, 40, 50, 60]

print(n[-6:])
print(n[5:0:-2])


"""10, 20, 30, 40, 50, 60
   0   1   2   3   4   5
 -6  -5  -4  -3  -2  -1"""

"""they are independent indexing of each other so no confusion 
positive integers have 0 with them and the negative interger have their 
own indexing so no confusion""" 
 
 
#tokenization

names='kirmada-shinchan-lucky man-Indrawarma-buta gorilla'
def rearranging_aplphabetically():
    splitted_names=names.split('-')
    sorted_names=sorted(splitted_names)
    arranged_names='-'.join(sorted_names)
    return arranged_names
result=rearranging_aplphabetically()
print(result)
 
names='Kirmada-shinchan-Lucky man-Indrawarma-Buta gorilla'
def rearranging_aplphabetically():
    return '-'.join(sorted(names.split('-')))



#positive or negative

def PoNe():
    num=int(input("input number?"))
    if num==0:
        print("zero input")
    elif num>0:
        print("positve input")
    elif num<0:
        print("neagtive input")
PoNe()


num=int(input("enter input of number?"))
def Pos_Neg():
    print("positive number" if num>0 else "negative number" )
Pos_Neg()
    

#even_odd
num=int(input("enter input of number?"))
def even_odd():
    print("even number" if num%2==0 else "odd number")
even_odd()
    
    
#same last digit for last numbers
num1=int(input("enter input of 1st number?"))
num2=int(input("enter input of 2nd number?"))

def SameLastDig():
    result1=num1%10
    result2=num2%10
    if result1==result2:
        print("same last digit")
    else:
        print("different last digit")
SameLastDig()



#1 to 10 in single line with a tab space

def print1to10():
    for i in range (10):
        print(i,end="   ")
print1to10()
     

#print even bet 23 and 57

def even_nums():
    for i in range(23,57):
        if i%2==0:
            print(i)
even_nums()



#prime nums
def prime_nums():
    for i in range(2, 100):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 2:  
            print(i)

prime_nums()

  


#List functions

lst():
lst=["cherry","mango","apple","banana"]
print(lst)

lst.clear()
print(lst)  

lst.append("doraemon")  
print(lst)  
    
lst=[2,3,5,6,8,7,6,4,3]
lst_even=[]
for i in lst:
    if i%2==0:
        lst_even.append(i)
print(lst_even)



#extend in list

lst1=[1,2,3]
lst2=[4,5,6]
lst1.extend(lst2)
print(lst1)

#insert in list

lst=["cherry","mango","apple","banana"]
lst.insert(2, "guava")
print(lst)

#popping from list
lst.pop(1)
print(lst)
        

lst.reverse()
print(lst)
    
lst=["cherry","mango","apple","cherry","banana"]
lst.sort()
print(lst)


lst_num=[5,65,42,12,400]
lst_num.sorted(lst,key=int)
lst_num
    

def test_even_nums():
    for i in range(23,57):
        if i%2==0:
            print(i)
        
test_even_nums()      
    


num=int(input("enter number"))
def palindrome():
    num_string=str(num)
    num_string_reversed=num_string[::-1]
    print(num_string_reversed)
    if num_string==num_string_reversed:
        print("palindrome")
    else:
        print("not palindrome")
    
    
palindrome()  
    
   
#Nested List

nested_list=[[1,2,3],["A","B","C",'D'],[True,False]]

print(nested_list[-1][])

nested_list[-1][0]=True
print(nested_list[-1][0])        



for sublist in nested_list:
    for item in sublist:
        print(j,end=" ")
    print()


"""List Comprehension with nested list, joined all the elememts  into 1 list
[[[]]]], we get data some times in multi dimensional list this is use to
    remove all that nd create one list for all the data"""

flat_list=[item for sublist in nested_list for item in sublist]
print(flat_list)


nested_list=[[1,2,3],['a','b','c'],['True','False']]
nested_list.append(["new","List"])
print(nested_list)

#adding elements to list

test_list=[1,2]   
test_list.append(3)
print(test_list)

nested_list=[[1,2,3],['a','b','c'],['True','False']]
nested_list[1].append(4)   """nested_list is a mutable object (a list).
                                If you don't reinitialize it, 
                                the changes persist across multiple runs,
                                and 4 keeps getting appended."""
print(nested_list)







#TUPLE
tup=("cherry","banana","cherry")
print(tup)
print(tup[1])
print(id(tup))

x=("apple","banana","cherry")
x[1]='kiwi'
print(id(x))


y=list(x)
y[1]='kiwi'
print(y)
print(id(y))

x=tuple(y)
print(x)
print(id(x))

#To join two or more tuple you can use + operator
tuple1=("a","b","c")
print(id(tuple1))
tuple2=(1,2,3)
print(id(tuple2))
tup1=tuple1+tuple2
print(tup1)
print(id(tup1))






#DICTONARY

dict1={"Brand":"Maruti","model":"2456","year":2011}
print(dict1)
print(len(dict1))
print(type(dict1))

dict1.get("model")
dict1.keys()

car={"Brand":"Ford","model":"mustang","year":"1964"

     }

print(id(car))
x=car.keys)\()
print(x)



#format operator

name = "Sameer"
age = 20
print("My name is {} and I am {} years old.".format(name, age))

print("{1} is older than {0}".format("Krishna", "Sameer"))

print("My name is {name} and I study {course}.".format(name="Sameer", course="ECE"))

print("The price is {:.2f}".format(9.5678))

print("{:<10} | {:^10} | {:>10}".format("Left", "Center", "Right"))


#This feature is called an f-string (formatted string literal) in Python. It allows you to embed expressions inside string literals using curly braces {}.

name = "Sameer"
age=20
print(f"My name is, {name} and I am {age} years old.")


age=50
print(f"The king was {age} years old") 


num1=10
num2=5

print(f"Sum: {num1+num2}, Difference: {num1-num2}, Product: {num1*num2}, Quotient: {num1//num2}")


for i in range(10,50):
    for j in range (2,i):
        if (i%j==0):
            continue
        else:
            break
    print(i)
                
    
    
    
#1.	Write a program to check number of occurrences of specified elements in the list

New_List=['a','b','a','b','c','d','d','d','e','f']
char=input("Number of occurance check? ")
count=0
for i in New_List:
    if i==char:
        count=count+1
print(count)


#2.	Write a program to check whether an element exist in a tuple or not

New_tup=('a','x','l','d','g') 
found=False
char=input("Exist check character? ")
for i in New_tup:
    if i==char:
        print(f"'{char}' exists in the tuple ")
        found=True
        break
      
if not found:
    print(f"'{char}' does not exists in the tuple")
    
    
#3.	Write a program to check number is odd or even

num=int(input("Give number for even odd check"))
if num%2==0:
    print("Input was even")
else:
    print("Ipnut was odd")
    
    
    
#4.	Write a program to print even numbers between 23 to 57.
#Each number should be printed in separate row

for i in range(23,57):
    if i%2==0:
        print(i)
        
        
#5.	Write program to write prime numbers between 10 to 99


for i in range(10,99):
    count=0
    for j in range (1,i):
        if i%j==0:
            count+=1
    if count==1:
        print(i)
        
        
#test

lower_limit=int(input("Enter lower limit for prime numbers:- "))
upper_limit=int(input("Enter upper limit for prime numbers:- "))













#dictionary

sorted_dict={'banana':40,'apple':100,'grapes':120,'mango':200}
free_item_key=min(sorted_dict,key=sorted_dict.get)
free_item_value=sorted_dict[free_item_key]
print(f"The lowest priced item is'{free_item_key}':{free_item_value}")

"""
min(sorted_dict) → Returns the minimum key (alphabetically in this case).
min(sorted_dict, key=sorted_dict.get) → Returns the key with the minimum value.
min(sorted_dict.values()) → Returns the minimum value itself.

"""

sorted_dict={'banana':40,'apple':100,'grapes':120,'mango':200}
free_item_key=max(sorted_dict,key=sorted_dict.get)
free_item_value=sorted_dict[free_item_key]
print(f"The highest priced item is'{free_item_key}':{free_item_value}")


unsorted_dict={'bun':40,'milk':100,'toasst':60,'tea':10}
cheapest=min(unsorted_dict.values())
print(cheapest)



dict1={'apple':40,'banana':50,'chickoo':20}
sum=0
for val in dict1.values():
    sum=sum+val
print(sum)

  
sum=0
dict1={'apple':'40','banana':'50','chickoo':'20'}
total_sum=sum(int(value) for value in dict1.values())
print(total_sum)
    
sum=print1to10
  
sum=0
dict2={'a':'10','b':'20'}
total_sum=sum(int(value) for value in dict2.values())
 

#concatination of two dictionaries

dict1={1:10,2:20,3:30}
dict2={4:40,5:50}
dict1.update(dict2)
print(dict1)

#or
dict1={1:10,3:30}
dict2={4:40}
dict1=dict1|dict2
print(dict1)

#membership operator
dict1={1:10,3:30,'a':2}
print(1 in dict1)
print('a' in dict1)



#break and comtine statements

i=1
while i<6:
    print(i)
    if(i==3):
        break
    i=i+1


#In your code, continue skips the rest of the loop's body 
#and moves directly to the next iteration.

i=1 
while i<6:
    i=i+1
    if(i==3):
        continue
    print(i)

"""BREAK STATEMET BREAKS THE EXECUTION OF THE ENTIRE LOOP
break	Stops the entire loop immediately.
continue	Skips only the current iteration and moves to the next.
"""

fruits=['apple','banana','cherry','orange','mango']
for i in fruits:
    if i=='cherry':
        break
    print(i)
    
fruits=['apple','banana','cherry','mango','rasberry']
for i in fruits:
    print(i)
    if i=='cherry':
        break

fruits=['apple','banana','cherry','plum','guava']
for i in fruits:
    if i=='cherry':
        continue
    print(i)

#range
for i in range(1,30,2):
    print(i)
    
#nested for loops

fruits=['apple','guava','banana','mango','chickoo']
colors=['red','yellow','blue','white']   

for i in fruits:
    for j in colors:
        print(i,j)
        
        
#PRACTICE
        
"""suppose u r selling milk 100 lites and there is a queue so f customers the moment sells reach 
100 litres inform customer that milk finished"""

#solution1
for i in range(100):
    print(i+1,"liter")
print("100 liters completed")


print(for in range(100),"100 liters completed")



#solution2
sold=0
while(sold!=100):
    x=int(input("How much litres do you want?"))
    sold=sold+x
    if sold>=100:
        print("Limit reached!")
        break
    print(sold,"liters of milk sold till now")
print("Sorry we are out of milk! check out later")


"""suppose u r standing in a queue, if professor 
therreare no checking but if students are there checking is done"""

id_card=input(" Enter Id ")
if id_card=='red':
    PRN=input("Enter PRN")
    Roll_No=int(PRN[7:8])
    if Roll_No<100:
        print("OK, ROll number verified, you can enter")
    else:
        print("Error with roll no")

elif id_card=='yellow':
    print("Faculty detected, Welcome sir")
    
    
    
##############################################################

#odd_even

list1=[2,3,5,4,65,69,7,5,-4,-7]
for i in list1:
    if abs(i)%2!=0:
        print(abs(i),"is odd")
    



#sort out -ve

for i in list1:
    if i%2==0:
        print(abs(i),"is an even num")



#function without argument

def my_function():
    print("Hello from a function")
my_function()


#function with argument

def my_function(name):
    print("hello "+name)
my_function("ram")



#function with positional argument, accor

def my_function(name1,name2):
    print(name1+" "+name2)
my_function("world", "hello")


 def my_function(name2,name1):
     print(name1+" "+name2)
 my_function("world", "hello")
   
 
    
 #passing unknkkown number of arguments to a funtion
def my_function(*args):
    print(args[0]+" "+args[2])
my_function("Tappu","Sonu","Goli") 


#passing unknown number of key value pair 
    
def My_Func(**kwargs):
    for key, value in kwargs.items() :
        print(f"{key}:{value}")
My_Func(first_name="papalalal",mid_name="mohanlal",last_name="goyal")
    
    
#default argument and passing

def my_function(country="norway"):
    print("i am from "+country)
my_function()
my_function("denmark")
    
    
    
#passing list to a function
fruits=['apple','banana','chickoo']

def my_function(fruits):
    for x in fruits:
        print(x)
        
my_function(fruits)
    
    
#returning value from a function

def my_function(x):
    y=x*5
    return y
my_function(5)
    
    
#returning multiple arguments
    
def my_function(x):
    y=x*5
    z=x*7
    return y,z
my_function(5)
    

#pass funtion

def my_function1():
    pass
my_function1()


    
#warm up question factorial
    
def factorial(x):
    if x==1:
        return 1 
    else:
        return(x*factorial(x-1))    
factorial(4)



#LIST comprehension lambda funtion

def add(a):
    sum=a+10 
    return sum
add(10)

add = lambda a:a+10 
print(add(20))



multiply=lambda x:x*10 
print(multiply(10))


add=lambda a,b:a+b
print(add(5,6))




#odd numbers using filter and lambda froma list

lst= [12, 24, 33, 45, 50, 61]
odd_list=list(filter(lambda x:(x%2!=0),lst))
print(odd_list)



lst= [12, 16, 33, 25, 50, 100]

sqr_list=list(map(lambda x:(x**2), lst))
print(sqr_list)





################################
#############################
 
#split and join
text="apple,banana,cherry"
words=text.split(",")
print(words)

new_text="-".join(words)
print(new_text)
print(type(new_text))


#.find and . index

text="hello python"
print(text.index("python"))
print(text.find("java"))
print(text.find("python"))
print(text.index("java"))



# count substring occurances
text="banana apple banana cherry banana"
print(text.count("banana"))



#startswith() and endwith()
 
text="Python is Great"
print(text.startswith("Python"))
print(text.endswith("Great"))
print(text.endswith("great"))


#isaplabet->isaplha()
"""isalnum() it would give true for 
either alphabet, number and for a combinatio too"""

text1="python123"
text2="123"
text3="python"
print(text1.isalpha())
print(text1.isdigit())
print(text1.isalnum())
print(text2.isalpha())
print(text2.isdigit())
print(text2.isalnum())
print(text3.isalpha())
print(text3.isdigit())
print(text3.isalnum())


#count number of uppercase letter in string, lowecase

text="HELLO buddy"
count1=0
for i in range(len(text)):
    if text[i].isupper():
        count1=count1+1
print(count1)


text="hello BOYY"
count2=0
for i in range(len(text)):
    if text[i].islower():
        count2=count2+1
print(count2)


text="123456abcdef"
count3=0
for i in range(len(text)):
    if text[i].isalnum():
        count3=count3+1
print(count3)



#usecase for endswith

text1="This is a text."
text2="This is maybe a text"
print(text1.endswith("."))
print(text2.endswith("."))

#####################
#mario pyraminds

#1
for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print()
    
  
#2
for i in range(4):
    for j in range (i+1):
        print("#",end=" ")
    print()
    
#3
for i in range(4):
    for j in range(4-i):
        print("#",end=" ")
    print()
    
#4
for i in range (4):
    for j in range (i+1):
        print("#",end=" ")
    print()
for i in range(4):
    for j in range(4-i):
        print("#",end=" ")
    print()
    
    
#is dupliate
lst=[1,2,3,4,5,6]
for i in range(len(lst)-1):
    if (lst[i]==lst[i+1]):
         return True
return False



#are anagaram or not
 
str='Elbow'
a=list(str.replace("", " ").lower())
sorted(a)

def are_anagram(str1,str2):
    a=list(str1.replace(""," ").lower())
    b=list(str2.replace(""," ").lower())
    
    
########################################################
########################################################
########################################################

#Different Types of Error
print(zzz)#NameError

print("Hello"#SyntaxError
      
str="Hello"
str=str+5#TypeError

print(str[10])#IndexError: string index out of range

dict={1:11,2:22,3:33}
print(dict[5])#KeyError

str="Bye"
str.reverse()#AttributeError

str="moose"
ans_1=int(str)#ValueError

#Syntax,Sementic,Compile
'''
#Types of Exceptions
#Arithmetic exception
#Array index out of bound exception
#Array store
#FileNotFound
#IOException-general I/O Failure
#NullPointer Excetion
#outofmemory Exception
#Security Exception
#StackOverflow Exception

#try://statement except://statement
'''

def calculate_salary(experience,role):
    base_salary={"Intern":30000,"Junior":50000,"Mid-level":80000,"Senior":100000,"manager":150000}
    if role not in base_salary:
        raise ValueError("Invalid job role")
    return base_salary[role]+(experience*2000)

calculate_salary("Intern",30000)


def validate_experience(exp):
    if not isinstance(exp, int) or exp<0:
        raise ValueError("Experience must be non-negative")
    return exp




def validate_role(role):
    valid_roles={"Intern","Junior","Mid-level","Senior","manager"}
    if role not in valid_roles:
        raise ValueError(f"Inavalid role:Choose from {valid_roles}")
    return role
    
validate_role("Intern")



def calculate_salary(experience, role):
    base_salary = {"Intern": 30000, "Junior": 50000, "Mid-level": 80000, "Senior": 100000, "manager": 150000}
    if role not in base_salary:
        raise ValueError("Invalid job role")
    return base_salary[role] + (experience * 2000)


def validate_experience(exp):
    if not isinstance(exp, int) or exp < 0:
        raise ValueError("Experience must be non-negative")
    return exp


def validate_role(role):
    valid_roles = {"Intern", "Junior", "Mid-level", "Senior", "manager"}
    if role not in valid_roles:
        raise ValueError(f"Invalid role: Choose from {valid_roles}")
    return role


# Example calls
print(calculate_salary(2, "Intern"))  # Should return 34000
print(validate_role("Intern"))        # Should return "Intern"

##############################

#eucledian algo for GCD

a=int(input("enter first number: "))
b=int(input("enter second number: "))

while b:
    a,b=b,a%b
print(a)



#math lib for GCD
import math
a=int(input("enter first number: "))
b=int(input("enter second number: "))
gcd=math.gcd(a,b)
print(gcd)


##############
#2nd largest element
def second_largest(lst):
    
    n=len(lst)
    for i in range(2):
        for j in range (n-i-1):
            if lst[j+1]<lst[j]:
                lst[j+1],lst[j]=lst[j],lst[j+1]
    return lst[n-2]
lst=[2,6,4,3,5,9]    
second_largest(lst)

lst=[2,6,4,3,5,9]  
print(len(lst))



#bubble sort

def bubble_sort(lst):
    n =len(lst)
    for i in range (n-1):
        for j in range (n-i-1):
            if lst[j+1]<lst[j]:
                lst[j+1],lst[j]=lst[j],lst[j+1]
    return lst
lst=[2,6,4,3,5,9]
bubble_sort(lst)


#2nd largest

def second_largest(lst):
    unique_nums=list(set(lst))
    unique_nums.sort(reverse=True)
    return unique_nums[1]
    

lst=[2,6,4,3,5,9]
second_largest(lst)


#second_smallest

def second_smallest(lst):
    unique_nums=list(set(lst))
    unique_nums.sort()
    return unique_nums[1]
lst=[2,6,4,3,5,9]
second_smallest(lst)


#missing num
#ask sir about this

def missing_num(lst,n):
    expected_sum=n*(n+1)//2
    actual_sum=sum(lst)
    missing_num=expected_sum-actual_sum
    return missing_num
n=3
lst=[1,3]



#reverse a string without built in funtion

string="My name is Anthony"
print(string[::-1])

#reversing the input string directly
rev_string=input("Enter string to reverse")[::-1]
print(rev_string)


#GCD and LCM



def gcd():
    num1=int(input("enter num1"))
    num2=int(input("enter num2"))
    num1,num2=num1,num1%num2
    return num2
gcd()

num1=int(input("enter num1"))
num2=int(input("enter num2"))
def lcm (num1,num2):
    lcm=abs(num1*num2)/gcd(num1,num2)
    return lcm
lcm(num1,num2)



##############################################################
##############################################################

Flag=0
def prime_or_not():
    num=int(input("Enter number: "))
    for i in range (2,num):
        if (num%i!=0):
            Flag=-1
        elif (num%i==0):
            Flag=1
            break
    if Flag==-1:
        print(num,"is a prime number")
    elif Flag==1:
        print(num,"is not a prime number")
prime_or_not()   



def num_of_vowels():
    count=0
    sentence=input("Give input to calculate number of vowels:-  ")
    low=sentence.lower()
    print(low)
    for i in sentence:
        if (i=='a' or i=='e' or i =='i' or i=='o' or i=='u'):
            count=count+1
    print("Number of vowles in your string is :- ",count)
num_of_vowels()   
    
def gcd():
    num1=int(input("First number: "))
    num2=int(input("Second number: "))
    
    for i in (1,num1):
        if num1%i==0:
            flag=1
            gcd=i
        elif num1%i!=0:
            flag=-1
            break
gcd()


#print num 1 to 10 with tab space
for i in range(1,11):
    print(i,end="    ")
    
    
#insert square of 1 to 15 in dictionary
def new_dict():
    new_dict={}
    for i in range (1,16):
        new_dict[i]=i*i
    return new_dict
new_dict()
   


""""Gary question for steup up and step down DDUUUDD thing"""



#recursion limit function

import sys
sys.setrecursionlimit(1000) #sets recusrion limit

def safe_recursive_function(depth=0,max_depth=10):
    if depth>=max_depth:
        return "Done"
    return safe_recursive_function(depth+1,max_depth)
print(safe_recursive_function())




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    







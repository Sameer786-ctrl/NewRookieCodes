# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 08:17:46 2025

@author: sam77
"""
########################################################
def plus_one(number):
    number1=number+1
    return number1
plus_one(5)

###########################

def calculate(num):
    def add_one(number):
        number1=number+1
        return number1
    result=add_one(num)
    return result
calculate(5)
        
###########################################
#defining function inside another function
def plus_one(number):
    result1=number+1
    return result1

def function_call(function):
    result=function(5)
    return result

#function calls function
function_call(plus_one)

#######################333

def hello_funtion():
    def say_hi():
        return "Hi"
    return say_hi

#hello_function() would not wokrk it would return object

s=hello_funtion()
s()


######################################
###################################
#decorators in advanced ptyhton

import time
def calc_square(numbers):
    start=time.time()
    result=[]
    for number in numbers:
        result.append(number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"total time for execution is {total_time}")
    return result


def calc_cube(numbers):
    start=time.time()
    result=[]
    for number in numbers:
        result.append(number*number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"total time for execution is {total_time}")
    return result

array=range(1,100000)
out_square=calc_square(array)
out_cube=calc_cube(array) 


#decorators in advanced ptyhton


def say_hi():
    return 'hello there'

def uppercase_decorator(function): #function passed as an argument
    def wrapper():
        func=function()  #create object of the function
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
decorate = uppercase_decorator(say_hi)
decorate()
        


#using @
def uppercase_decorator(function): #function passed as an argument
    def wrapper():
        func=function()  #create object of the function
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'
say_hi()

#decorators are used in flask programming

#######################################################################

def split_string(function):
    def wrapper():
        func=function()
        splitted_string=func.split()
        return splitted_string
    return wrapper

def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper

@split_string
@uppercase_decorator

def say_hi():
    return 'hello there'
say_hi() 


#####################################################################3





def time_it(func):
    def wrapper(*args,**kwargs):
        #*args and **kwargs allow wrapper 
        #to accept any number of positional and keyword
        start=time.time()
        result=func(*args,**kwargs)
        #calls the original funcion (func)
        #with the provided arguments
        end=time.time()
        print(func.__name__+" took "+str((end-start)*1000)+"mil sec")
        return result
    return wrapper


@time_it
def calc_square(numbers):
    result=[]
    for number in (numbers):
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result=[]
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,100000)
out_square=calc_square(array)
out_cube=calc_cube(array)


###############################################################

def log_decorator(func):
    def wrapper(*args,**kwargs):
        
        ''' log_decorator wraps add

When @log_decorator is applied to add, it replaces add with wrapper.

So, add(3,4) is actually calling wrapper(3,4).'''
        
        print(f"Calling {func.__name__} with {args}{kwargs}")
        return func(*args,**kwargs)
    return wrapper
       
@log_decorator
def add(a,b):
    return a+b

print(add(3,4))
    

##################################

#accesss control

        
def auth_required(func):
    def wrapper(user):
        if not user.get("authenticated",False):
            
            print("Access Denied")
            return
        return func(user)
    return wrapper
 
@auth_required
def dashboard(user):
    print(f"Welcome {user['name']}!")

user1={"name":"Alice","authenticated":True}
user2={"name":"Bob","authenticated":False}

dashboard(user1)
dashboard(user2)

##################################33
#validation
#ensures inputs meet certain criteria before executing


def validate_positive(func):
    def wrapper(x):
        if x<0:
            raise ValueError("negative values are not allowed")
        return func(x)
    return wrapper

@validate_positive 
def square_root(x):
    return x**0.5

print(square_root(4))   #works fine 
print(square_root(-4))  #raises value error 


######################################33333333333
##rate limiter




import time
def rate_limiter(max_calls,time_frame):
    calls=[]
    def decorator(func):
        def wrapper(*args,**kwargs):
            now=time.time()
            while calls and now-calls[0]>time_frame:
                calls.pop(0)
                
            if len(calls)>=max_calls:
                print("RAte limit reached. Try again later")
                return
            calls.append(now)
            return func(*args,**kwargs)
        return wrapper
    return decorator

'''
calls is a list that stores timestampsof previous function calls
calls[0] represents the oldest function call in the list
now is the current time when the function is being called
now-calls[0] computes when the oldest call occured 
if that time exceed the time frame it means that the function is no longer 
within the window adn can be removed
 '''

@rate_limiter(3,10)
def say_hello():
    print("Hello!")
    
    
say_hello()
say_hello()
say_hello()
say_hello()
say_hello()


################################################################
##################################################################
#3 april 2025
#list comprehension
lst=[]
for num in range(20):
    lst.append(num)
print(lst)

#
names=['dada','mama','chacha']
lst=[name.capitalize() for name in names ]
print(lst)

########
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)

############


lst=[f"{x}{y}"for x in range(5) for y in range(3) ]
print(lst)


##set comprehension

set_one={x for x in range(3)}
print(set_one)

#dictionaay comprehension
dict={x:x*x for x in range (3)}
print(dict)


#generators in python
#naother way of creating iterators
#it uses a keyword yeild insted of returiing

gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)
    
##########33
gen=(x for x in range(3))
next(gen)

#3333
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)

gen=range_even(6)
next(gen)


#########################33
#########################3
def lengths(itr):
    for ele in itr:
        yield len(ele)

def hide(itr):
    for ele in itr:
        yield ele*'*'
        
        
'''
ele* appears to be a placeholder for an element from an iterable.

'''
        
passwords=["hello","sameer","radhe mohan"]

for password in hide(lengths(passwords)):
    print(password)

#############33
lst=["milk",'egg','bread']
for index ,item in enumerate (lst, start=1):
    print(f"{index} {item}")
    
#########
#use of zip function
name=['dada','mama','kaka']
info=[1234,2345,3456]
for nm,inf in zip(name,info):
    print(nm,inf)

#zip with mismatched no of lements
name=['dada','mama','kaka','lala']
info=[1234,2345,3456]
for nm,inf in zip(name,info):
    print(nm,inf)
    #lala not displayed
    
#using zip_longest to get lala as well
from itertools import zip_longest
name=['kaka','baba','lala','raja']
info=[1234,2345,3456]
for nm,inf in zip_longest(name,info):
    print(nm,inf)

from itertools import zip_longest
name=['dada','mama','kaka','tai']
info=[1234,23456,34556]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)

##############################
#all function

lst=[1,23,4,87,0]
if all(lst):
    print("no null values")
else:
    print("there are null values")
    
#any function
lst=[0,0,0,0,000]
if any(lst):
    print("some non null values")
else:
    print("all null")
    
    
# count() from itertools
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))    

from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))

#cycle()
import itertools
instructions=('Eat','Code','Sleep')
for instruction in itertools.cycle(instructions):
    print(instruction)
    
    
###########################33
###################3
# 4/4/25


#repeat() in itertools
from itertools import repeat
for msg in repeat("Hello",times=5):
    print(msg)

#combination
from itertools import combinations
players=['a','b','c']
for i in combinations(players,2):
    print (i)


#permutation
from itertools import permutations
players=['a','b','c']
for i in permutations(players,2):
    print(i)
    
#product
team_a=['a','b','c']
team_b=['1','2','3']
from itertools import product
for pair in product(team_a,team_b):
    print(pair)


#filter
age=[14,46,13,40,27]
adults=filter(lambda age:age>=18, age)
print([age for age in adults])


#mapping the same references
list_a=[1,2,3,4]
list_b=list_a
print(list_a)
print(list_b)
list_b[0]=-10
print(list_a)
print(list_b)


#shallow copy works in 1 level list
import copy
list_a=[1,2,34,5]
list_b=copy.copy(list_a)

list_b[0]=-10
print(list_a)
print(list_b)
#different op since different object or say different memory location


#shallow copy is only useful in 1 level list
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.copy(list_a)
list_b[0][0]=-10
print(list_a)
print(list_b)
#same op 


#deep copies

import copy
list_a=[[1,2,3,4],[5,6,7,8,9]]
list_b=copy.deepcopy(list_a)

list_b[0][0]=-10
print(list_a)
print(list_b)


#checking id in assignment
old =[[1,2,3,4],[5,6,7,8,9]]
list_b=list_a

list_b[0][0]=-10

print(list_a)
print(id(list_a))
print(list_b)
print(id(list_b))

#checking id in shallow copy
import copy
list_a=[[1,2,3,4],[5,6,7,8]]
list_b=copy.deepcopy(list_a)
list_b[0][0]=-10
print(f"value of list a {list_a} and id of a is {id(list_a)},value of list b {list_b} and id of b is {id(list_b)} ")
#different id

#checking id in deep copy
#similar



#unpcking dictionary
friends={
    "Dale":9850,
    "Male":6032
    }

contacts={
    
    "dada":8530,
    "mama":5286
    }

contacts.update(friends)
print(contacts)

#pipe operator

friends={
    "satish":6566,
    "Ram":97603
    }
sham={"sham":556}

all_friends=friends|sham
print(all_friends)

#############33
##############3

def process_transaction(transaction):
    if 'ERROR' in transaction[2]:
        raise ValueError("Tranasaction failed!")
    return f"Processed transaction: {transaction}"

with open("C:/1-Python/transaction.csv") as file:
    reader=csv.reader(file)
    next(reader)
    
    for index,transaction in enumerate(reader,start-1):
        try:
            result=process_transaction(transaction)
            print(f"Row{index}:{result}")
        except ValueError as e:
            print(f"Error at inex{e}")

#############

'''
imagine a customer support team where new tickket s are assigned 
to available agents in a round-robin manner.
Each agent should recieve the next ticket in sequence.
If the last agent is reached the cycle should restart
form the first agent automatically

'''
import itertools

agents=['Alice','Bob','Charlie','David']
agent_cycle=itertools.cycle(agents)
tickets=["Ticket-101","Ticket-102","Ticket-103","Ticket-104","Ticket-105","Ticket-106"]
assignments={ticket:next(agent_cycle) for ticket in tickets}
for ticket,agent in assignments.items():
    print(f"{ticket}->Assigned to:{agent}")


import itertools
import time
agents=['Alice','Bob','Charlie','David']
agent_cycle=itertools.cycle(agents)
tickets=["Ticket-101","Ticket-102","Ticket-103","Ticket-104","Ticket-105","Ticket-106"]
assignments={ticket:next(agent_cycle) for ticket in tickets}
for ticket,agent in assignments.items():
    start=time.time()
    print(f"{ticket}->Assigned to:{agent} at {start}")

############################
#shallow copy use case
import copy
report_template={
    "name":"",
    "scores":[0,0,0],
    "remarks":"Pending"    
    }

#shallow copy for a new student
student1_report=copy.copy(report_template)
student1_report["name"]="Alice"
student1_report["scores"][0]=85
print(report_template["scores"])

#deepcopy use case
import copy
report_template={
    "name":"",
    "scores":[0,0,0],
    "remarks":"Pending"    
    }

#deep copy for a new student
student2_report=copy.deepcopy(report_template)
student2_report["name"]="bob"
student2_report["scores"][0]=93
print(report_template["scores"])


import copy
params={
        "layers":[64,158,256],
        "activation":"relu"
        }

experiment1=copy.deepcopy(params)
experiment2=copy.deepcopy(params)

experiment1["layers"][0]=32
print(params["layers"])

#######################
#use case of filter
users=[
       {"name":"Alice","role":"admin"},
       {"name":"Bob","role":"editor"},
       {"name":"Charlie","role":"admin"}
       ]
admins=list(filter(lambda user:user ['role']=='admin',users))
print(admins)

#########################################

import time

patients=int(input("number of patients"))
for i in (patients): 
    reporting=time.time() 
    
    print(f"You should report at {reporting}")
    reporting=reporting+10





import itertools
import time

agents=['Alice','Bob','Charlie','David','bal','tal']
agent_cycle=itertools.cycle(agents)
clock_time = time.time()


tickets=["Ticket-101","Ticket-102","Ticket-103","Ticket-104","Ticket-105","Ticket-106"]
assignments={ticket:next(agent_cycle) for ticket in tickets}
for ticket,agent in assignments.items():
    print(f"{ticket}->Assigned to:{agent} at time {clock_time}")
    clock_time=clock_time+600
    clock_time = time.strftime("%H:%M:%S", time.localtime(clock_time))



import time

start = time.time()
clock_time = time.strftime("%H:%M:%S", time.localtime(start))

print(clock_time)


import time

start = time.time()
future = start + 600  # 10 minutes later

future_time = time.strftime("%H:%M:%S", time.localtime(future))
print(future_time)



import time

patients = ["Patient-001", "Patient-002", "Patient-003", "Patient-004", "Patient-005"]
start_time = time.time()  # current time

for i, patient in enumerate(patients):
    visit_time = start_time + (i * 600)  # add 10 minutes per patient
    formatted_time = time.strftime("%H:%M:%S", time.localtime(visit_time))
    print(f"{patient} -> Visit scheduled at: {formatted_time}")
    
###########################################################################
##########################################################################
    







































































        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      












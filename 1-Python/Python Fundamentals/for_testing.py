# -- coding: utf-8 --
"""
Spyder Editor

This is a temporary script file.
author chanchal
"""
print("hello")

num1=10
num2=5.2
result=False
print(type(num1))
print(type(num2))
print(type(result))
print("hello world")

x=90.0000
print(type(x))

x=10000000000000000000000000000000000000000000000000000000000
print(type(x))

x=input("enter")
x=int(x)
x=x+3
print(x)
print(type(x))

y=int(input("Enter your Year of Birth :"))
y=2025-y
print("Your Age is :",y)


# float input
name=input("Enter Your Name:")
print("Here is Your Introduction : \n My Name is %s and I am %i Years old"%(name,y))

#complex no 
c1=1
c2=2j
print(type(c2))
print('c1: %i , c2:%s'%(c1,c2))

#boolean value 
status=bool(input("OK this Is Comfirmed or Not:"))
print(status)

#Arithmatic Operator
a=10.5
b=6.0
c=3.3
print(a**b)
print(type(c))
c=int(a)-int(b)
print(type(c))

#(identity operator) is and is not
a=3
b=3
print(a is b)
print(a is not b)

#comparison operator == , <= ets.
a=3
b=4
print(a==b)

#membership operator in and not in 
a=[1,3,9]
b=[9]
print(a in b)
print(b in a)


# conditional statement
a=int(input("Chanchal Enter your password:"))
password_of_chanchal=12345
if a==password_of_chanchal:
    print("login successfully !")
else:
    print("inavalid Credintials !!!")
    
# elif use

name1='chanchal'
pass1=1234
name2='shraddha'
pass2=5678
a=input("enter your username:")
if a==name1:
    b=int(input("Enter your password :"))
    if b==pass1:
        print("Login successfully !")
    else:
        print("Wrong password")
elif a==name2:
    b=int(input("Enter your password :"))
    if b==pass2:
        print("Login successfully !")
    else:
        print("Wrong password !!!")
else:
    print("Invalid Credentials!!!!")
    
#loop statements
a=int(input("Enter the range from upto which you want to print a no:"))
for i in range(1,a+1):
    print(i)
print("Done !")

#pattern printing
for _ in range(0,5):
    for _ in range(0,_):
        print('*',end=' ')
    print('*')

for i in range(0,5):
    if i==3:
        break
    else:
        print(i)

#even and odd nos    
start=1
a=0
odd=[]
even=[]
while start!=20:
    if start%2==0:
        even.append(start);
    else:
        odd.append(start);
    start+=1
print(even,'\n',odd)

#local and global variable
def my_function():
    print(x)
    y='done'
    print(y)
x='python is awesome'
my_function()
print(x)

#dictionary
chanchal={"surname":"chavhan","age":19,"branch":"ECE"}
print(type(chanchal))
print(chanchal)

#type casting
x=int(1.3)
print(type(x),  x)

#formating operator in print
a=4
b='5'
print(a+b)
print(f"Hello{b}")

#commenting and double line string
s='''chanchal karna chavhan
Roll no:10
Branch:Electronics and Computer Engineering'''#paragraph declaration
print(s)

'''-------------------------------------------------------'''

#function of string
string='Hello World!'
#1) len()
len("hello")

#2) upper()
string.upper()

#3) slicing[]
print(string[:4])
print(string[4:])
a='I am staying in Jay colany'
print(a[16:])
print(a[0:-1])


#slicing for reversing the string
a='hello'
print(a[::-1])
'''string[start:stop:step]'''
#when we add 2 for step it will jumb one step means skip one letter
print(a[1:4:2])

#4) type casting in string str()
a=123
a=str(a)
print(type(a))

#5) lower to upper and viceversa with lower() and upper()
a='abc'
a.upper()
b.lower()

#6) deleting the element from the string using strip() and r strip when we want only right hand side space
a='  1abc  '
a.strip()
a.strip('1')
'''default value for this is space'''

#7) repace the word with replace()
'''format:  string.replace(old, new [, count])'''
a='hello world '
a.replace('world','universe')

a='hello world ,but not whole world'
a.replace('world','universe',1)

#8) split() #world tokenization and sentence 
x='hello_world'
print(x.split("_"))
'''string.split([sep[, maxsplit]]) '''
x='h_e_l_l_o'
print(x.split("_",2))

#9)  joining the string join()
#FORMAT==> separator.join(iterable)
a=['hello','world']
b='_'.join(a)
print(b)

#10) sort function
colors=[]
for i in range(0,5):
    char=input("Enter the %i th Color:"%(i))
    colors.append(char)
colors=sorted(colors)
print(colors)
colorsa=' '.join(colors)
print(colorsa)

#11) find function
#finds the specified string index
a='chanchal scored 94 marks in python'
print(a.find('94')) 
b=a.find('94')
print(a[b:b+2])
  

#12) to add white space
x='Hello'
y='World!' 
print(x+" "+y)

#13) format function and f operator
#we can concatinate the string with integer
quantity=3
item_no=54
price=67
print(f"i want {quantity} pieces and item no is {item_no},its price is {price} ")
#this is using f operator 

#using format function
my_order="i want {} pieces and item no is {} , its price is{}"
print(my_order.format(quantity,item_no,price))
#instead of this we can also use place holders as ** my_order="i want {0} pieces and item no is {1} , its price is{2}"

#14) escape characters for double some string
#text="hi This is Chanchal Chavhan "my cgpa is 9.33""
#print(text)
text="hi This is Chanchal Chavhan \"my cgpa is 9.33\""
print(text)

#python boolean
#returns true if conditions are true, false otherwise
print(10>9)
print(5<6)

a=90
b=60
if (a<b):
    print("a is less than b")
else:
    print("b is less than a")

#python works on PEDMAS rule 

#identity operator 'is' and 'is not'
#works same as booleam operator true false 
# membership operator 'in' and 'not in' these are used on list




lst= [12, 24, 33, 45, 50, 61]
filter (lambda x:(x%2!=0))








file=open(example.txt)



with open('example.txt','r') as file:
    content=file.read()
    print(content)


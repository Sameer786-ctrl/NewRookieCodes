# Write a Python program that takes two floating-point numbers as input, adds them,
#  and prints the result with only two decimal places.

num1=float(input("Enter number 1:- "))
num2=float(input("Enter number 2:- "))
print(round(num1+num2,2))


# Write a function that takes a number as input and 
# prints whether it is positive, negative, or zero using 
# an if-elif-else statement.

def new():
    x=int(input("Give the input number:- "))
    if x<0:
        print("Negative Number")
    elif x>0:
        print("Positive Number")
    else:
        print("Zero")

new()


#prime numbers
flag=0
for i in range(200):
    for j in range (2,i):
        if i%j==0:
            flag=0
            break
        elif i%j!=0:
            flag=1
            
            
    if flag==1:
        print(i," is a prime number")
        
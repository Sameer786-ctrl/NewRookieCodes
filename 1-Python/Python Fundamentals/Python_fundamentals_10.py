# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 08:40:11 2025

@author: sam77
"""

#########################
############################
#file handeling
#for read only
with open('hello.txt','r') as file:
    content=file.read()
    print(content)
    
#for write
with open('hello.txt','w') as file:
    file.write("new file")
    

with open ("C:/1-Python/pi_digits.txt",'r') as File:
    contents=File.read()
    print(contents.rstrip))
    
with open ("C:/1-Python/pi_digits.txt") as File:
    s=File.read()
    print(s.rstrip())
    
with open ("C:/1-Python/pi_digits.txt") as File:
    lines=File.readlines()
    if lines:
        print("FL",lines[0].strip())
        
        
    #######################
############error in creating file    
filename='D:/10-python/programming.txt'
with open(filename,'w') as file:
    file.write("I love programming")
    in_line=input("Enter line")
    file.write(in_line)
    
    ###########
    ########
    
    
##read contents from txt file 
#and store each line into a list

filename='C:/1-Python/pi_digits.txt'
with open (filename,'r') as file:
    lines=file.readlines()
    pi_strings=[]
    for line in lines:
        pi_strings.append(line.rstrip())
        
    print(pi_strings)
    
    

##################################33
##################################33

filename='C:/1-Python/10-python/programming.txt'
with open(filename,'r') as file:
    lines=file.readlines()
    longest_word=''
    for line in lines:
        words=line.split()
        for word in words:
            if(len(word)>len(longest_word)):
                longest_word=word
print("Longest word",longest_word)


############################

sentence='world wide web'
sentence=sentence.upper()
words=sentence.split()
words    
char_lists=[list(word)for word in words]
char_lists

first_char=char_lists[0][0]
last_char=char_lists[0][-1]

ascii_first=ord(first_char)
ascii_last=ord(last_char)

first_char
last_char
ascii_first
ascii_last


sentence='world wide web'
sentence=sentence.upper()
words=sentence.split()

char_lists=[list(word)for word in words]

ascii_difference=[]
for word in char_lists:
    first_char=word[0]
    last_char=word[-1]
    ascii_first=ord(first_char)
    ascii_last=ord(last_char)
    
    difference=abs(ascii_first-ascii_last)
    ascii_difference.append(difference)
    
#result
for word,diff in zip (words,ascii_difference):
    print(f"Word: {word}, ASCII Differnce: {diff}")

####################################
word_sums=[]
for word in words:
    length=len(word)
    total=0
    
    for i in range:
        
        
        
###################################################################
#####################################################################
# 20th of march Thursday
#exception handeling 


#take two float inputs divide and with two exception case
try:
    num1=int(input("Give first number "))
    num2=int(input("Give second number "))
    num=num1/num2
    print("Result is ",num)
except ZeroDivisionError:
    print("Division with zero not allowed")
except ValueError:
    print("invalid input")
    num1=int(input("Give first number "))
    
    
#take input from unser to check number is prime or not
#with value erroer of invalid input


def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
   
try:
    num=int(input("ENter number"))
    if is_prime(num):
        print("Number is prime")
    else:
        print("Number is not prime")
except ValueError:
    print("Invalid input, integer input is expected")


#######################
try:
    file_name=input("Enter file name with absolute adress:")
    with open(file_name,'r') as file:
        content=file.read()
        print(content.capitalize())
except FileNotFoundError:
    print("Error : File not found")


##############################
'''declare a list with 10 integeres and ask the user for an index
and at tht index check if the number is positive or negative.
For invalid index handle the exceptiona d show a error message


'''

numbers=[1,56,48,-65,-45,9,2,-6,2,-56]
try:
    index=int(input("Enter index to be checked:- "))
    value=numbers[index]
    if value>0:
        print("Positive number")
    else:
        print("Negtive number")
except IndexError:
    print("Error : Index out of range")
except ValueError:
    print("Error : Only integer inputs expected")
    
    
    
    
    
    
''''Command line arguments'''
from sys import argv
print("The Fisrt argument",argv[1])
print("The Second argument",argv[2])



###############################################################3
####################################################################

# Function to add two numbers represented as strings
# Assumption: The input will contain only numeric digits.
# The input strings can be of any large lengths.
def add_of_string(num1, num2):
    # Convert the strings to integers, perform addition, and convert back to string
    sum = str(int(num1) + int(num2))
    return sum

# Example usage
print(add_of_string("1234", "56"))


from collections import Counter

# Function to find the most frequently occurring digit in a list of numbers
def most_frequent_digit(numbers):
    digit_count = Counter()
    
    # Count occurrences of each digit in all numbers
    for num in numbers:
        digit_count.update(str(num))
        
    # Find the maximum frequency of any digit
    max_frequency = max(digit_count.values())
    
    # Collect all digits that appear with maximum frequency
    most_frequency = [int(digit) for digit, count in digit_count.items() if count == max_frequency]
    
    return most_frequency, max_frequency

# Example usage
numbers = [1237, 262, 666, 140]
most_frequency, frequency = most_frequent_digit(numbers)
print(f"Most frequently occurring digit: {most_frequency}")


# Function to find the digit to remove to make a number a palindrome
def find_digit_to_remove(input1):
    str_num = str(input1)  # Convert number to string
    
    # Check if number is already a palindrome
    if str_num == str_num[::-1]:
        return -1  # No digit needs to be removed
    
    # Try removing each digit one by one
    for i in range(len(str_num)):
        new_num = str_num[:i] + str_num[i+1:]  # Remove digit at index i
        if new_num == new_num[::-1]:  # Check if new number is palindrome
            return int(str_num[i])  # Return the removed digit
    
    return -1  # If no single digit removal makes it a palindrome

# Example usage
print(find_digit_to_remove(12332))
print(find_digit_to_remove(251532))
print(find_digit_to_remove(10101))
print(find_digit_to_remove(981894))


# Function to find the sum of values present at non-prime indices in an array
# Note: The array index starts from 0
def sum_non_prime(input1, input2):
    # Function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    total = 0
    for i in range(input2):
        if not is_prime(i):  # Check if index is non-prime
            total += input1[i]  # Add the value at non-prime index
    
    return total

# Example usage
input1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
input2 = 10
print(sum_non_prime(input1, input2))


lst=[3,15,2,4,6,7,9,11,8,10,12,13,15,17,19]
current_length=0
current_sum=0
max_length=0
longest_sums=[]

for num in lst:
    if num%2!=0:
        current_length+=1
        current_sum+=num
    else:
        if current_length>max_length:
            max_length=current_length
        elif current_length==max_length:
            longest_sums.append(current_sum)
            
        current_length=0



lst = [3,1,5,2,4,6,7,9,11,8,10,12,13,15,17,19]
lst = [1,3,5,7,9,11]
lst = [2,4,6,8,10]
lst = [1,2,3,4,5,6,7]
lst = [1,3,5,7,2,4,6,8,9,11]
lst = [2,4,6,8,1,3,5,7,9]
lst = [1,3,5,2,7,9,11,2,13,15,17]
lst = [2,4,6,8,11,10,12]
lst = []
current_length = 0
current_sum = 0
max_length = 0
longest_sums = []

for num in lst:
    if num % 2 != 0: #Check if the number is odd
        current_length += 1 
        current_sum += num
        
    else:
        if current_length > 0:
            if current_length > max_length:
                max_length = current_length
                longest_sums = [current_sum] #Reset list with new longest sum
            elif current_length == max_length:
                longest_sums.append(current_sum) #Append if same
                
                
             #Reset for next sequence
            current_length = 0
            current_sum = 0
             
# Check the last sequence in case the list ends with odd numbers
if current_length > 0:
   if current_length > max_length:
       max_length = current_length
       longest_sums = [current_sum]
   elif current_length == max_length:
       longest_sums.append(current_sum)
       
# Print the result
print(sum(longest_sums) if longest_sums else -1)
 input1="The Good The Bad and The Ugly"
words=input1.split()
words
char_lists=[list(word)for word in words]
char_lists
letter_counts=[len(chars)for chars in char_lists]
letter_counts
def total_sum(num):
    total=0
    while (num!=0):
        last_digit=num%10
        total=total+last_digit
        num//=10
    return total
total=[total_sum(num)for num in letter_count]
total
result=sum(total)
print("PIN",result)

def get_pin(input1):
    word=[]
    word=input1.split()
    total_length=sum(len(word)for word in input1)
    while total_length>=10:
        total_length=sum(int(digit)for digit in str(total_length))
    return total_length
get_pin("The Good The Bad and The Ugly")
get_pin("Wipro Technologies")
  
      
'''Adittion using strings :write a function that
takes two nus in string formate and forms a string containing
the sum of this two nos'''
def add_of_string(num1,num2):
    sum=str(int(num1)+int(num2))
    return sum
print(add_of_string(10,20))
    

'''Find the most frequently occuring digit in 
series '''
from collections import Counter
def most_frequent_digit(numbers):
    digit_count = Counter()
    for num in numbers:
        digit_count.update(str(num))
    max_frequency=max(digit_count.values())
    most_frequency=[int(digit) for digit,count in digit_count.items() if count==max_frequency]
    return most_frequency,max_frequency
numbers=[1234,1234,44678]
most_frequent,frequency=most_frequent_digit(numbers)
print(f'most frequent occuring digit:{most_frequent}')
      
  
'''To find palindrome if the digit  is not palindrom the remove 
then remove those digit print how many digits are removed '''
def find_digit_to_remove(input1):
    str_num=str(input1)
    #Check if n is already palindrom 
    if str_num == str_num[::-1]:
        return -1#no digit need to be removed
    #Try removing each digit one by one
    for i in range(len(str_num)):
        new_num = str_num[:i]+str_num[i+1:]
        #remove digit at index i
        if new_num == new_num[::-1]:
            return int(str_num[i])
    return -1 
print(find_digit_to_remove(12332))      
print(find_digit_to_remove(122332))      
print(find_digit_to_remove(133321))      
print(find_digit_to_remove(123))      


'''Array with n elements expcted to find
 sum of values that are present in non-prime
 indices of the array.
'''
def sum_non_prime(input1,input2):
    def is_prime(num):
        if num<2:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
            return True
    total=0
    for i in range(input2):
            if not is_prime(i):
                total+=input1[i]
    return total
input1=[10,20,30,40,50,60,70,80,90,100]
input2=10
print(sum_non_prime(input1,input2))

''' '''
lst=[3,1,5,2,4,6,7,9,11,8,10,12,13,15,17,19]
lst=[1,3,5,7,11,13]#only odd nos
lst=[0,2,4,6,8,9]#only even nos
lst=[1,2,3,4,5,6,7,8,9]#odd and even alternate
lst=[2,4,5,6,8]#single odd
curr_len=0
curr_sum=0
max_len=0
longest_sums=0
for num in lst:
    if num%2!=0:
        curr_len+=1
        curr_sum+=num
    else:
        if curr_len >0:
            if curr_len>max_len:
                max_len=curr_len
                longest_sums=[curr_sum]
            elif curr_len==max_len:
                longest_sums.append(curr_sum)
            curr_len=0
            curr_sum=0
if curr_len>0:
    if curr_len>max_len:
        max_len=curr_len
        longest_sums=[curr_sum]
    elif curr_len==max_len:
        longest_sums.append(curr_sum)
print(sum(longest_sums)if longest_sums else -1)
       

    
lst=[3,-1,-2,5,-3,-4,-5,6,-7,-8,-9,-10,-11,-12]
curr_len=0
curr_sum=0
max_len=0
longest_sums=0
for num in lst:
    if num<0:
        curr_len+=1
        curr_sum+=num
    else:
        if curr_len >0:
            if curr_len>max_len:
                max_len=curr_len
                longest_sums=[curr_sum]
            elif curr_len==max_len:
                longest_sums.append(curr_sum)
            curr_len=0
            curr_sum=0
if curr_len>0:
    if curr_len>max_len:
        max_len=curr_len
        longest_sums=[curr_sum]
    elif curr_len==max_len:
        longest_sums.append(curr_sum)
print(sum(longest_sums)if longest_sums else -1)
       

def minminusproduct(input1,input2):
    min_num=min(input1)
    subtracted_array=[x-min_num for x in input1]
    result_array=[x*min_num for x in subtracted_array]
    return result_array
input1=[4,8,2,6]
input1=[4,4,4,4]
input1=[4,8,2,6]
input2=0
minminusproduct(input1,input2)        











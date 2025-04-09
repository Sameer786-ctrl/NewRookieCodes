
    
''''Command line arguments'''
from sys import argv
print("The Fisrt argument",argv[1])
print("The Second argument",argv[2])

########################################
#process each word and computer ascii differnce

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


####################################################
#########################################################

sentence='world wide web'
sentence=sentence.upper()
words=sentence.split()
words
char_lists=[list(word)for word in words]

ascii_difference=[]
for word in char_lists:
    first_char=word[0]
    last_char=word[-1]
    ascii_first=ord(first_char)
    ascii_last=ord(last_char) 
    
    difference=abs(ascii_first-ascii_last)
    ascii_difference.append(difference)

for word,diff in zip(words, ascii_difference):
    print(f"Word:{word},Ascii difference: {diff}")
    
    
result=int("".join(map(str,ascii_difference)))
print(f"final output {result}")
    
####################
###########get mapped values
def get_mapped_values(letter):
    return ord(letter)-ord('A')+1

letters=['A','B','R','Y','Z']
for letter in letters:
    print(f"Letter:{letter}, Mapped Value:{get_mapped_values(letter)}")
    
    
print (ord('Y'))




###############
##########
def findStringCode(sentence): 
    sentence = sentence.upper() 
    words = sentence.split() 
    word_sums=[] 


    for word in words: 
        length = len(word) 
        total = 0 # Sum of ASCII differences 
        print(f"\nProcessing Word: {word}") 
        
        # Compute absolute differences using 
        for i in range(length // 2): 
            first_char = word[i] 
            last_char = word [length - 1 - i]
            first_val=ord(first_char)-ord('A')+1
            last_val=ord(last_char)-ord('A')+1
            diff=abs(first_val-last_val)
            print(f"Pair:({first_char},{last_char})->({first_val}-{last_val}={diff})")
            total+=diff
    
        #If word length is odd, add the middle charcter value
        if length%2==1:
            mid_char=word[length//2]
            mid_value=ord(mid_char)-ord('A')+1
            print(f"Middle Character: {mid_char}, Mapped Value:{mid_value}")
            total+=mid_value
            
        print(f"Total for '{word}':{total}")
        word_sums.append(str(total))
    
    #concatinate values to final result
    final_result=int("".join(word_sums))
    print(f"\n Final Output : {final_result}")
    return final_result
    
sentence="WORLD WIDE WEB"
findStringCode(sentence)



##################################3
##############################farah wipro tech 

input1="Wipro Technologies"

words=input1.split()
words
char_list=[ list(word) for word in words]

def cal_sum(num):
    total=0
    while num!=0:
        last_dig=num%10
        total=total+last_dig
        num=num//10
    return total

result=0
for i in range(2):
    result=result+cal_sum(len(char_list[i]))

print(result)


##########
#more optimized
input1="wipro technologies"
words=input1.split()
char_list=[list(word) for word in words]
letter_counts=[len(char) for char in char_list]
char_list
letter_counts

def total_sum(num):
    total=0
    while(num!=0):
        last_digit=num%10
        total=total+last_digit
        num=num//10
    return total
total=[total_sum(num) for num in letter_counts]
total
result=sum(total)
print('PIN',result)
 
#even more optimized

def get_pin(input1):
    words=input1.split()
    total_length=sum(len(word) for word in words)
    while total_length>=10:
        total_length=sum(int(digit) for digit in str(total_length))
    return total_length   
get_pin("Wipro Technologies")


    


####################
input1="hi hello sam"
words=input1.split()
total_length=sum(len(word) for word in words)
total_length
#####################3


""" encoding 3 strings 
anand was assigned

"""


s1='John'
s2='Johny'
s3='Janardhan'

lst=[s1,s2,s3]

for char in lst:
    n=len(char)
    
    if n%3==1:
        first=char[:1]
        middle=char[1:(n-1)]
        last=char[(n-1):]
    
    elif n%3==2:
        first=char[:2]
        middle=char[2:(n-2)]
        last=char[(n-2):]
        
    else:
        first=char[0:3]
        middle=char[3:6]
        last=char[6:9]
        
    print(f"First:-{(first)}, Middle:-{(middle)}, End:-{(last)}")

    print(f"First:-{''.join(first)}, Middle:-{''.join(middle)}, End:-{''.join(last)}")
        
 
##############################################3
####################################################

s1='John'
s2='Johny'
s3='Janardhan'

lst=[s1,s2,s3]
first_parts=[]
middle_parts=[]
end_parts=[]

for char in lst:
    n=len(char)
    
    if n%3==1:
        first=char[:1]
        middle=char[1:(n-1)]
        end=char[(n-1):]
        
    
    elif n%3==2:
        first=char[:2]
        middle=char[2:(n-2)]
        end=char[(n-2):]
    
    else:
        first=char[0:3]
        middle=char[3:6]
        end=char[6:9]
    
    first_parts.append(first)
    middle_parts.append(middle)
    end_parts.append(end)

output1=''.join(first_parts)
output2=''.join(middle_parts)
output3=''.join(end_parts).swapcase()

print(output1)
print(output2)
print(output3)

    #return (output1,output2,output3)   
    
    
    
##########for generalized and test cases
  
def encodeThreeStrings(s1, s2, s3):
    lst = [s1, s2, s3]
    fps, mps, eps = [], [], []
    
    for char in lst:
        n = len(char)
        
        if n % 3 == 1:
            first = char[:(n//3)]
            middle = char[(n//3):(2*(n//3))+1]
            last = char[(2*(n//3))+1:]
        
        elif n % 3 == 2:
            first = char[:(n//3)+1]
            middle = char[(n//3)+1:(2*(n//3))+1]
            last = char[(2*(n//3))+1:]
        
        else:
            first = char[:(n//3)]
            middle = char[(n//3):(2*(n//3))]
            last = char[(2*(n//3)):]
        
        fps.append(first)
        mps.append(middle)
        eps.append(last)
    
    output1 = ''.join(fps)
    output2 = ''.join(mps)
    output3 = ''.join(eps).swapcase()
    
    return output1, output2, output3

# Example usage
s1, s2, s3 = input("Enter first string: "), input("Enter second string: "), input("Enter third string: ")
result = encodeThreeStrings(s1, s2, s3)
print(result)


from datetime import date, timedelta
dt=date.today()-timedelta(5)
print("Current Date :",date.today())
print("5 day ago:",dt)

import time
print(time.asctime(time.strptime('2025 12 4','%Y %W %w')))









from datetime import date, timedelta

def all_sundays(year):
    sundays = []
    dt = date(year, 1, 1)  # Start from January 1st
    dt += timedelta(days=(7 - dt.weekday()))  # Move to the first Sunday

    while dt.year == year:
        sundays.append(dt)  # Store the Sunday in the list
        dt += timedelta(days=7)  # Move to the next Sunday

    return sundays  # Return the list of all Sundays

# Example usage:
print(all_sundays(2025))




from datetime import date, timedelta

def all_sundays(year):
    dt = date(year, 1, 1)  # Start on January 1st
    dt += timedelta(days=(6 - dt.weekday()))  # Move to first Sunday

    while dt.year == year:
        yield dt  # Instead of returning a full list, yield one Sunday at a time
        dt += timedelta(weeks=1)  # Move to next Sunday

# Example usage:
sundays = all_sundays(2025)  # This creates a generator, not a list
print(next(sundays))  # First Sunday
print(next(sundays))  # Second Sunday





print(dt.weekday())

print(6 - dt.weekday())
print(timedelta(days=(6 - dt.weekday())))
    
















































    
    
    
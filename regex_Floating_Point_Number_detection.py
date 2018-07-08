#Problem Statement:
#You are given a string . Your task is to verify that  is a floating point number.
#In this task, a valid float number must satisfy all of the following requirements:

#Number can start with +, - or . symbol. 
#For example: 
#✔ +4.50 
#✔ -1.0 
#✔ .5 
#✔ -.7 
#✔ +.4 
#✖  -+4.5

 #Number must contain at least  decimal value. 
#For example: 
#✖  12. 
#✔ 12.0  
# Number must have exactly one . symbol. 
# Number must not give any exceptions when converted using .

#Input Format
#The first line contains an integer , the number of test cases. 
#The next  line(s) contains a string .

#Output Format:
#Output True or False for each test case.

#Sample Input 0
#4
#4.0O0
#-1.00
#+4.54
#SomeRandomStuff

#Sample Output 0
#False
#True
#True
#False

-----------------------------------------------------------SOLUTION-----------------------------------------------------------------------

import re
x=int(input())
for i in range(x):
     matchobj=input()
     pattern=r'^[+|-]?\d*\.\d+$'  #a + or - sign in begining (0 or 1 occurance), a digit(0 or more), a dot(.), a digit(1 or more)at end
     m=bool(re.match(pattern,matchobj)) #convert match value into bool
     print(m)

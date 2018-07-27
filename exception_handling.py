#Task
#You are given two values a and b. 
#Perform integer division and print  a/b.

#Input Format
#The first line contains n, the number of test cases. 
#The next n lines each contain the space separated values of a and b.

#Output Format
#Print the value of a/b. 
#In the case of ZeroDivisionError or ValueError, print the error code.

#Sample Input
#3
#1 0
#2 $
#3 1

#Sample Output
#Error Code: integer division or modulo by zero
#Error Code: invalid literal for int() with base 10: '$'
#3

#----------------------------------------------------------SOLUTION---------------------------------------------------------------------
#solution 1
n=int(input())
for i in range(n):
    x,y = input().split(" ")
    try:
        num=int(x)//int(y)
    except ZeroDivisionError: 
        print("Error Code: integer division or modulo by zero")
    except ValueError as v:
        print("Error Code:", v)
    else:
        print(num)
        
#solution 2       
#for i in range(int(input())):
# try:
       # a,b=map(int,input().split())
       # print(a//b)
    #except Exception as e:
       # print("Error Code:",e)


#ABCXYZ company has up to  employees. The company decides to create a unique identification number (UID) for each of its employees. 
#The company has assigned you the task of validating all the randomly generated UIDs.A valid UID must follow the rules below:

#It must contain at least 2 uppercase English alphabet characters.
#It must contain at least 3 digits ( 0-9 ).
#It should only contain alphanumeric characters (a -z , A -Z  & 0 - 9).
#No character should repeat.
#There must be exactly 10 characters in a valid UID.

#Input Format:
#The first line contains an integer n, the number of test cases. 
#The next n lines contains an employee's UID.

#Output Format:
#For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

#Sample Input
#2
#B1CD102354
#B1CDEF2354

#Sample Output
#Invalid
#Valid

#Explanation
#B1CD102354: 1 is repeating → Invalid 
#B1CDEF2354: Valid

 

#--------------------------------------------------------------SOLUTION--------------------------------------------------------------------
import re
n=int(input())
for i in range(n):
    #split the input
    uid = input().strip()
    alnum=bool(uid.isalnum())
    upperclass=bool(re.search(r'(.*[A-Z]){2,}',uid)) #.* means any character except new line
    numero=bool(re.search(r'(.*[0-9]){3,}',uid))  #digit between 0-9
    if (len(uid) == 10):
        if (alnum and upperclass and numero): 
              if re.search(r'.*(.).*\1+.*',uid):#it searches any number of repeating characters in first group                                            #first group
                    print ('Invalid')
              else:
                    print ('Valid') 
        else:
            print ('Invalid')
    else:
        print ('Invalid')
         

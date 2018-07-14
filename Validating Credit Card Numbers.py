#You and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!
#A valid credit card from ABCD Bank has the following characteristics: 

#► It must start with a 4, 5 or 6 . 
#► It must contain exactly 16 digits. 
#► It must only consist of digits (0-9). 
#► It may have digits in groups of 4, separated by one hyphen "-". 
#► It must NOT use any other separator like ' ' , '_', etc. 
#► It must NOT have 4 or more consecutive repeated digits.

#Examples:
#Valid Credit Card Numbers
#4253625879615786
#4424424424442444
#5122-2368-7954-3214
#Invalid Credit Card Numbers
#42536258796157867       #17 digits in card number → Invalid 
#4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
#5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
#44244x4424442444        #Contains non digit characters → Invalid
#0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid

#Input Format:
#The first line of input contains an integer . 
#The next  lines contain credit card numbers.

#Output Format
#Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.

#Sample Input
#6
#4123456789123456
#5123-4567-8912-3456
#61234-567-8912-3456
#4123356789123456
#5133-3367-8912-3456
#5123 - 3567 - 8912 - 3456

#Sample Output
#Valid
#Valid
#Invalid
#Valid
#Invalid
#Invalid

#---------------------------------------------------------SOLUTION------------------------------------------------------------------
import re
N=int(input())
for i in range(N):
        cc=input()
       # check if it is starting with a 4,5 or 6 
        patternstart=re.search(r'^(4|5|6)',cc)
       #check if pattern has 4 groups of 4 digits(i.e total 16) with o/1 occurance of '-'
       #(?:a{6})* matches any multiple of 6'a' chars. so (?:\d{4}) matches multiple of 4 digits
        patternlen=re.search(r'(\d{16}|(\d{4}-){3}\d{4})$',cc)
        #now we use substitution and remove these "-"
        newcc=re.sub("-","",cc)
        #next we try to catch 3 or more occurances by \1 for first digit group
        patternrepeat=re.search(r'(\d)\1{3,}',newcc)  
        #if patternstart and len are proper and there are no consecutive repeats print valid
        if patternstart and patternlen:
            if not patternrepeat:
                   print("Valid")
            else:
                   print("Invalid")
        else:
                print("Invalid")

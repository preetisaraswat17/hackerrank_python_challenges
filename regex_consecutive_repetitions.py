#Task
#You are given a string . 
#Your task is to find the first occurrence of an alphanumeric character in  (read from left to right) that has consecutive repetitions.

#Input Format:
#A single line of input containing the string .

#Output Format:
#Print the first occurrence of the repeating character. If there are no repeating characters, print -1.

#Sample Input
#..12345678910111213141516171820212223

#Sample Output
#1

--------------------------------------------------------Solution-------------------------------------------------------------------

import re
pattern=r'([a-zA-Z0-9])\1+' #(alphanumeric)repetation(\1)
x=input()
m = re.findall(pattern,x)
print(m[0] if m else -1)


#Task 
#You are given a string . It consists of alphanumeric characters, spaces and symbols(+,-). Your task is to find all the substrings of 
#that contains 2 or more vowels. Also, these substrings must lie in between 2 consonants and should contain vowels only.

#Note : 
#Vowels are defined as: AEIOU and aeiou. 
#Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.

#Input Format:
#A single line of input containing string .

#Output Format
#Print the matched substrings in their order of occurrence on separate lines. If no match is found, print -1.

#Sample Input
#rabcdeefgyYhFjkIoomnpOeorteeeeet

#Sample Output:
#ee
#Ioo
#Oeo
#eeeee

#Explanation
#ee is located between consonant d and f. 
#Ioo is located between consonant k and m . 
#Oeo is located between consonant p and r. 
#eeeee is located between consonant t and t .

#----------------------------------------------------------SOLUTION-----------------------------------------------------------------------

import re
substring=input()
#use positive lookbehind & positive lookahead to find consonants around vowel with size 2 or more
pattern=r'(?<=[bcdfghjklmnpqrstvwxyz])[aeiou]{2,}(?=[bcdfghjklmnpqrstvwxyz])'
m=re.findall(pattern,substring,re.I) #re.I is for ignorecase(treats and upper and lowercase same)
#finally join all the groups in m by new line and return -1 if no groups  are found
if m:
   print('\n'.join(m))
else:
    print('-1')

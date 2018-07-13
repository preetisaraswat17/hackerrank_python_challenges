#Task 
#You are given a string s. Your task is to find the indices of the start and end of string k in s.

#Input Format:
#The first line contains the string S. 
#The second line contains the string k .

#Output Format:
#Print the tuple in this format: (start _index, end _index). 
#If no match is found, print (-1, -1).

#Sample Input
#aaadaa
#aa

#Sample Output
#(0, 1)  
#(1, 2)
#(4, 5)

#-----------------------------------------------------------SOLUTION---------------------------------------------------------------------

#search(String, pattern.start()+1) is used since we need to move the index to the right after each search.
import re
S=input()
k=input()
pattern=re.compile(r'('+k+')')
match = pattern.search(S)
if not match: print ("(-1, -1)")
while match:
    print((match.start(),match.end()-1))
    match = pattern.search(S,match.start() + 1)

       


#Neo has a complex matrix script. The matrix script is a  X  grid of strings. It consists of alphanumeric characters, spaces and symbols
#(!,@,#,$,%,&). To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo
#reads the column from top to bottom and starts reading from the leftmost column. If there are symbols or spaces between two alphanumeric
#characters of the decoded script, then Neo replaces them with a single space '' for better readability. Neo feels that there is no need
#to use 'if' conditions for decoding.
#Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

#Input Format
#The first line contains space-separated integers n (rows) and m  (columns) respectively. 
#The next n lines contain the row elements of the matrix script.

#Output Format
#Print the decoded matrix script.

#Sample Input 0
#7 3
#Tsi
#h%x
#i #
#sM 
#$a 
##t%
#ir!

#Sample Output 0
#This is Matrix#  %!

#------------------------------------------------------SOLUTION------------------------------------------------------------------------
#!/bin/python

import re

rows, cols = map(int, input().split())
lines=[]
characters = ""

for i in range(rows):
    lines.append(input())

for z in zip(*lines):
    characters += "".join(z)

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", characters))

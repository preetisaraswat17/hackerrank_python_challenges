#In this challenge, you will be given  integers,n  and m . There are n  words, which might repeat, in word group A. There are m words 
#belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence
#of m in group A. If it does not appear, print -1.

#Input Format
#The first line contains integers,n and m separated by a space. 
#The next n  lines contains the words belonging to group A. 
#The next m lines contains the words belonging to group B.

#Output Format
#Output m lines. 
#The ith line should contain the 1 -indexed positions of the occurrences of the ith word separated by spaces.

#Sample Input
#5 2
#a
#a
#b
#a
#b
#a
#b

#Sample Output
#1 2 4
#3 5

#Explanation
#'a' appeared  times in positions ,  and . 
#'b' appeared  times in positions  and . 
#In the sample problem, if 'c' also appeared in word group , you would print .




#--------------------------------------------------------Solution-----------------------------------------------------------------------

from collections import defaultdict
#we are taking default_factory as list so that if item is not present in lista then it returns a default value of a new empty list object

#since we need default value of -1 in list A we will make it as our default dict. i.e for every value in B if it is in A print index of A else print default value of -1
A = defaultdict(list)
B=[]

n, m = map(int,input().split())

#we take range from 1 else it will give 0 as first position and we need position of a in list and #not index
for i in range(1,n+1):
    A[input()].append(i) 

for i in range(1,m+1):
    B.append(input()) 


for i in B: 
    if i in A:
        #we need to map positions to str as it is in int and join cant be applied to int
        print (" ".join( map(str,A[i]) ))
    else:
        print ('-1')

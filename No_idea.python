#There is an array of  integers. There are also  disjoint sets, A and B , each containing  integers. 
#You like all the integers in set A and dislike all the integers in set B . Your initial happiness is 0. 
#For each  integer in the array, if i is in A, you add 1 to your happiness. If i is in B, you add -1  to your happiness.
#Otherwise, your happiness does not change. Output your final happiness at the end.

#Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

#Input Format:
#The first line contains integers m and n separated by a space. 
#The second line contains n integers, the elements of the array. 
#The third and fourth lines contain m integers, A and B , respectively.

#Output Format:
#Output a single integer, your total happiness.

#Sample Input:
#3 2
#1 5 3
#3 1
#5 7

#Sample Output:
#1

#Explanation:
#You gain 2 unit of happiness for elements  3 and 1 in set A. You lose 1 unit for 5  in set B. The element 7 in set B does not exist
#in the array so it is not included in the calculation.
#Hence, the total happiness is 2-1=1.


---------------------------------------------------------SOLUTION------------------------------------------------------------------------

#take input arrays
n,m=map(int,input().split())
myarray=[int(x) for x in input().split()]
A=set(map(int,input().split()))
B=set(map(int,input().split()))

happiness=0
#if myarray is a set we can find intersection of A and B with array and add happiness accordingly
#happiness+=len(myarray.intersection(A))
#happiness-=len(myarray.intersection(B))

#if my array is some other iterable we need to use membership function
for i in myarray:
    if (i in A):
        happiness+=1
    elif (i in B):
        happiness-=1
    else:
        happiness=happiness

#print happiness
print(happiness)
print(happiness)
        

#You are given a set  and  other sets. 
#Your job is to find whether set  is a strict superset of each of the  sets.
#Print True, if  is a strict superset of each of the  sets. Otherwise, print False.
#A strict superset has at least one element that does not exist in its subset.

#Example 
#Set {1,3,4} is a strict superset of set{1,3}. 
#Set {1,3,4}is not a strict superset of set {1,3,4}. 
#Set {1,3,4} is not a strict superset of set {1,3,5}.

#Input Format:
#The first line contains the space separated elements of set A . 
#The second line contains integer , n the number of other sets. 
#The next n lines contains the space separated elements of the other sets.

#Output Format:
#Print True if set A is a strict superset of all other  sets. Otherwise, print False.

#Sample Input:
#1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
#2
#1 2 3 4 5
#100 11 12
#Sample Output:
#False

#explanation:
#Set  is the strict superset of the set but not of the set because  is not in set . 
#Hence, the output is False.

---------------------------------------------------------------SOLUTION-------------------------------------------------------------------
A=set(map(int,input().split()))
supersets=[]
n=int(input())
for i in range(n):
    x=set(map(int,input().split()))
    if (A.issuperset(x)):
        supersets.append(True)
    else:
        supersets.append(False)
    i+=1
print(all(supersets))

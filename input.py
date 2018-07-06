#Task:
#You are given a polynomial p of a single indeterminate (or variable), x. 
#You are also given the values of  x and k. Your task is to verify if p(x)=k.

#Constraints 
#All coefficients of polynomial p are integers. 
#x and y are also integers.

#Input Format:
#The first line contains the space separated values of x and k. 
#The second line contains the polynomial p .

#Output Format:
#Print True if p(x)=k. Otherwise, print False.

#Sample Input
#1 4
x**3 + x**2 + x + 1

#Sample Output
#True

#--------------------------------------------------------------Solution----------------------------------------------------------------

x,k = map ( int , input().split())
s= input()
print (eval(s) == k)

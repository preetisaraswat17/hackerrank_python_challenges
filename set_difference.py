M=int(input())
#create empty sets
A=set()
B=set()
#update set A by splitting input in 2nd line
A.update([int(x) for x in input().split()])

N=int(input())
#update set B
B.update([int(k) for k in input().split()])
#find symmetric difference
diff=A.symmetric_difference(B)
#print multipke objects using * (else it will return a list)..seperated by \n..
print(*sorted(diff), sep="\n")

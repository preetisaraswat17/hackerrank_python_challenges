from itertools import combinations

#split the input
word, comsize=[x for x in input().split()]

#loop for i=1 then i=2...for i=0 it prints space
for i in range(1, int(comsize)+1):
    x=list(combinations(sorted(word),i))
    [print(*a, sep="") for a in x]
    i+=1

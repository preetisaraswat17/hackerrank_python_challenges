from itertools import combinations_with_replacement

#split input
word, size=[x for x in input().split()]
#print list of multiple objects with combinations_with_replacement for sorted word.seperated by ""
[print(*i,sep="") for i in list(combinations_with_replacement(sorted(word),int(size)))]

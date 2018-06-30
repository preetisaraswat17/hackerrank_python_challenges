#make an empty ser

stamps=set()
N=int(input())
#Add all succesive inputs to stamps using add
for i in range(N):
    stamps.add(input())
    
#print len of set stamps
print(len(stamps))

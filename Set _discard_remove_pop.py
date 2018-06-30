n = int(input())
#this maps all the input of set to integer
s = set(map(int, input().split()))

num=int(input())
for i in range(num):
      #split the input string
      x= [x for x in input().split()]
      if (x[0]=='pop'):
           s.pop()
      elif (x[0]=='discard'):
           s.discard(int(x[1]))
      elif (x[0]=="remove"):
           s.remove(int(x[1]))
      else:
           print("incorrect command")
      i+=1
print(sum(s))

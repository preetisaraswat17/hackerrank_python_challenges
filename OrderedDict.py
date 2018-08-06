#Task
#You are the manager of a supermarket. You have a list of  items together with their prices that consumers bought on a particular day. 
#Your task is to print each item_name and net_price in order of its first occurrence. item_name = Name of the item. 
#net_price = Quantity of the item sold multiplied by the price of each item.

#Input Format
#The first line contains the number of items, n. 
#The next n lines contains the item's name and price, separated by a space.

#Output Format
#Print the item_name and net_price in order of its first occurrence.

#Sample Input
#9
#BANANA FRIES 12
#POTATO CHIPS 30
#APPLE JUICE 10
#CANDY 5
#APPLE JUICE 10
#CANDY 5
#CANDY 5
#CANDY 5
#POTATO CHIPS 30

#Sample Output
#BANANA FRIES 12
#POTATO CHIPS 60
#APPLE JUICE 20
#CANDY 20

#Explanation

BANANA FRIES: 1 item so price 12  
POTATO CHIPS: 2 item so , Price: 30*2=60
APPLE JUICE: 2 item so , Price: 10*2=20
CANDY: 4 item so , Price: 5*4=20

#----------------------------------------Solution-----------------------------------------------------------

from collections import OrderedDict

n=int(input())
itemlist = OrderedDict()
for i in range (n):
     x=input().split(" ")
     itemname=" ".join(x[:-1])
     itemprice=int(x[-1])
     #if itemlist.get item is true i.e item is already in dict add the price for that item
     if itemlist.get(itemname):
          itemlist[itemname]+=itemprice
     else:
          itemlist[itemname] = itemprice
            
for k,v in itemlist.items():
    print(k,v)

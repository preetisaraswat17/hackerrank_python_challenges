#Task
#Raghu is a shoe shop owner. His shop has X number of shoes. He has a list containing the size of each shoe he has in his shop. 
#There are N number of customers who are willing to pay x amount of money only if they get the shoe of their desired size.
#Your task is to compute how much money Raghu earned.

#Input Format
#The first line contains N, the number of shoes. 
#The second line contains the N space separated list of all the shoe sizes in the shop.
#The third line contains n , the number of customers. 
#The next n lines contain the space separated values of the shoe size desired by the customer and x, the price of the shoe.

#Output Format
#Print the amount of money earned by raghu.

#Sample Input
#10
#2 3 4 5 6 8 7 6 5 18
#6
#6 55
#6 45
#6 55
#4 40
#18 60
#10 50

#Sample Output
#200

#Explanation
#Customer 1: Purchased size 6 shoe for $55. 
#Customer 2: Purchased size 6 shoe for $45. 
#Customer 3: Size 6 no longer available, so no purchase. 
#Customer 4: Purchased size 4 shoe for $40. 
#Customer 5: Purchased size 18 shoe for $60. 
#Customer 6: Size 10 not available, so no purchase.

#Total money earned => 55+45+40+60=200


#----------------------------------------------------------SOLUTION--------------------------------------------------------------------

from collections import Counter
num_shoes=int(input())
#counter counts the count no. of shoes available for each sizes
shoes=Counter(map(int, input().split(" ")))
num_customer=int(input())

#make an empty list of profit
profit=[]
for _ in range(num_customer):
      size, price=map(int,input().split(" "))
      #we can also use if size in shoes but in that case it also counts the 0 occurance of shoes so we use greater than 0 condition
      if shoes[size]>0:
         #append price and reduce shoe count by 1
         profit.append(price)
         shoes[size] -= 1
      else:
          pass
print(sum(profit))

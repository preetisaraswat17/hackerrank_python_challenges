Task
#The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English,
#some have subscribed to only French and some have subscribed to both newspapers.
#You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the 
#French newspaper. The same student could be in both sets.
#Your task is to find the total number of students who have subscribed to at least one newspaper.' ' '

total_english=int(input())
#create set for students roll num with english newspaper
E=set([int(x) for x in input().split()])
total_french=int(input())
#create set for students roll num with french newspaper
F=set([int(x) for x in input().split()])
#create union of students with atleast 1 newspaper subscription
Subscribers=E.union(F)
print(len(Subscribers))

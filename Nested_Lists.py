#Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any
#student(s) having the second lowest grade. Note: If there are multiple students with the same grade, order their names alphabetically 
#and print each name on a new line.

#Input Format
#The first line contains an integer, n, the number of students. 
#The 2n subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains
#their grade. There will always be one or more students having the second lowest grade.

#Output Format
#Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names 
#alphabetically and print each one on a new line.

#Sample Input 0
#5
#Harry
#37.21
#Berry
#37.21
#Tina
#37.2
#Akriti
#41
#Harsh
#39

#Sample Output 0
#Berry
#Harry

#---------------------------------------------------------------Solution----------------------------------------------------------------

num=int(input())
#first create an empty list where we will be storing nested lists[names, marks]
student=[]
for i in range(0,num):
              student.append([input(),float(input())])
#first create a list of marks from student list then convert it to set toremove duplicate values
#now agin convert it to a list because sets cant be sorted and we need sorted items. since #duplicates are already removed any second element will be the second lowest
second_lowest_grade=sorted(list(set([marks for name, marks in student])))[1]
#create a sorted list of names from student where marks are equal to second_lowest
x=sorted([names for  names,marks in student if marks==second_lowest_grade])

# these elements can be printed with join or simply by print statement with * and \n as seperator
print(*x ,sep="\n")
        

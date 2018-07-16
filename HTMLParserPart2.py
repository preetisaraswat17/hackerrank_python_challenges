#Task
#You are given an HTML code snippet of n lines. Your task is to print the single-line comments, multi-line comments and the data.

#Print the result in the following format:
#>>> Single-line Comment  
#Comment
#>>> Data                 
#My Data
#>>> Multi-line Comment  
#Comment_multiline[0]
#Comment_multiline[1]
#>>> Data
#My Data
#>>> Single-line Comment:  
#Note: Do not print data if data == '\n'.

#Input Format
#The first line contains integer n, the number of lines in the HTML code snippet. The next n  lines contains HTML code.

#Output Format
#Print the single-line comments, multi-line comments and the data in order of their occurrence from top to bottom in the snippet.

#Format the answers as explained in the problem statement.

#Sample Input
#4
#<!--[if IE 9]>IE9-specific content
#<![endif]-->
#<div> Welcome to HackerRank</div>
#<!--[if IE 9]>IE9-specific content<![endif]-->

#Sample Output
#>>> Multi-line Comment
#[if IE 9]>IE9-specific content
#<![endif]
#>>> Data
#Welcome to HackerRank
#>>> Single-line Comment
#[if IE 9]>IE9-specific content<![endif]

#-----------------------------------------------------------Solution-------------------------------------------------------------------

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
           multi='\n'
           if multi in data:
                    print(">>> Multi-line Comment ")
                    print(data)
                    #we can also split the data by new line and then print it
                    #comment=[x for x in data.split('\n')]
                    #print(*comment, sep='\n')
                  
           else:
                   print(">>> Single-line Comment ")
                   print(data)
                   
    def handle_data(self, data):
        if (data=='\n'):
            pass
        else:
             print (">>> Data")
             print(data)
        
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#You are given an HTML code snippet of n lines. Your task is to detect and print all the HTML tags, attributes and attribute values.
#Print the detected items in the following format:

#Tag1
#Tag2
#-> Attribute2[0] > Attribute_value2[0]
#-> Attribute2[1] > Attribute_value2[1]
#-> Attribute2[2] > Attribute_value2[2]
#Tag3
#-> Attribute3[0] > Attribute_value3[0]

#The -> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute 
#value. The > symbol acts as a separator of attributes and attribute values.If an HTML tag has no attribute then simply print the name of
#the tag.

#Note: Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags (<!-- Comments -->). Comments can be 
#multiline. All attributes have an attribute value.

#Input Format
#The first line contains an integer n , the number of lines in the HTML code snippet.
The next n lines contain HTML code.

#Output Format
#Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the snippet.
#Format your answers as explained in the problem statement.

#Sample Input
#9
#<head>
#<title>HTML</title>
#</head>
#<object type="application/x-flash" 
#  data="your-file.swf" 
#  width="0" height="0">
 # <!-- <param name="movie" value="your-file.swf" /> -->
 # <param name="quality" value="high"/>
#</object>

#Sample Output

#head
#title
#object
#-> type > application/x-flash
#-> data > your-file.swf
#-> width > 0
#-> height > 0
#param
#-> name > quality
#-> value > high

#----------------------------------------------------------SOLUTION-------------------------------------------------------------------

from html.parser import HTMLParser

#make a class with appropriate methods
class Myparser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if (attrs!=None):
            for ele in attrs:
                print("->",ele[0],">",ele[1])
    def handle_endtagtag(self, tag):
         print(tag)
    def handle_startendtag(self, tag, attrs):
        print(tag)
        if (attrs!=None):
            for ele in attrs:
                print("->",ele[0],">",ele[1])
    def handle_comment(self,data):
        pass
    

#take input and instantiate class
n=int(input())
parser=Myparser()

#feed the data
for i in range(n):
     parser.feed(input())
    

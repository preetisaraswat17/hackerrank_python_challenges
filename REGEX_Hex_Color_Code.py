#CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).
#Specifications of HEX Color Code

■ It must start with a '#' symbol.
■ It can have 3 or 6 digits.
■ Each digit is in the range of 0 to F. ( 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E and F).
■  A-F letters can be lower case. (a,b,c,d,e and f are also valid digits).

#Examples
#Valid Hex Color Codes
#FFF 
#025 
#F0A1FB 

#Invalid Hex Color Codes
#fffabg
#abcf
#12365erff

#You are given  lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.
#CSS Code Pattern
#Selector
#{
#	Property: Value;
#}

#Input Format:
#The first line contains n , the number of code lines.The next n lines contains CSS Codes.

#Output Format:
#Output the color codes with '#' symbols on separate lines.

#Sample Input
#11
#BED
#{
 #   color: #FfFdF8; background-color:#aef;
 #  font-size: 123px;
 #   background: -webkit-linear-gradient(top, #f9f9f9, #fff);
#}
#Cab
#{
 #   background-color: #ABC;
 #   border: 2px dashed #fff;
#}

#Sample Output
#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff

#----------------------------------------------------SOLUTION-------------------------------------------------------------------------
import re
n=int(input())
for i in range(0,n):
    pattern=re.findall(r':?.(#[0-9a-f]{6}|#[0-9a-f]{3})',input(),re.I)
    #understanding the pattern here
    #:? 0/1 occurance of : as in colors:
    #. space or any other character, required so that it doesnt selected #bed or #cab in start
    #(#[0-9a-f]{6}|  6 letter hex code with # or
    #[0-9a-f]{3})    3 letter hex code with #
    if pattern:
        print(*pattern,sep='\n')
        

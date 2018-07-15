#Input Format:
#The first line contains a single integer, n , denoting the number of email address. Each n line  of the  subsequent lines contains a 
#name and an email address as two space-separated values following this format:
#name <user@email.com>

#Output Format
#Print the space-separated name and email address pairs containing valid email addresses only. Each pair must be printed on a new line
#in the following format:
#name <user@email.com>
#You must print each valid email address in the same order as it was received as input.

#Sample Input
#2  
#DEXTER <dexter@hotmail.com>
#VIRUS <virus!@variable.:p>
#Sample Output

#DEXTER <dexter@hotmail.com>

#----------------------------------------------------------SOLUTION--------------------------------------------------------------------

import email.utils
import re
n=int(input())
for i in range(0,n):
    #parseaddr takes 1 i/p email and returns a tuple (name, mailaddress) with 2 arguments
     emails=email.utils.parseaddr(input())
     #split the name and emailaddress
     name=emails[0]
     mailaddr=emails[1]  
     #use character classes in pattern for email format
     pattern=re.compile(r'^[a-zA-Z][\w\.\-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$')
     #understanding the pattern here:
     #^[a-zA-z]    username starts with an English alphabetical character, 
     #[\w|\.|\-]*   & consist of one or more alphanumeric characters, -,., and _. 
     #@[a-zA-z]*  The domain and extension contain only English alphabetical characters.
     #\.[a-zA-z]{1,3} The extension is 1,2 or 3  characters in length
     match=pattern.match(mailaddr)
     #print(bool(match))
     if match:
        #formataddre takes tuple(name, emailaddress) and returns 1 result email
        print(email.utils.formataddr((name,mailaddr)))
   

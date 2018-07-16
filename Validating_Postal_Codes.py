#A valid postal code  have to fullfil both below requirements:
#1) must be a number in the range from 1000000 to 999999 inclusive.
 #2) must not contain more than one alternating repetitive digit pair.
#Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit
#pair is formed by two equal digits that have just a single digit between them.

#For example:
#121426 # Here, 1 is an alternating repetitive digit.
#523563 # Here, NO digit is an alternating repetitive digit.
#552523 # Here, both 2 and 5 are alternating repetitive digits.

#Your task is to provide two regular expressions regex_integer_in_range and regex_alternating_repetitive_digit_pair. Where:
#regex_integer_in_range should match only integers range from 1000000 to 999999 inclusive
#regex_alternating_repetitive_digit_pair should find alternating repetitive digits pairs in a given string.
#Both these regular expressions will be used by the provided code template to check if the input string  is a valid postal code

#Input Format:
#Locked stub code in the editor reads a single string denoting n from stdin and uses provided expression and your regular expressions 
#to validate if  is a valid postal code.

#Output Format
#You are not responsible for printing anything to stdout. Locked stub code in the editor does that.

#Sample Input:
110000

#Sample Output :
False
Note: 
A score of  will be awarded for using 'if' conditions in your code. 
You have to pass all the testcases to get a positive score.

#----------------------------------------------------------solution-------------------------------------------------------------------

import re
P = input()

regex_integer_in_range = r"^[1-9]\d{5}$"	#we need $ at end else it will match in a greedy pattern(at leat 6 digits) (we need exact 6)
# it takes a digit and then use look forward assertion to find out if there is any digit and then the repetation of digit captured by first
#group alternatively we can also use (\d)(?=.\1)
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	 

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


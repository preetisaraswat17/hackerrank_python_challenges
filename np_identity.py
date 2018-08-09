#Task
#Your task is to print an array of size X with its main diagonal elements as 1's and 0's everywhere else.

#Input Format
#A single line containing the space separated values of  m and n. 
#m denotes the rows. 
#n denotes the columns.

# Output Format
# Print the desired X array.

#Sample Input
#3 3

#Sample Output
#[[ 1.  0.  0.]
# [ 0.  1.  0.]
# [ 0.  0.  1.]]

#-------------------------------------Solution------------------------------------------------------------------

import numpy as np
n,m=map(int,input().split(" "))
#for extra white spaces sign can be set to " ","+","-"
np.set_printoptions(sign=' ')
print(np.eye(n,m,k=0)) #k=1 for 1 above diagonal k=-2 second lower diagonal for value 1

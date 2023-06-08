"""

###  To know contents of directory :

=>> os module provides listdir() to list out the contents of the specified directory. 
	It won't display the contents of sub directory

"""

import os 

# print(os.listdir('yy'))

print(os.listdir('.'))   # =>> . ==> current working directory



"""

The above program display contents of current working directory but not contents of sub
directories.


###

If we want the contents of a directory including sub directories then we should go for
walk() function.

"""

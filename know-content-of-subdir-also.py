"""

### To know contents of directory including sub directories:

We have to use walk() function
[Can you please walk in the directory so that we can aware all contents of that directory]



os.walk(path,topdown=True,onerror=None,followlinks=False)

It returns an Iterator object whose contents can be displayed by using for loop

path-->Directory path. cwd means .
topdown=True --->Travel from top to bottom
onerror=None --->on error detected which function has to execute.
followlinks=True -->To visit directories pointed by symbolic links

"""


import os 

for dirpath, dirnames, filenames in os.walk('e:\\') :          #  .  =>> for the current working directory
	print('current working directory path : ', dirpath)
	print('directories : ', dirnames)
	print('file names : ', filenames)
	print()


"""

==> To display contents of particular directory, we have to provide that directory name
	as argument to walk() function.

os.walk("directoryname")

"""


### difference between listdir() and walk() functions =>> 
"""
In the case of listdir(), we will get contents of specified directory but not sub directory
contents. But in the case of walk() function we will get contents of specified directory and
its sub directories also.
"""
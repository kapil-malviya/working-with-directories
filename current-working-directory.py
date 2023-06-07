"""

Working with Directories =>> 

it is very common requirement to perform operations for directories like : 
  - To know current working directory
  - To create a new directory
  - To remove an existing directory
  - To rename a directory
  - To list contents of the directory etc...


==>> to perform these operations, python provides inbuilt module os, 
	  which contains several functions to perform directory related operations


"""

# to know current working directory =>> 


import os 

cwd = os.getcwd()
print('Current Working Directory : ', cwd)



"""   output =>> 

Current Working Directory :  D:\directories

"""
"""

### To create a sub directory in the current working directory :



import os 

new = os.mkdir('xx')     # xx =>> new sub directory name
print('sub dir created successfully...')




# ==>  a new folder created inside current folder

"""



### To create a new sub directory in mysub directory :

"""

import os 

new = os.mkdir('xx/xyz')     # here folder *xx* compulsory, it should be already available
print('sub dir created successfully inside my dir...')



  # =>> folder *xyz* created inside *xx* folder 

"""



### To create multiple directories like sub1 in that sub2 in that sub3 : 



import os 

mul_new = os.makedirs('sub1/sub2/sub3/sub4')
print('sub dir created and so on ....')


# ==>> folder inside folder created...
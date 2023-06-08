"""
### To remove/delete the directories : 




import os

os.rmdir('xx/xyz')        # only folder *xyz* will be removed and not folder *xx*
print('task done : folder *xyz* removed')


"""


### To remove multiple directories in the path : 


import os

os.removedirs('sub1/sub2/sub3/sub4')
print('all four directories removed successfully...')


# all folders deleted successfully...
### How to get information about a File ==> 

"""
We can get statistics of a file like size, last accessed time, last modified time etc by using
	stat() function of os module.

stats = os.stat("abc.txt")

The statistics of a file includes the following parameters :

st_mode==>Protection Bits
st_ino==>Inode number
st_dev===>device
st_nlink===>no of hard links
st_uid===>userid of owner
st_gid==>group id of owner
st_size===>size of file in bytes
st_atime==>Time of most recent access (last access time)
st_mtime==>Time of most recent modification
st_ctime==> Time of most recent meta data change

"""

"""

import os 

stats = os.stat('dummy-file.txt')
print(stats)



st_atime, st_mtime and st_ctime returns the time as number of milli seconds since Jan 1st
1970 , 12:00AM. 

By using datetime module in that module fromtimestamp() function, we can get exact
date and time.

"""



import os 
import datetime

stats = os.stat('dummy-file.txt')
print('file size in bytes : ', stats.st_size)
print('files last accessed time : ', datetime.datetime.fromtimestamp(stats.st_atime))
print('files last or recent modified time : ', datetime.datetime.fromtimestamp(stats.st_mtime))



"""

file size in bytes :  138
files last accessed time :  2023-05-19 14:59:20.832836
files last or recent modified time :  2023-05-19 14:55:24.853668

"""

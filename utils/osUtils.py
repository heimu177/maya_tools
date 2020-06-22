import os
from shutil import copyfile
# from distutils.dir_util import copy_tree

newDir = 'e:/dir1/dir2'

# if not os.path.exists(newDir):
#     os.makedirs(newDir)

# copy_tree(newDir, newDir.replace('dir1', 'dir1Changed'))

# file = open(newDir + '/demo.txt', 'a')
# file.write('Hello World!')
# file.close()

# copyfile(newDir + '/demo.txt', newDir + '/demo2.txt')

contents = [os.path.join(newDir, file) for file in os.listdir(newDir)]
print contents

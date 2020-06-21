import os
from distutils.dir_util import copy_tree

newDir = 'e:/dir1/dir2'

# if not os.path.exists(newDir):
#     os.makedirs(newDir)

copy_tree(newDir, newDir.replace('dir1', 'dir1Changed'))

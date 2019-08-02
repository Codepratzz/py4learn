# The shutil Module
# The shutil (or shell utilities) module has functions to let you copy, move,
# rename, and delete files in your Python programs. To use the shutil functions,
# you will first need to use import shutil.

import os
import shutil

import send2trash

old_path = 'C:\\Users\\quasar\\Downloads\\Music'
new_path = 'C:\\Users\\quasar\\Downloads\\Music_bk'
shutil.rmtree(new_path)
os.chdir('C:\\')
shutil.copytree(old_path, new_path)

#  Calling os.unlink(path) will delete the file at path.
# • Calling os.rmdir(path) will delete the folder at path. This folder must be
# empty of any files or folders.
# • Calling shutil.rmtree(path) will remove the folder at path, and all files
# and folders it contains will also be deleted
# import os  A goodway to delete a file
# for filename in os.listdir():
# if filename.endswith('.rxt'):
# #os.unlink(filename)
# print(filename)

baconFile = open('C:\\Users\\quasar\\Downloads\\Music\\bacon.txt', 'a')  # creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('C:\\Users\\quasar\\Downloads\\Music\\bacon.txt')

for folderName, subfolders, filenames in os.walk(new_path):
    print(os.walk(new_path))
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

    print('')

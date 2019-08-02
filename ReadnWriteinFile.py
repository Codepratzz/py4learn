# single period (“dot”) for a folder name is shorthand for “this directory.” Two periods (“dot-dot”)
# means “the parent folder.” import os. Whenever your programs need to work with files, folders, or file paths,
# you can refer to the short examples in this section.

import os

path = 'C:\\Users\\quasar\\Dropbox\\Apps\\MYmutualfundinvestment'
print(os.path.abspath('..'))
# If you need a path’s dir name and base name together, you can just call os.path.split() to get a tuple
# value with these two strings, like so:
print(os.path.split(os.path.abspath('.')))
print(os.listdir(os.path.dirname(path)))  # dir-returns the path of the dir

# If I want to find the total size of all the files in this directory, I can use os.path.getsize() and
# os.listdir() together.
totalSize = 0
for filename in os.listdir(path):
    totalSize = totalSize + os.path.getsize(os.path.join(path, filename))
print(totalSize)

# There are three steps to reading or writing files in Python.
# 1. Call the function to return a object. open() File
# 2. Call the or method on the object. read() write() File
# 3. Close the file by calling the method on the object close() File

helloFile = open('C:\\Users\\quasar\\Dropbox\\Apps\\MYmutualfundinvestment\\a.txt', 'a')
# print(helloFile.read())
# print(helloFile.readline())
helloFile.writelines('my name is baba yaga\n'
                     'my name is nbaba dasdw2\n')
helloFile.close()
helloFile = open('C:\\Users\\quasar\\Dropbox\\Apps\\MYmutualfundinvestment\\a.txt')
print(helloFile.readlines())

# Instead, you need to open it in “write plaintext” mode
# or “append plaintext” mode, or write mode and append mode for short.

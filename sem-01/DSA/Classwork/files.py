fp = open('log.txt', 'w+')
fp.write('one world\n')
fp.write('two\n')
fp.write('four\n')

text = ['five\n', 'six\n']
fp.writelines(text)

fp.seek(10) # changes the location of the pointer
print(fp.read())

fp.seek(0)
for line in fp:
    print(line, end='')

fp.close()

# As an alternative to writing fp.close(), you can do
with open('log.txt', 'w+') as fp:
    # ... do whatever you want to do in the file here ...
    # ...
    pass
# you do not need to close the file anymore


'''
Doing open('../log.txt', 'w+') instead of just open('log.txt', 'w+') creates 
/ accesses log.txt not in the current folder, but in the parent of the current 
folder. You can extend it further by doing stuff like 
open('../parent_folder/log.txt', 'w+'), which opens it in the parent of the 
parent folder, and so on.
'''

'''
Difference between 'r+' and 'w+':
If no file is present, 'w+' creates a new file, while 'r+' throws an error.
'''

'''
Different types of file reading mechanisms:
fp.read() # reads entire document
fp.readline() # reads a single line
fp.readlines() # reads all lines and stores them as different strings
'''

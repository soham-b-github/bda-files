# Check if a number is present in the list or not

l = [12, 35, 6, 8, 99, 45, 67]
key = 45

def find(l, key):
    for e in l:
        if e == key:
            print("Exists")
            return
    print("Does not exist")

find(l, key)

# Go through API of .join() in python strings

fp = open('test.log', 'w+')
fp.write("welcome to programming")
fp.seek(8)
line = fp.readline()
print(line)
fp.close()

if __name__ == '__main__':
 with open('log.txt','w+') as f:
    f.write('hello, how are you this morning?\n')
    f.write('hello, how are you? second line\n')
    f.write('hello, how are you? 3rd line\n')
    f.writelines(['5\n','6\n','7'])
    

 print('written into the file')    

 fp = open('log.txt','r')

 text = fp.read(6)
 print(text)

 print(f"position is {fp.tell()}")

#  fp.seek(5,1)
 text = fp.readline()
 print(text)




# text = fp.readline()
# print(text)

# text = fp.readlines()
# for i in text:
#  print(i)

# for line in fp:
#     print(line)


 fp.close()


 a = {'1','2','3','6','7','8'}

 print(''.join(map(str,a)))


def summation(a=5,b=6):
    return a+b

with open('output.bin', 'wb') as fp:
    data = b'abc123 welcome to the binary mode of operations '
    fp.write(b'012345')
    # fp.seek(10,2)
    print(data)
    fp.write(data)

with open('output.txt', 'rb') as fp:
    data = 'abc123 welcome new to the binary mode of operations'
    print(data)
    # fp.seek(-9,2)
    print(fp.readline())

print(summation())
print(summation(b=15,a=100))


a = {1,2,3,4,5,6,6,7}
b = {'x','y','z','a', 1, 2, 4}
print(a & b)
print(f"{a - b} difference set")
print(f"{a ^ b} symmetric difference set")

c = {1:'one',2:'two','3':'three'}
c[3] = 'new_three'
print(c)
print(c[3])

a.update(b)
print(a)




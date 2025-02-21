'''
Task: Read 3 elements from 'input.txt': two numbers and an operator.
Use the 3 elements to perform the operation and print the result on the next
line.

Numbers can be any real numbers, while operators can be *, //, +, -, **, /.
'''

fp = open('input.txt', 'r+')

elements = fp.readline().split()
num1, num2 = float(elements[0]), float(elements[1])
operator = elements[2]
ans = 0

if operator == '*':
    ans = num1 * num2
elif operator == '//':
    ans = num1 // num2
elif operator == '+':
    ans = num1 + num2
elif operator == '-':
    ans = num1 - num2
elif operator == '**':
    ans = num1 ** num2
elif operator == '/':
    ans = num1 / num2

fp.write('\n')
fp.write(str(ans))
fp.close()

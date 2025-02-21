# Write a program to take a list as input and print distinct elements
L = list(map(int, input("Enter elements of list: ").split()))

occurred = []
for e in L:
    if e not in occurred:
        occurred.append(e)

print("Unique list =", occurred)

repeated = []
for e in L:
    if L.count(e) > 1 and e not in repeated:
        repeated.append(e)

print("List with repeated numbers only =", repeated)



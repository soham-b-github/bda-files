# character -> ChArAcTeR

s = input("Enter a word: ")
res = ""
for i in range(len(s)):
    if i % 2 == 0:
        res += s[i].upper()
    else:
        res += s[i].lower()

print("result =", res)


res2 = ""
for i in range(len(s)):
    if i % 2 == 0:
        if ord(s[i]) >= 97:
            res2 += chr(ord(s[i]) - 32)
        else:
            res2 += s[i]
    else:
        if ord(s[i]) < 97:
            res2 += chr(ord(s[i]) + 32)
        else:
            res2 += s[i]
print("result2 =", res2)

# ~ 🐄 = input()
# ~ print("cow =", 🐄)

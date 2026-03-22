# Find the sum of odd digits in a number
n = input()
s = 0
for d in n:
    if int(d) % 2 != 0:
        s += int(d)
print(s)
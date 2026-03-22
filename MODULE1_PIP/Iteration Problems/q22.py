# Difference between sum of odd and even digits
n = input()
odd = even = 0
for d in n:
    if int(d) % 2 == 0:
        even += int(d)
    else:
        odd += int(d)
print(odd - even)
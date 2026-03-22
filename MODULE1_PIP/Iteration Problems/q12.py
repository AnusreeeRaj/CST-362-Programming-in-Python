# Check whether a number is prime or not
n = int(input())
flag = True
if n <= 1:
    flag = False
for i in range(2, n):
    if n % i == 0:
        flag = False
        break
print("Prime" if flag else "Not Prime")
# Check whether a number is Armstrong or not
n = int(input())
s = 0
temp = n
digits = len(str(n))
while temp > 0:
    d = temp % 10
    s += d ** digits
    temp //= 10
print("Yes" if s == n else "No")
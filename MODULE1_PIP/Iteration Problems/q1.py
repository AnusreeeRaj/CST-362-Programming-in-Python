# Find the sum of the first N natural numbers using iteration
n = int(input())
s = 0

for i in range(1, n+1):
    s += i

print(s)
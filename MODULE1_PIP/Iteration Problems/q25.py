# Sum of series: 1 + 2/2! + 3/3! + ... + n/n!
n = int(input())
fact = 1
s = 1
for i in range(2, n+1):
    fact *= i
    s += i / fact
print(s)
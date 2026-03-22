# Sum of series: 1 + x + x^2/2! + x^3/3! + ... + x^n/n!
x = int(input())
n = int(input())
fact = 1
s = 1
for i in range(1, n+1):
    fact *= i
    s += (x**i) / fact
print(s)
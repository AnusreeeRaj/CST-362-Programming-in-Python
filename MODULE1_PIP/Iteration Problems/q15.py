# Print Armstrong numbers between two limits
l, u = map(int, input().split())
for n in range(l, u+1):
    s = 0
    digits = len(str(n))
    temp = n
    while temp > 0:
        d = temp % 10
        s += d ** digits
        temp //= 10
    if s == n:
        print(n, end=" ")
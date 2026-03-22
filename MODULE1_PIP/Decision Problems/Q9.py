# Determine the nature of roots of a quadratic equation
a, b, c = map(int, input().split())
d = b*b - 4*a*c
if d > 0:
    print("Real and distinct")
elif d == 0:
    print("Real and equal")
else:
    print("Complex")
# Check whether a number is completely divisible by another number
a, b = map(int, input().split())
print("Yes" if a % b == 0 else "No")
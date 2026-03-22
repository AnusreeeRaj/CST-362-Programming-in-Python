# Find the large digit in a two-digit number
n = int(input())
print(max(n//10, n%10))
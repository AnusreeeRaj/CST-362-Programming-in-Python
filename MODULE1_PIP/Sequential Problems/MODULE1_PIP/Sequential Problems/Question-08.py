# 8. Swap 2 numbers using a temporary variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
temp = a
a = b
b = temp
print(a, b)

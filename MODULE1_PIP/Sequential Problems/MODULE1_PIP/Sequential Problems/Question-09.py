# 9. Swap 2 numbers without using a temporary variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print(a, b)
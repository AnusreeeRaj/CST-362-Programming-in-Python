# 6. Area and perimeter of a triangle ( p=a+b+c, a=sqrt(s(s-a)s-b)(s-c))
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
p = a + b + c
s = p / 2
print(s)
a = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(a)
print(p)

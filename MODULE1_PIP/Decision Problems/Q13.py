# Find grade based on percentage
p = float(input())
if p >= 90:
    print("O")
elif p >= 85:
    print("A+")
elif p >= 80:
    print("A")
elif p >= 70:
    print("B+")
elif p >= 60:
    print("B")
elif p >= 50:
    print("C")
elif p >= 45:
    print("P")
else:
    print("F")
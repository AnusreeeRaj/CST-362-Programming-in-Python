# 7. Convert seconds to hours : minutes : seconds
s = int(input("Enter seconds: "))
h = s // 3600
m = (s % 3600) // 60
s = s % 60
print(h, ":", m, ":", s)

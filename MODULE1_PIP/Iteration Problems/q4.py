# Print first N terms of an arithmetic progression
a = int(input("First term: "))
d = int(input("Common difference: "))
n = int(input("Number of terms: "))
for i in range(n):
    print(a + i*d, end=" ")
# Print even numbers in reverse order starting from N
n = int(input())
for i in range(n, -1, -1):
    if i % 2 == 0:
        print(i, end=" ")
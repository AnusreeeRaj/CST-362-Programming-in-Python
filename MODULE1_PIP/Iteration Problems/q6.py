# Print even numbers from a starting number to an ending number
a, b = map(int, input().split())
for i in range(a, b+1):
    if i % 2 == 0:
        print(i, end=" ")
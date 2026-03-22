# Numbers between 100 and 200 divisible by 3 but not by 4
for i in range(100, 201):
    if i % 3 == 0 and i % 4 != 0:
        print(i, end=" ")
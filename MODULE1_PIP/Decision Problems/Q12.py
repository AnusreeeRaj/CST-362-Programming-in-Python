# Calculate electricity bill based on units consumed
u = int(input())
if u <= 200:
    bill = u * 0.5
elif u <= 400:
    bill = 100 + (u - 200) * 0.65
elif u <= 600:
    bill = 230 + (u - 400) * 0.80
else:
    bill = 425 + (u - 600) * 1.25
print(bill)
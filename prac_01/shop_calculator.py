items = int(input("Number of Items: "))
total = 0
while items < 0:
    print("Invalid number of items!")
    items = int(input("Number of Items: "))

for i in range(0, items):
    price = int(input("Price of item: "))
    total = total + price

if total > 100:
    total = total * 0.9

print("Total Price for {0} items is ${1:.2f}".format(items, total))

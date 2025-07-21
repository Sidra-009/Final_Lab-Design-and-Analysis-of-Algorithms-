# Input Product Names and Prices
products = []
n = int(input("How many products do you want to enter? "))

for i in range(n):
    name = input(f"Enter name of product {i + 1}: ")
    price = float(input(f"Enter price of {name}: "))
    products.append((name, price))

# Search Product by Name
search_name = input("\nEnter the product name to search: ")

found = False
for index, (name, price) in enumerate(products):
    if name.lower() == search_name.lower():
        print(f"\nProduct Found!")
        print(f"Name: {name}")
        print(f"Price: {price}")
        print(f"Position in the list: {index + 1}")
        found = True
        break

if not found:
    print("\nProduct not available in the list.")

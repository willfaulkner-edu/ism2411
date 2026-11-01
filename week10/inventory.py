#1. The most surprising thing about python list is how adjustable index is especially using negative numbers to count backwards. Its also interesting how list methods put data right in place.
#2. In my senior computer class sorting through large sets of data manually would take lots of time. Writing a python script makes it easier to filter numbers and calculate averages automatically.

# Exercise 1
inventory = ['pen', 'notebook', 'stapler', 'tape', 'marker']
print("Exercise 1:")
print(inventory)
print("Number of items:", len(inventory))
print("-" * 30)

# Exercise 2
middle_index = len(inventory) // 2
print("Exercise 2:")
print("First item:", inventory[0], "(positive)", inventory[-5], "(negative)")
print("Last item:", inventory[4], "(positive)", inventory[-1], "(negative)")
print("Middle item:", inventory[middle_index], "(positive)", inventory[middle_index - len(inventory)], "(negative)")
print("-" * 30)

# Exercise 3
print("Exercise 3:")
print("First three items:", inventory[:3])
print("Last two items:", inventory[-2:])
print("Every other item:", inventory[::2])
print("-" * 30)

# Exercise 4
print("Exercise 4:")
inventory.append('envelope')
print("After append:", inventory)

inventory.remove('tape')
print("After remove:", inventory)

inventory.sort()
print("After sort:", inventory)
print("-" * 30)

# Exercise 5
print("Exercise 5:")
coords = (48.7128, -74.8068)
try:
    coords[0] = 99
except TypeError as e:
    print("TypeError caught, explanation printed:", e)
    print("Tuples are immutable, which is useful for coordinates because it ensures geographic data cannot be accidentally modified.")

print("Original coords unchanged:", coords)
print("-" * 30)

# Exercise 6
print("Exercise 6:")
sales = [100, 250, 75, 480, 200]
total_sales = sum(sales)
count_sales = len(sales)
avg_sales = total_sales / count_sales
print(f"Total: {total_sales} | Average: {avg_sales} | Count: {count_sales} | Best: {max(sales)} | Worst: {min(sales)}")
print("-" * 30)

# Exercise 7
print("Exercise 7:")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.90, 2))

print("Original:", prices)
print("Discounted:", discounted)
print("-" * 30)

# Exercise 8
print("Exercise 8:")
sales_data = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for s in sales_data:
    if s > 300:
        high_sales.append(s)

high_avg = sum(high_sales) / len(high_sales)
print("High sales:", high_sales)
print(f"Count: {len(high_sales)} | Avg: {high_avg:.2f}")
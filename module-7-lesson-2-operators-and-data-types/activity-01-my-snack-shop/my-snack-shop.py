# Step 2: Snack details using four data types
snack_name = "Chocolate Bar"   # str
price = 1.50                   # float
quantity = 10                  # int
is_available = True            # bool

print("Snack name:", snack_name, "| type:", type(snack_name))
print("Price:", price, "| type:", type(price))
print("Quantity:", quantity, "| type:", type(quantity))
print("Available:", is_available, "| type:", type(is_available))

# Step 3: Arithmetic operators
total_stock_value = price * quantity
sale_price = price - 0.25
double_stock = quantity * 2

print("Total stock value:", total_stock_value)
print("Sale price:", sale_price)
print("Double the stock:", double_stock)

# Step 4: Comparison operators
print("Is price under $2?", price < 2)
print("Is quantity greater than 5?", quantity > 5)
print("Is price exactly $1.50?", price == 1.50)

# Step 5: String operations
shop_name = "Quick" + " " + "Bites"
print("Shop name:", shop_name)
print("Number of letters in snack_name:", len(snack_name))
print("First letter of snack_name:", snack_name[0])

# Step 6: Swap two prices using a temp variable
price_a = 1.50
price_b = 3.00

print("Before swap: price_a =", price_a, "| price_b =", price_b)

temp = price_a
price_a = price_b
price_b = temp

print("After swap: price_a =", price_a, "| price_b =", price_b)
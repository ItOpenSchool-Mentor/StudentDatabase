products = ["Shirts", "Shoes", "Watch"]
prices = [999, 1999, 2999]

for prod, price in zip(products, prices):
    print(f"{prod} costs ₹{price}")

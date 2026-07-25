order_amount = int(input("Enter order amouont"))

# print(f"Order amount type is '{type(order_amount)}")
delivery_fee = 0 if order_amount >300 else 30

print(f"delivery fee is {delivery_fee}")
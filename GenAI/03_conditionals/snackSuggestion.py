# if conditions

snack = input("Enter what you want : ").lower()

print(f"you have entered {snack}")

if snack == "samosa" or snack == "burger":
    print(f"your order has been confirmed")
else:
    print(f"item not available. Only Samosa or burger is available.")
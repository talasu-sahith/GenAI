# Upcasting 
# functions used bool()
isBoiling = True
stir_count = 5
total_grams = stir_count +isBoiling #Upcasting

print(f"total grams : {total_grams}")

milk_present = None
print(f"is Milk present : {bool(milk_present)}") #bool function convert text or int to boolean. 0 = false and 1 = true

# Logical

isWaterHot = True
teaAdded = False

canServe = isWaterHot and teaAdded

print(f"can we serve the tea : {canServe}")
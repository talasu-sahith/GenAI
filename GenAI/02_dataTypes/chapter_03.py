# Integer
# operators tested + , - , / , // - for integer part of decimal , ** - exponential calculation just like ^
blackTea = 16
ginger = 4

totalGrams = blackTea +ginger
print(f"total tea in grams :{totalGrams}")

remaining_grams = blackTea - ginger
print(f"remaining grams :{remaining_grams}")

totalCost = 18
NumItems = 7

Each = totalCost / NumItems

Revised = totalCost //NumItems

print(f"cost of each Item : {Each}")
print(f"cost of each Item : {Revised}")

leftOver = totalCost % NumItems

print(f"Lefover cost : {leftOver}")
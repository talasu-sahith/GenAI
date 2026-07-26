# return is of 3 types
# 1. return one value
# 2.return early
# 3.return multiple values

def chai_order():
    return "chai" , "sugar" # example for multiple return values

item1 , item2 = chai_order()

print(f"item 1 : {item1}")
print(f"item 2 : {item2}")


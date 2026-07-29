# Example of code for List Comprehension
# [Expression for item in iterable if condition]
# [coffee for coffee in menu if "Coffee" in coffee]
# Compare the above two statements for matching syntax - Expressions , item , iterable is menu , condition 

menu = ["Black Coffee" , "Cappuchino Coffee" , "Black Tea" , "Ginger Tea"]

coffee_menu = [coffee for coffee in menu if "Coffee" in coffee]

print(f"{coffee_menu}")
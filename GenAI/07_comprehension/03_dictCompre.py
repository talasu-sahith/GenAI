# Dictionary and sets both looks same - Objects. Only diff is dict deals with key:value pairs
# {expression for item in iterable if condition} - here when the expression in key value pair it is a dictionary Comprehension

biriyani_Prices_inr = {
    "Dum" : 70,
    "Mixed": 400,
    "Zaffrani": 220
}

# .items will let us access both key an value instead of only values in an object
prices_dollar = { type:price/80 for type , price in biriyani_Prices_inr.items() }

print(prices_dollar)
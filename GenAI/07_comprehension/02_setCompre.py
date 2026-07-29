# Code for Set comprehension

favourite_briyanis= ["Special biriyani" , "Zaffrani briyani" , "Dum Biriyani" , "Special biriyani" , "Fry Peice Biriyani"]

# set compre without if condition return unique elements

unique_biriyanis = { biriyani for biriyani in favourite_briyanis if len(biriyani) <11 }

# { biriyani for biriyani in favourite_briyanis if len(biriyani) <11 } this is standard compre set

print(unique_biriyanis)

# another example to filter values of an object

menu = {
    "Mutton": ["Zaffrani" , "Mixed"],
    "Chicken" : ["Dum" , "Mixed" , "Fry Peice"],
    "Mix":["Fish" , "Mixed"]
}

# from the above I want to fetch uniqu values of biriyani types

unique_types = {type for meat in menu.values() for type in meat}
# .values() will allow you to loop into each meat item array , 

print(f"{unique_types}")
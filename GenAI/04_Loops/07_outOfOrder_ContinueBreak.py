# continue keyword enables us to continue the loop
# break keyword helps us to break the loop

menu =["Ginger" , "OutofStock","lemon","Discontinued" , "Tualsi"]

for flavour in menu:
    if flavour == "OutofStock" :
        print(f"{flavour} is found")
        continue
    elif flavour == "Discontinued":
        break
    print(f"{flavour} is found")

print("Out of Loop")
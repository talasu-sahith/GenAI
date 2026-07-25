# input : "small" , "medium" , "large"
# condition: small = 10 , medium = 15 , large = 20
# invalid  = "unknown Cupsize"

varInput = input("Please enter cup size").lower()

if varInput == "small":
    print(f"Small costs : 10")
elif varInput == "medium":
    print(f"Medium costs : 15")
elif varInput == "large":
    print(f"Large costs : 20")
else:
    print(f"Unknown Cup Size")
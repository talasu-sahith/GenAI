# Pure Impure
# recursive
# Lambdas (anonymus functions)

def PureChai(): # Example of pure function
    chai_type = "ginger"
    print(f"ordered {chai_type}")

PureChai()

chaiCups = 4

def ImpureChai(): # example of impure function
    global chaiCups
    chaiCups += 2
ImpureChai()
print(f"numbe rof cups : {chaiCups}")

def RecursiveChai(n): # Example of recursive function
    print(f"{n}")
    if n== 0:
        print("All cups Served")
    else:
        return RecursiveChai(n-1)

RecursiveChai(3)

 # Example of lambda Function 
chaiTypes = ["ginger" , "masala" , "kadak" , "masala" ,"lemon"]

strongChai = list(filter(lambda chai: chai !="masala" , chaiTypes))

print(f"{strongChai}")
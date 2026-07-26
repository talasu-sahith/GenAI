# global is a key work that acces sthe variable from the global such as variables initialized outside the functions and any changes will update at global

chaiType = "ginger"

def chai_order():
    # global chaiType
    chaiType = "lemon"

chai_order() 

print(f"Chai type is {chaiType}") #this prints lemon as the chaitype is getting updated to lemon inside the chai order function and the function is getting called. If comment line 6 "global" you will see printing ginger
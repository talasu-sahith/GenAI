# nonlocal keyword helps us to access the variable initialized inside its parent function

def chai_order():
    chaiType = "ginger"
    def chai_counter():
        nonlocal chaiType
        chaiType = "kesar"
    chai_counter()
    print(f"chai type : {chaiType}")

chai_order() # this prints kesar because of the line 7 - nonlocal. eventhough print statement access chai type ginger it is getting updated inside chai counter  to kesar
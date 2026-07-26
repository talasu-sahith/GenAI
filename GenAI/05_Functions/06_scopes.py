# fourtypes of scopes - Local , Enclosing , Global , Build in

def chaiOrder():
    chaiType = "masala" # this is local scope
    print(f"Local : {chaiType}") 

def chai_counter():
    chaiType = "Lemon" #Local Scope
    def printOrder():
        chaiType = "ginger" # Enclosing Scope
        print(f"Enclosing : {chaiType}")
    printOrder()
    print(f"Local : {chaiType}")

chai_counter()
chaiType = "black" # Global Scope
print(f"Global : {chaiType}")
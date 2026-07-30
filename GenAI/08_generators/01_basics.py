# generator uses the keyword - yield , next
# diff between function and generator is function uses return keyword and generator uses Yield keyword


def serveChai():
    yield "Masala Chai"
    yield "Ginger chai"
    yield "Lemon chai"

chai = serveChai()

# for cup in chai:
#     print(cup)

def getCups():
    yield "cup 1"
    yield "cup 3"
    yield "cup 2"

getCup = getCups()

print(next(getCup)) # next key word needs to be used to yield and view the items in a generator
print(next(getCup))

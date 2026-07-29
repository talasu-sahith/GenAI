# Generator - (expression for item in iterable if condition)
# only diff is generator uses () parenthesis instead of [] array braces.
# both consume lists / arrays
#  It is memory efficient. List consumes whole memory at once but generator consumes in stream

Values = [8 , 14, 7, 2, 23]

final_value = ( value for value in Values if value <9 ) # this will not retun any value in print but allows us to consume

sum_values = sum(value for value in Values if value<9)

print(f"{final_value}")
print(f"{sum_values}") 

# This way it avoid to write a lot amount of code like storing the value into a variable and looping the array such things
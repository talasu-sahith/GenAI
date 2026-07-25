# string manipulations - Indexing , Slicing and Encoding/Decoding

order = "Ginger tea"
orderedBy = "Angel Priya"

print(f"Excuse me {orderedBy} , your order for {order} is ready to deliver")

sampleString = "Agentic AI and Python"

print(f"First 5 letter : {sampleString[0:5:1]}")
print(f"Start from 5 to end : {sampleString[4::]}")
print(f"reverse a string : {sampleString[::-1]}")

label_text = "Special text ☺"
encoded_text = label_text.encode("utf-8")
print(f"encoded text : {encoded_text}")
print(f"encoded text : {label_text}")

decoded_text = encoded_text.decode("utf-8")
print(f"encoded text : {decoded_text}")

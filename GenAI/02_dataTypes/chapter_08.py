# List operations - append , extend , remove , pop (removes last element of array) , sort , reverse , min , max , insert

list1 = ["mouse" , "keyboard" , "charger" , "laptop"]
list1.append("mousepad")
print(f"Append operation : {list1}")

list2 = ["water" , "coffee"]
list1.extend(list2)
print(f"Extend operation : {list1}")

list1.remove("water")
print(f"remove operation : {list1}")

list1.pop()
print(f"Pop Operation :{list1}")

list1.sort()
print(f"sort operatoion : {list1}")

list3 = [1,12,54,2,33]
print(f"minimmum in list 3 : {min(list3)}")
print(f"miximmum in list 3 : {max(list3)}")

list1.insert(3 , "monitor")
print(f"insert operation : {list1}")

baseLiquid = ["whisky" , "rum"]
mixer = ["water" , "soda"]

baseLiquid.extend(mixer)
print(f"blended : {baseLiquid}")

blend = baseLiquid+mixer
print(f"blended using operator overloading : {blend}")

mixer2 = mixer * 2
print(f"doublemix : {mixer2}")

utensils =bytearray( b"Glasses")
study  = utensils.replace(b"Glass",b"Class")
print(f"updated bytearray : {study}")
deviceStatus = "active"
temp = 38

if deviceStatus =="active":
    if temp>35:
        print("High temperature")
    else:
        print("temperature is normal")
else:
    print("Devic eis offline")
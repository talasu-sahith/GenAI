# enumerate function generates tuples along with index.
# enumerate(array , start:1) - using this second parameter gives index to start form 1

menu = ["Asian" , "russian" , "thai" , "spanish", "latin" , "japanese"]

for idx , item in enumerate(menu, start=1):
    print(f"{idx} : {item} chai")
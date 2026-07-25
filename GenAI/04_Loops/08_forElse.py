# for else loop is used as a try catch case

Info = [("Ram", 24),("Sita" , 21), ("Laxman" , 23) , ("Hanuman" , 18)]

for name , age in Info:
    if age>18 :
        print(f"{name} is eligible to vote")
        break

else:
    print(f"no one is eligible")
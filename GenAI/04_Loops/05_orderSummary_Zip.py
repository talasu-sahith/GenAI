# Zip function takes 2 parameters of arrays of same length and return tuples.
# zip(array1,array2) -> returns [(ar1,ar2),(ar1,ar2),(ar1,ar2)]

names = ["rama" , "sita" , "laxman" , "hanuman"]
bill = [100,900,300,400]

for amount , name in zip(bill,names):
    print(f"{name} paid {amount} rupees ")
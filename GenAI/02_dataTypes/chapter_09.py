# sets - uniion indicate using pipe operator '|' and intersection indicate using and operator '&' 

hardDrinks = {"whisky" , "rum" , "vodka" , "sting"}
softDrinks = {"coke" , 'fanta' , "Limca" , "sting"}

allDrinks = hardDrinks | softDrinks #union
print(f"all drinks would be l; {allDrinks}") 

commondrinks = hardDrinks & softDrinks #intersection
print(f"common drinks : {commondrinks}")

dieHardDrinks = hardDrinks - softDrinks #A - A intersection B
print(f"alcohols : {dieHardDrinks}")

print(f" is Limca in hard srinks : {'Limca' in hardDrinks}")

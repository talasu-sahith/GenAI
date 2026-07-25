# tuples
# in conditioning works in tuples

masalaSpices = ("cardamon","cinnamon" , "dalchin")

(spice1 , spice2 , spice3)  = masalaSpices

print(f" Masala Spices are {spice1 },{ spice2 },{ spice3}")

gingerratio, cardamonRatio = 2,7

print(f"ginger ratio : {gingerratio} , cardamon ratio {cardamonRatio}")

gingerratio,cardamonRatio = cardamonRatio , gingerratio #swap ratios
print(f"ginger ratio : {gingerratio} , cardamon ratio {cardamonRatio}")

print(f" is cardamon available in masalaspices {'cardamon' in masalaSpices}")
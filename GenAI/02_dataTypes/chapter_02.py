# functions used set() , .add() , id()
spice_mix = set()
print(f"initial id of sugar mix : {id(spice_mix)}")

spice_mix.add("ginger")

print(f"items of spicemix : {spice_mix}")
print(f"id after adding into spicemix : {id(spice_mix)}")
spice_mix.add("lemon")
print(f"items of spicemix : {spice_mix}")
print(f"id after adding into spicemix : {id(spice_mix)}")

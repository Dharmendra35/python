# set is mutable
spice_mix = set()
print(f"Initial spice_mix id: {id(spice_mix)}")

spice_mix.add("Ginger")
spice_mix.add("Cardamom")
print(f"After spice_mix id: {id(spice_mix)}")
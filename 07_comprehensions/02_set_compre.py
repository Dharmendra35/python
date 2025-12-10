favourite_chais = ["masala chai", "kadak chai", "masala chai", "kadak chai"]

unique_chai = {chai for chai in favourite_chais if len(chai) > 5}
print(unique_chai)


recipies = {
  "Masala Chai" : ["ginger", "cardmom", "clove"],
  "Elaichi Chai" : ["cardmom", "milk"],
  "Spicy Chai" : ["ginger", "back pepper", "clove"]
}

# this will take the unique of every values

unique_spices = {spice for ingredients in recipies.values() for spice in ingredients}
print(unique_spices)
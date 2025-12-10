flavours = ["Ginger", "Out of Stock", "lemon", "Discontinued", "sugar"]

for item in flavours:
  if(item == "Out of Stock"):
    continue
  if(item == "Discontinued"):
    print(f"{item} found")
    break
  print(f"Valid item found {item}")

print(f"loop end")
for token in range(1, 11):
  print(f"Serving chai to Token #{token}")

orders = ["Ram", "Shyam", "Hema", "Monu", "Sinu"]

for name in orders:
  print(f"Chai ordered by {name}")

ingredients = ["sugar", "chai", "ginger", "milk"]
for inx, item in enumerate(ingredients, 1):
  print(f"{inx}: {item}")


names = ["Hitesh", "Meela", "Hinu", "kalua"]
bills = [23, 45, 67, 6]

for name, amount in zip(names, bills):
  print(f"{name} paid {amount} rupees")
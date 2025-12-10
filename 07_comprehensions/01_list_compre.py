menu = [
  "malsala-chai",
  "Iced Lemon tea",
  "Green tea",
  "Iced Peach tea",
  "Ginger tea"
]

iced_tea = [tea for tea in menu if "Iced" in tea]
iced_tea_len = [tea for tea in menu if (len(tea) > 10) > 12]
print(iced_tea)
  
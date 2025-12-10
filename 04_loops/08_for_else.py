staff = [("Amit", 16), ("Sara", 17), ("Raj", 15)]

for name, age in staff:
  if(age >= 18):
    print(f"{name} is eligible to vote")
    break
else:
  print("No one is eligible to vote")
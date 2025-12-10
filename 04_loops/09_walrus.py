# value = 15
# remainder = 15 % 4

# if remainder:
#   print(f"{value} is not divisible by {remainder}")

# value = 15

# if(remainder := value % 4):
#   print(f"{value} is not divisible")


available_sizes = ["small", "medium", "large"]

if(requested_size := input("Tell us about your cup size: ")) in available_sizes:
  print(f"this is your {requested_size} cup")
else:
  print(f"size is unavailabe {requested_size}")
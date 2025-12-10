order_amount = int(input(f"Enter your amount: "))
if order_amount >= 300:
  print(f"Free delivery applied")
else:
  print(f"Your delivery fee is : 30 rupees")


delivery_fee = 0 if order_amount >= 300 else 30
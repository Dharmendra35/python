def make_chai():
  #return "Here is your masala chai"
  print("Here is your masala chai")


#return_val = make_chai -> this will hold the val
#print(return_val) -> contains none if func not have return type

def sold_cups():
  return 120

total = sold_cups()
print(total)

def chai_status(cups_left):
  if cups_left == 0:
    return "No chai available"
  return "take your chai"

print(chai_status(0))
print(chai_status(5))

def chai_report():
  return 100, 20

sold, remaining, _ = chai_report()

print("Sold: ", sold)
print("Remaining: ", remaining)
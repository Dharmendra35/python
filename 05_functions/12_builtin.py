def chai_flavor(flavor="masala"):
  """Return the flavor of chai."""
  return flavor

print(chai_flavor.__doc__)
print(chai_flavor.__name__)

help(len)

def generate_bills(chai = 0, samosa = 0):
  """
  Docstring for generate_bills
  
  :param chai: Description
  :param samosa: Description
  """
  total = chai * 10 + samosa * 12
  return total, "Thank you for visiting!"
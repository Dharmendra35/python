# chai = "Ginger chai"

# def prepare_chai(order):
#   print("preparing ", chai)

# prepare_chai(chai)
# print(chai)

chai = [1, 2, 4]

def edit_chai(cup):
  cup[1] = 43

edit_chai(chai)
print(chai)

def make_chai(tea, milk, sugar):
  print(tea, milk, sugar)


make_chai("Darjeeling", "Yes", "Low") #positional
make_chai(tea = "Darjeeling", milk = "Yes", sugar="Low") #keywords

def special_chai(*ingredients, **extras):
  print("Ingredients", ingredients)
  print("Extras", extras)

special_chai("Cinamonn", "Cardmom", sweetener="Honey", foam="yes")

# Ingredients ('Cinamonn', 'Cardmom') -> will tuple => args
# Extras {'sweetener': 'Honey', 'foam': 'yes'} -> will dictionary  => kwargs 

def chai_order()
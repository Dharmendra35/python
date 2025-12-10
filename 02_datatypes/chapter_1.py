#immutable -> reference can be change not val

sugar_amount = 12
print(f"Initial sugar: {sugar_amount}")

sugar_amount = 20
print(f"Second Initial sugal: {sugar_amount}")

print(f"Id of 12: {id(12)}")
print(f"Id of 20: {id(20)}")
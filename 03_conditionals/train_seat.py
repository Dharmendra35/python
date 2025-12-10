seat_type = input(f"Choose your seat type (sleeper / Ac / general): ").lower()

match seat_type:
  case "sleeper":
    print(f"no a, but bed will be there!")
  case "ac":
    print(f"ac and bed both will be there!")
  case "general":
    print(f"just seat will be there!")
  case _:
    print(f"Invalid seat type!")
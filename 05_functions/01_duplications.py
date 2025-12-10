def print_order(name, chai_type):
  print(f"{name} ordered the {chai_type}")

print_order("Shilla", "Mashala-chai")

def fetch_data():
  print("fetching the data")

def summarise_data():
  print("summarising the data")

def prepare_report():
  fetch_data()
  summarise_data()

prepare_report();
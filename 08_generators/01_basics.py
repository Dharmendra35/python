def serve_chai():
  yield "Cup 1: Masala chai"
  yield "Cup 2: Ginger chai"
  yield "Cup 3: Elaichi chai"

stall = serve_chai()
for cup in stall:   # for each cup, serve_chai called 
  print(cup)

def get_chai_list():
  return ["cup 1", "cup 2", "cup 3"]

def get_chai_gen():
  yield "cup 1"
  yield "cup 2"
  yield "cup 3"

chai = get_chai_gen()
print(chai)


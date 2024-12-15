import random
def dice(sides):
  return random.randint(1,sides)
def health():
  return dice(6) * dice(8)
print("Character Stats Generator")
while True:
  name = input("Name your warrior: ")
  print("Their health is: ",health(),"hp")
  print()
  again = input("Do you want to create another character? ")
  if again == "yes":
    continue
  else:
     print(name,"is dead")
     break
  

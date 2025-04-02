# Write code below 💖

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

q1 = int(input(f"\nDo you like Dawn or Dusk?: \n1) Dawn. \n2) Dusk. \n1. or 2.:"))

if q1 == 1:
  Gryffindor =+ 1
  Ravenclaw =+ 1
elif q1 == 2:
  Hufflepuff =+ 1
  Slytherin =+ 1
else:
  print("Wrong input.")

print(f"\n{Gryffindor = }, {Ravenclaw = }, {Hufflepuff = }, {Slytherin = }")

q2 = int(input(f"\nWhen I’m dead, I want people to remember me as:\n1) The Good. \n2) The Great. \n3) The Wise. \n4) The Bold. \n1. 2. 3. or 4.:"))

if q2 == 1:
  Hufflepuff += 2
elif q2 == 2:
  Slytherin += 2
elif q2 == 3:
  Ravenclaw += 2
elif q2 == 4:
  Gryffindor += 2
else:
  print("Wrong input.")

print(f"\n{Gryffindor = }, {Ravenclaw = }, {Hufflepuff = }, {Slytherin = }")

q3 = int(input(f"\nWhich kind of instrument most pleases your ear?\n1) The violin. \n2) The trumpet. \n3) The piano. \n4) The drum. \n1. 2. 3. or 4.:"))

if q3 == 2:
  Hufflepuff += 4
elif q3 == 1:
  Slytherin += 4
elif q3 == 3:
  Ravenclaw += 4
elif q3 == 4:
  Gryffindor += 4
else:
  print("Wrong input.")

print(f"\n{Gryffindor = }, {Ravenclaw = }, {Hufflepuff = }, {Slytherin = }")

if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
  print(f"\nThe house winer is Gryffindor.\n")
elif Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
  print(f"\nThe house winer is Ravenclaw.\n")
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
  print(f"\nThe house winer is Hufflepuuff.\n")
else:
  print(f"\nThe hose winer is Slytherin.\n")
  
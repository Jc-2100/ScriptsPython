# Sorting Hat Harry Potter films

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print('Q1) Do you like Dawn or Dusk?')
print('    1) Dawn')
print('    2) Dusk')

selection = int(input())

if selection == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif selection == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print('Wrong input.')

print('Q2) When I´m dead, I want people to remember me as:')
print('    1) The Good')
print('    2) The Great')
print('    3) The Wise')
print('    4) The Bold')

selection = int(input())

if selection == 1:
    Hufflepuff += 1
elif selection == 2:
    Slytherin += 1
elif selection == 3:
    Ravenclaw += 1
elif selection == 4:
    Gryffindor += 1
else:
    print('Wrong input.')

print('Q3) Which kind of instrument most pleases your ear?')
print('    1) The violin')
print('    2) The trumpet')
print('    3) The piano')
print('    4) The drum')

selection = int(input())

if selection == 1:
    Slytherin += 1
elif selection == 2:
    Hufflepuff += 1
elif selection == 3:
    Ravenclaw += 1
elif selection == 4:
    Gryffindor += 1
else:
    print('Wrong input.')

if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
    print('Gryffindor!')
elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
    print('Ravenclaw!')
elif Hufflepuff >= Slytherin:
    print('Hufflepuff')
else:
    print('Slytherin')

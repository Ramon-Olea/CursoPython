

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets)
planeta= input("ingrese el planeta:  ")
index = planets.index(planeta)



print("planeta más cercano al sol que " + planeta )
print( planets[0:index])

print('planeta más lejos al sol que ' + planeta)
print(planets[index + 1:])
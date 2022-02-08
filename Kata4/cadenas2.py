# Datos con los que vas a trabajar
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"


distancia= gravity * 1000
# Creamos el título

subject = 'Ejercicio 2 the moon'




plantilla = f"""{subject.title() }
planeta: {planet} 
Gravedad en {planet}: {distancia} m/s2 
"""
print(plantilla)

subject = 'Ejercicio 2 the Marte'
name = "Marte"
gravity = 0.00143 # in kms
planet = "Ganímedes"

plantilla = f"""{subject.title() }
planeta: {planet} 
Gravedad en {planet}: {distancia} m/s2 
"""
print(plantilla)

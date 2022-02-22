planeta = {
    'nombre': 'Marte',
    'lunas': 2
}

print(f'{planeta["nombre"]} tiene {planeta["lunas"]} lunas')

planeta['circunferencia (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}

print(f'{planeta["nombre"]} tiene una  circunferencia polar de {planeta["circunferencia (km)"]["polar"]}')
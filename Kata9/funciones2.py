def reporte_cohete_2(hora_prelanzamiento, tiempo_recorrido, tanque_interno, tanque_externo, nombredestino):
    
    return f"""
    Viaje:
    Viaje espacio: {nombredestino}
    Tiempo total del  viaje  {hora_prelanzamiento+tiempo_recorrido} minutos
    Total de {tanque_interno+tanque_externo} combustible 
    """
    
print(reporte_cohete_2(2, 54, 1200, 1750, "Luna"))

def reporte_c(destino, *minutes, **fuel_reservoirs):
    return f"""
    Viaje espacio {destino}
    Tiempo total del  viaje : {sum(minutes)} minutos
    Total de combustible : {sum(fuel_reservoirs.values())}
    """

print(reporte_c("Luna", 32, 11, 55, t_in=1200,t_ex=1750))

def mission_report(destination, *minutes, **fuel_reservoirs):
    
    main_report = f"""
    Mision a {destination}
    Tiempo total de viaje: {sum(minutes)} minutes
    Total de combustible: {sum(fuel_reservoirs.values())}
    """
    
    for tank_name, gallons in fuel_reservoirs.items():
        main_report += f"""Galon {tank_name} --> {gallons} sobrante | """
    
    return main_report

print(mission_report("Luna", 32, 11, 55, principal=1200, externo=1750))
def reporte_cohete(tanque1,tanque2,tanque3):
    
    total_prom=(tanque1+tanque2+tanque3)/3

    return f"""
    Reporte combustibles:
    Total Promedio: {total_prom}%
    Tanque1: {tanque1}%
    Tanque2: {tanque2}%
    Tanque3: {tanque3}% 
    """

print(reporte_cohete(40,53,65))

def prom(values):
    
    total = sum(values)
    numero_tanques = len(values)
    return total / numero_tanques

prom([46,52,48])

def reporte_cohete(tanque1,tanque2,tanque3):
    
    return f"""
    Reporte combustibles:
    Total Promedio: {prom([tanque1,tanque2,tanque3])}%
    Tanque1: {tanque1}%
    Tanque2: {tanque2}%
    Tanque3: {tanque3}% 
    """

print(reporte_cohete(56, 35, 23))
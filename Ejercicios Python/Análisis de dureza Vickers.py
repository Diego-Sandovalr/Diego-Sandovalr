# Mediciones de dureza HV
mediciones = [210, 215, 198, 223, 205, 189, 218, 201, 199, 140, 300]
spec_min, spec_max = 190, 230

# Acumuladores
suma = 0
maximo = mediciones[0]
minimo = mediciones[0]
fuera_spec = []

for hv in mediciones:
    suma += hv
    if hv > maximo:
        maximo = hv
    if hv < minimo:
        minimo = hv
    if hv < spec_min or hv > spec_max:
        fuera_spec.append(hv)

promedio = suma / len(mediciones)
print(f"Promedio: {promedio:.1f} HV")
print(f"Máx: {maximo}  Mín: {minimo}")
print(f"Fuera de spec: {fuera_spec}")
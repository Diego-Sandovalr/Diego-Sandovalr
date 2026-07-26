def calcular_densidad(masa, volumen): 
    return masa / volumen 
def evaluar_dureza(dureza): 
    return dureza >= 180 
def evaluar_temperatura(temperatura): 
    return 850 <= temperatura <= 950 
masa = float(input("Masa (kg): ")) 
volumen = float(input("Volumen (m3): ")) 
temperatura = int(input("Temperatura (°C): ")) 
dureza = int(input("Dureza (HB): ")) 
densidad = calcular_densidad(masa, volumen) 
cumple_dureza = evaluar_dureza(dureza) 
cumple_temperatura = evaluar_temperatura(temperatura) 
print("\n===== REPORTE =====") 
print(f"Densidad: {densidad:.2f} kg/m3") 
print(f"Dureza: {'✔ Cumple' if cumple_dureza else '✘ No cumple'}") 
print(f"Temperatura: {'✔ Cumple' if cumple_temperatura else '✘ No cumple'}") 
if cumple_dureza and cumple_temperatura: 
    print("Resultado final: PIEZA ACEPTADA") 
else: 
    print("Resultado final: PIEZA RECHAZADA")
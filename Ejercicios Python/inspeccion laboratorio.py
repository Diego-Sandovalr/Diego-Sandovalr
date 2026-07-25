material = input("Ingrese el nombre del material: ")
masa = float(input("Ingrese la masa (kg): "))
volumen = float(input("Ingrese el volumen (m3): "))
temperatura = int(input("Ingrese la temperatura (°C): "))
dureza = int(input("Ingrese la dureza (HB): "))

print("\n==============================")
print("REPORTE DE INSPECCIÓN")
print("==============================")
print(f"Material: {material}")

if dureza >= 180:
    print(f"Dureza: {dureza} HB ✔ Cumple")
else:
    print(f"Dureza: {dureza} HB ✘ No cumple")

if 850 <= temperatura <= 950:
    print(f"Temperatura: {temperatura} °C ✔ Dentro del rango")
else:
    print(f"Temperatura: {temperatura} °C ✘ Fuera del rango")

densidad = masa / volumen

if densidad >= 7.85:
    print(f"Densidad: {densidad:.2f} kg/m3 ✔ Cumple")
else:
    print(f"Densidad: {densidad:.2f} kg/m3 ✘ No cumple")

print("==============================")



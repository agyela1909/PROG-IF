#PROGRAMA10
#CarolAgyelaGonzalezOchoa

meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

numero = int(input("Escoge un número entre 1 y 12: "))

if numero in meses:
    print(f"El mes correspondiente es: {meses[numero]}")
else:
    print("Número fuera de rango. Escoge un número entre 1 y 12.")

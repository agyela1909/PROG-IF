#PROGRAMA9
#CarolAgyelaGonzalezOchoa

dias = {
    1: "lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo",
}

numero = int(input("Escoge un número entre 1 y 7: "))

if numero in dias:
    print(f"El día de la semana es: {dias[numero]}")
else:
    print("Número fuera de rango. Escoge un número entre 1 y 7.")
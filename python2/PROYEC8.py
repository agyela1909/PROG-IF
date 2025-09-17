#PROGRAMA8
#CarolAgyelaGonzalezOchoa

print("DIAS TRABAJADOR")
print("LUNES")
print("MARTES")
print("MIERCOLES")
print("JUEVES")
print("VIERNES")
print("SABADO")
pago_lunes=600
pago_martes=600
pago_miercoles=600
pago_jueves=600
pago_viernes=600
pago_sabado=600
suma=pago_lunes+pago_martes+pago_miercoles+pago_jueves+pago_viernes+pago_sabado
trabajo_extra=(input("trabajaste dias extras (si/no): "))
if trabajo_extra:
    total = suma+1000
    var = ("EL PAGO TOTAL ES: ", total)
else:
    print("NO TRABAJO DIAS EXTRAS")
SUMA=pago_lunes+pago_martes+pago_miercoles+pago_jueves+pago_viernes+pago_sabado
print("EL PAGO TOTAL ES", SUMA)
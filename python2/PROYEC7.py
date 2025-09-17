#PROGRAMA7
#CarolAgyelaGonzalezOchoa

print("VENTA DE TIENDA DE MAQUILLAJES")
paleta_sombras=int(input("INGRESE CANTIDAD DE PALETAS DE SOMBRAS "))
corrector=int(input("INGRESE CANTIDAD DE CORRECTORES "))
rimen=int(input("INGRESE CANTIDAD DE RIMEN "))
lapiz_lavial=int(input("INGRESE CANTIDAD DE LAPIZ LAVIAL"))
costo_sombras=float(input("INGRESE COSTO POR PALETA DE SOMBRAS "))
costo_corrector=float(input("INGRESE COSTO POR CORRECTOR "))
costo_rimen=float(input("INGRESE COSTO POR RIMEN "))
costo_lapiz=float(input("INGRESE COSTO POR LAPIZ LAVIAL "))
SUMA=paleta_sombras+corrector+rimen+lapiz_lavial
MULTI=paleta_sombras*costo_sombras
multi=corrector*costo_corrector
multip=rimen*costo_rimen
MULTIPLI=lapiz_lavial*costo_lapiz
NUM=MULTI+multi+multip+MULTIPLI
print("en total son: ", SUMA)
print("EL DINERO TOTAL POR LOS PRODUCTOS ES DE: ", NUM)
if NUM>=500:
    print("OBTUBO UN DESCUENTO DEL 20%")
    descuento=NUM*.20
    print("EL PAGO TOTAL ES DE: ", descuento)

else:
    print("OBTUBO UN DESCUENTO DEL 10%")
    des=NUM*.10
    print("EL PAGO TOTAL ES DE: ", des)
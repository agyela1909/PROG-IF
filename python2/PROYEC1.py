#PROGRAMA1
#CarolAGyelaGonzalezOchoa

print("PAGO ENTRADA DE FERIA")
edad=int(input("ingresa la edad"))
num=float(input("pago por entrada"))
if(edad>=1)and(edad<=12):
    pago=num*.50
    print("el pago es:",pago)
if(edad>=13)and(edad<=17):
    costo=num*.70
    print("el pago es:",costo)
if(edad>=18)and(edad<=59):
    entrada=num*.80
    print("el pago es:",entrada)
if edad>=60:
    print("entran gratis")

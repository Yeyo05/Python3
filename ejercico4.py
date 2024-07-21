opcion=int(input("Elige una opcion de comversion: (1)Longitud (2)Masa (3)Temperatura "))
if opcion==1:
    num1=int(input("Introduce un valor en centimetros:"))
    total=num1/2.54
    print("el valor equivale en pulgadas a",total)
elif opcion==2:
    num1=int(input("Introduce un valor en kilogramos:"))
    total=num1*2.205
    print("el valor equivale en libras a",total)
elif opcion==3:
    num1=int(input("Introduce un valor en grados centigrados:"))
    total=(num1*1.8)+32
    print("el valor equivale en farenheit a",total)
else:
    print("Opcion no valida")
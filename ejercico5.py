ns=6
num=int(input("Introduce un numero entre 0 y 10, te dire si adivinaste o te acercaste al numero secreto: "))
if num>ns:
    print("El numero secreto es menor a este!, intentalo de nuevo")
elif num<ns:
    print("El numero secreto es mayor a este!, intentalo de nuevo")
elif num==ns:
    print("ADIVINASTE!!, el numero secreto es ", ns)
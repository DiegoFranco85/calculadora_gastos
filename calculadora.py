print ("-----Calculadora de Gastos-----")

lista = []

while True:
    gastos = float(input("Ingresa un gasto generado (puedes usar centavos)."))

    if gastos < 0:
        print ("No puede haber un gasto negativo, por favor verifica el número.")
    elif gastos == 0:
        print("Estos fueron tus gastos:",lista)
        break
    else:
        lista.append(gastos)
        
if len(lista) == 0:
    print("No ingresaste ningún gasto a la lista!")
else:
    print("Resumen de gastos:")
    print("Tu mayor gasto fue:",max(lista))
    print("La cantidad que gastaste fue de:",sum(lista))
    print("El promedio de tus gastos fue de:", sum(lista)/ len(lista))
    print("Tu menor gasto fue de:",min(lista))
    print("La cantidad de gastos realizados fue:",len(lista))
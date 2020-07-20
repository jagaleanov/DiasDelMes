# Escribir un programa que reciba un número del 1 al 12 desde el teclado 
# y muestre el número de días correspondientes al mes que corresponda con ese dia. 
# Usar funciones

def mes(num):

    if num == 1 or num == 3 or num == 5 or num == 7 or num == 8 or num == 10 or num == 12:
        return 31
    elif num == 4 or num == 6 or num == 9 or num == 11 :
        return 30
    elif num == 2:
        return 28

numero = int(input("Ingrese un número entre 1 y 12: "))
print("El mes ",numero," tiene usualmente ",mes(numero)," dias")
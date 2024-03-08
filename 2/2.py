# Programa para saber si se le permite acceder a un prestamo bancario

# Entrada
Salario = int(input("cuanto es su Salario :"))
Deuda = input("usted tiene otra deuda que no ha pagado(si o no): ")

# Proceso y salida
if Salario >= 945200:
    if deuda == "no":
        print("su prestamo ha sido aprobado")
    else:
        print("su prestamo ha sido denegado")
elif Salario < 945200:
    print("su prestamo ha sido denegado")
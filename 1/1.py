# Programa para calcular en que cuadrante esta en punto, de un plano cartesiano

# Entrada 
X = int(input("ingrese la coordenada x: "))
y = int(input("ingrese la coordenada y: "))

# Processo y salida
if x == 0:
    if Y == 0:
        print("la coordenada" ,(x , y),"esta en el origen")
    else:
        print("la coordenada" ,(X , y),"esta en el Eje Y")
elif Y == 0:
    print("la coordenada" ,(x , y),"esta en el Eje X")
elif x > o:
    if Y > 0:
        print("la coordenada" ,(x , y),"esta en el cuadrante 1")
    else:
        print("la coordenada" ,(x , y),"esta en el cuadrante 4")
elif Y > 0:
    print("la coordenada" ,(X , y),"esta en el cuadrante 3")
else:
    print("la coordenada" ,(x , y),"esta en el cuadrante 2")

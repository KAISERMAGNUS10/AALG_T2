import random
n = int(input("¿Cuántas coordenadas quieres? "))
matriz = []
for i in range(n):
    x = random.randint(-81, 81)
    y = random.randint(-81, 81)
    matriz.append([x, y])
print("\nCoordenadas:")
for par in matriz:
    print(par)
def distancia(punto):
    x = punto[0]
    y = punto[1]
    return (x * x + y * y) ** 0.5
def buscar_mas_lejana(lista):
    if len(lista) == 0:
        return None
    elif len(lista) == 1:
        x, y = lista[0]
        if x > 0 and y < 0:
            return [x, y]
        else:
            return None
    else:
        mitad = len(lista) // 2
        izquierda = buscar_mas_lejana(lista[:mitad])
        derecha = buscar_mas_lejana(lista[mitad:])
        if izquierda and derecha:
            if distancia(izquierda) > distancia(derecha):
                return izquierda
            else:
                return derecha
        elif izquierda:
            return izquierda
        elif derecha:
            return derecha
        else:
            return None
resultado = buscar_mas_lejana(matriz)
if resultado:
    print("\nLa coordenada más alejada es:", resultado)
    print("Distancia al origen:", round(distancia(resultado), 2))
else:
    print("\nNo se encontró ninguna coordenada con X positivo e Y negativo.")

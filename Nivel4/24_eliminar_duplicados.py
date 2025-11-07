numeros = []
numeros_sin_duplicados = []
for i in range(5):# for para que el usuario ingrese 5 numeros
    numero = int(input("Ingresar 5 números: "))
    numeros.append(numero)

for i in numeros:
    if i not in numeros_sin_duplicados: #si el elemento de la lista no existe en la lista sin duplicados, se agrega a numeros sin duplicados
        numeros_sin_duplicados.append(i)
        
print(numeros_sin_duplicados)
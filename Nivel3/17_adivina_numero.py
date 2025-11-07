import random #importar la libreria de random
num = random.randint(1,10) #usar random para generar un número aleatorio entre 1-10

while True: #Ciclo para que el usuario adivine el número
   num_usuario = int(input("Ingresar un número: "))
   if num_usuario < num: #Si el número ingresado es menor al número a adivinar, indica que ingrese un número más alto
      print("Intenta con un número más alto")
   elif num_usuario > num: #Si el número ingresado es mayor al número a adivinar, indica que ingrese un número más bajo
      print("Intenta con un número más bajo")
   else: #Si acierta el número imprime el mensaje indicando que acertó y el número
      print("¡Acertaste! El número era", num)
      break
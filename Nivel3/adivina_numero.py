import random

num = random.randint(1, 50)

num_oculto = int(input("Digite un numero -> "))

if num == num_oculto:
    print("Adivinaste el numero")
else:
    print("Ese no es :( ")
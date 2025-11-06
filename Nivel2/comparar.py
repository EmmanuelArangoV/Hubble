num1 = int(input("Ingresa primer numero -> "))
num2 = int(input("Ingresa segundo numero -> "))
num3 = int(input("Ingresa tercer numero -> "))

if num1 > num2 and num1 > num3:
    print(f"El {num1} es mayor")
elif num2 > num1 and num2 > num3:
    print(f"El {num2} es mayor")
else:
    print(f"El {num3} es mayor")

if num1 < num2 and num1 < num3:
    print(f"El {num1} es menor")
elif num2 < num1 and num2 < num3:
    print(f"El {num2} es menor")
else:
    print(f"El {num3} es menor")

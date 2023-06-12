import random

numeroAdivinar = random.randrange(1, 20, 1)

intento = 5
numeroUsuario = int(input("Dime un número entre uno y 20: "))

while numeroAdivinar != numeroUsuario:
    intento -= 1

    if intento == 0:
        print("Te quedaste sin intentos.")
        break

    if numeroUsuario < numeroAdivinar:
        print(f"El número está por encima, te quedan {intento} intentos.")
    else:
        print(f"El número está por debajo, te quedan {intento} intentos.")

    numeroUsuario = int(input("Dime un número entre uno y 20: "))
else:
    print("¡Encontraste el número!")

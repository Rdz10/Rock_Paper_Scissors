"""
Juego de piedra papel y tijeras vs la computadora
"""
import random
opciones = ["piedra", "papel", "tijeras"]

print("Bienvenido al juego de piedra, papel y tijeras")

while True:
    print("Selecciona entre una de las 3 opciones: piedra, papel o tijeras ")
    jugador = input("En caso de escribir algo diferente el juego seleccionara una opcion por ti:  ")

    jugador = jugador.lower()

    if (jugador != "piedra" and jugador != "papel" and jugador != "tijeras"):
        jugador = random.choice(opciones) 
    print(f"El jugador eligio:",jugador)

    computador = random.choice(opciones)
    print(f"El computador eligio:",computador)
    
    if jugador == computador:
        print("Los dos eligieron lo mismo: Empate!\n")
    elif (jugador=="piedra") and (computador=="papel"):
        print("El computador gana\n")
    elif (jugador=="piedra") and (computador=="tijeras"):
        print("El jugador gana\n")
    elif (jugador=="tijeras") and (computador=="papel"):
        print("El jugador gana\n")
    elif (jugador=="tijeras") and (computador=="piedra"):
        print("El computador gana\n")
    elif (jugador=="papel") and (computador=="tijeras"):
        print("El computador gana\n")
    elif (jugador=="papel") and (computador=="piedra"):
        print("El jugador gana\n")



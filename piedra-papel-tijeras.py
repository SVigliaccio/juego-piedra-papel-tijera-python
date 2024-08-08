nombre1 = input("¿Como se llama el primer jugador? ")
nombre2 = input("¿Como se llama el segundo jugador? ")

jugador1 = input("¡Hola "+nombre1+"! ¿Que elijes? (piedra, papel o tijera): ")
jugador2 = input("¡Hola "+nombre2+"! ¿Que elijes? (piedra, papel o tijera): ")

jugador1 = jugador1.strip().lower()
jugador2 = jugador2.strip().lower()

if(jugador1 == jugador2):
    print("¡Empate!")
elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
    print("¡ Gana", nombre1, "!")
else:
    print("¡ Gana", nombre2, "!")
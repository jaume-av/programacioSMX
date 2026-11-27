# -*- coding: utf-8 -*-
# Activitat 6. Encàrrec de canvi: menors de 12 anys gratuïts abans de qualsevol descompte.
# Pressuposem edat no negativa i respostes si/no.
trajecte = input("Trajecte (urbà/interurbà): ")
edat = int(input("Edat: "))
carnet_jove = input("Tens carnet jove? (si/no): ") == "si"
discapacitat = input("Discapacitat reconeguda? (si/no): ") == "si"

# Un trajecte incorrecte no ha de produir cap càlcul de preu.
if trajecte != "urbà" and trajecte != "interurbà":
    print("Trajecte no vàlid")
else:
    if trajecte == "urbà":
        preu_base = 1.50
    else:
        preu_base = 3.00

    # Una sola regla de descompte: les alternatives són excloents.
    # Canvi local: prioritzem la gratuïtat, mantenint la resta de regles.
    if edat < 12:
        factor = 0
        descripcio = "Gratuït per edat"
    elif discapacitat:
        factor = 0.50
        descripcio = "50% per discapacitat"
    elif edat >= 12 and edat <= 25 and carnet_jove:
        factor = 0.70
        descripcio = "30% amb carnet jove"
    elif edat >= 65:
        factor = 0.60
        descripcio = "40% per edat"
    else:
        factor = 1
        descripcio = "Sense descompte"

    preu_final = preu_base * factor

    # Presentem una vegada les dades de qualsevol trajecte vàlid.
    print(f"Trajecte: {trajecte}")
    print(f"Preu base: {preu_base:.2f} €")
    print(f"Condició aplicada: {descripcio}")
    print(f"Preu final: {preu_final:.2f} €")

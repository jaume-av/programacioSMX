# -*- coding: utf-8 -*-
# Activitat 8. Validació, rebuig amb prioritats i pressupost.
hores = int(input("Hores de reserva: "))
assistents = int(input("Nombre d'assistents: "))
resposta_major = input("Responsable major d'edat? (si/no): ")
resposta_associacio = input("Associació registrada? (si/no): ")
resposta_disponible = input("Sala disponible? (si/no): ")
resposta_projector = input("Necessites projector? (si/no): ")
resposta_neteja = input("Necessites neteja addicional? (si/no): ")

# Comprovem els valors ABANS de convertir qualsevol altre text en False.
numeros_valids = hores >= 1 and hores <= 8 and assistents >= 1 and assistents <= 30
respostes_valides = (
    (resposta_major == "si" or resposta_major == "no")
    and (resposta_associacio == "si" or resposta_associacio == "no")
    and (resposta_disponible == "si" or resposta_disponible == "no")
    and (resposta_projector == "si" or resposta_projector == "no")
    and (resposta_neteja == "si" or resposta_neteja == "no")
)

if not numeros_valids or not respostes_valides:
    print("Dades no vàlides")
elif resposta_disponible == "no":
    # La falta de disponibilitat preval sobre l'edat del responsable.
    print("Sala no disponible")
elif resposta_major == "no":
    print("Cal una persona responsable major d'edat")
else:
    # Només calculem imports quan la reserva es pot acceptar.
    if hores <= 3:
        tarifa = 12.00
    else:
        tarifa = 10.00

    lloguer_base = hores * tarifa
    descompte = 0.00
    if resposta_associacio == "si":
        descompte = lloguer_base * 0.20

    # Els complements són independents i no tenen descompte.
    cost_projector = 0.00
    if resposta_projector == "si":
        cost_projector = 8.00
    cost_neteja = 0.00
    if resposta_neteja == "si":
        cost_neteja = 15.00

    total = lloguer_base - descompte + cost_projector + cost_neteja
    print("Reserva acceptada")
    print(f"Hores: {hores}")
    print(f"Assistents: {assistents}")
    print(f"Tarifa horària: {tarifa:.2f} €")
    print(f"Lloguer abans del descompte: {lloguer_base:.2f} €")
    print(f"Descompte: {descompte:.2f} €")
    print(f"Projector: {cost_projector:.2f} €")
    print(f"Neteja addicional: {cost_neteja:.2f} €")
    print(f"Total final: {total:.2f} €")

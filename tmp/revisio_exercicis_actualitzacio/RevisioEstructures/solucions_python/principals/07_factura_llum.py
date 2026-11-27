# -*- coding: utf-8 -*-
# Activitat 7. Una tarifa excloent i dos ajustos compatibles.
consum = float(input("Consum mensual (kWh): "))
potencia = float(input("Potència contractada (kW): "))
bo_social = input("Tens bo social? (si/no): ") == "si"
nocturna = input("Tarifa nocturna? (si/no): ") == "si"

if consum < 0 or potencia <= 0:
    print("Dades no vàlides")
else:
    # Una tarifa per a TOT el consum. No són trams acumulatius.
    if consum <= 100:
        preu_kwh = 0.15
    elif consum <= 250:
        preu_kwh = 0.20
    else:
        preu_kwh = 0.25

    cost_consum = consum * preu_kwh
    cost_potencia = potencia * 4.00
    total = cost_consum + cost_potencia
    nocturn_aplicat = "no"
    social_aplicat = "no"

    # Dos if independents: es poden aplicar els dos ajustos.
    if nocturna and consum <= 200:
        total = total * 0.95
        nocturn_aplicat = "si"
    if bo_social:
        # El 25% s'aplica al total que ja inclou l'ajust nocturn.
        total = total * 0.75
        social_aplicat = "si"

    # El format afecta la presentació, no els càlculs intermedis.
    print(f"Preu per kWh: {preu_kwh:.2f} €")
    print(f"Cost de consum: {cost_consum:.2f} €")
    print(f"Cost de potència: {cost_potencia:.2f} €")
    print(f"Descompte nocturn aplicat: {nocturn_aplicat}")
    print(f"Bo social aplicat: {social_aplicat}")
    print(f"Total final: {total:.2f} €")

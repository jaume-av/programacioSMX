# -*- coding: utf-8 -*-
# Activitat 2. Dues vies d'accés i una prohibició comuna.
# Pressuposem una edat no negativa i respostes si/no.
edat = int(input("Edat: "))
soci = input("Eres soci? (si/no): ") == "si"
autoritzacio = input("Tens autorització? (si/no): ") == "si"
bloquejat = input("Estàs bloquejat? (si/no): ") == "si"

# Cada variable representa una via d'accés completa.
via_adult = edat >= 18 and soci
via_menor = edat >= 16 and edat <= 17 and autoritzacio

# El bloqueig afecta les DUES vies, gràcies als parèntesis.
pot_entrar = not bloquejat and (via_adult or via_menor)

# Podem utilitzar directament una variable booleana en un if.
if pot_entrar:
    print("Accés al taller autoritzat")

print("Sol·licitud revisada")

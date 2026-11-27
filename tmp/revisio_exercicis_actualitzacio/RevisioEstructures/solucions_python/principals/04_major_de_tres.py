# -*- coding: utf-8 -*-
# Activitat 4. Conservem el màxim conegut fins al moment.
primer = float(input("Primer número: "))
segon = float(input("Segon número: "))
tercer = float(input("Tercer número: "))

# Començar amb el primer valor funciona també si tots són negatius.
major = primer

# Són decisions independents: cal comparar els dos candidats.
if segon > major:
    major = segon
if tercer > major:
    major = tercer

# En un empat no cal substituir: el màxim continua sent correcte.
print(f"El major és {major}")

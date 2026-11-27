# -*- coding: utf-8 -*-
# Activitat 3. Primer validem; després classifiquem.
nota = float(input("Nota: "))

if nota < 0 or nota > 10:
    print("Nota no vàlida")
else:
    # L'ordre evita classificar un 9 com un simple aprovat.
    if nota >= 9:
        qualificacio = "Excel·lent"
    elif nota >= 5:
        qualificacio = "Aprovat"
    else:
        qualificacio = "Suspés"

    # Només arribem ací quan la nota és vàlida.
    print(qualificacio)

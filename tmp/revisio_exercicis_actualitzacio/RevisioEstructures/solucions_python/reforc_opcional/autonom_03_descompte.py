# -*- coding: utf-8 -*-
# Reforç autònom 3. Una sola franja de descompte.
# L'enunciat pressuposa un import de compra no negatiu.
import_compra = float(input("Import de la compra: "))
if import_compra < 100:
    percentatge = 0
elif import_compra <= 200:
    percentatge = 10
else:
    percentatge = 20
# Calculem i mostrem el preu una vegada, fora de les alternatives.
preu_final = import_compra * (1 - percentatge / 100)
print(f"Preu final: {preu_final:.2f} €")

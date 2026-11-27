# -*- coding: utf-8 -*-
# Reforç guiat 3. Esta versió elemental no demana validar el rang.
nota = float(input("Nota: "))
# Comprovem primer el llindar més alt per a evitar solapaments.
if nota >= 9:
    print("Excel·lent")
elif nota >= 5:
    print("Aprovat")
else:
    print("Suspés")

# -*- coding: utf-8 -*-
# Reforç guiat 6. Mateixes categories amb una cadena llegible.
# Es pot comparar amb el guiat 4, sense repetir tota la pràctica.
edat = int(input("Edat: "))
if edat < 18:
    print("Menor d'edat")
elif edat < 65:
    print("Adult")
else:
    print("Jubilat")

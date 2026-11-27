# -*- coding: utf-8 -*-
# Reforç guiat 5. La segona decisió només té sentit si pot entrar.
edat = int(input("Edat: "))
soci = input("Eres soci? (si/no): ") == "si"
if edat < 18:
    print("Accés denegat")
else:
    # El descompte només es comprova per a les persones adultes.
    if soci:
        print("Entrada amb descompte")
    else:
        print("Entrada normal")

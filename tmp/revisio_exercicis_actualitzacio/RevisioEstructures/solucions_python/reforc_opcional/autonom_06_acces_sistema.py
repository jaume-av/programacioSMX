# -*- coding: utf-8 -*-
# Reforç autònom 6. Ser VIP no anul·la el requisit d'edat.
edat = int(input("Edat: "))
vip = input("Eres VIP? (si/no): ") == "si"
if edat < 18:
    print("Accés denegat")
else:
    if vip:
        print("Accés premium")
    else:
        print("Accés normal")

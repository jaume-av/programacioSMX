# -*- coding: utf-8 -*-
# Reforç IF 6. El VIP és una via alternativa a adult i soci.
edat = int(input("Edat: "))
vip = input("Eres VIP? (si/no): ") == "si"
soci = input("Eres soci? (si/no): ") == "si"
if (edat >= 18 and soci) or vip:
    print("Pot entrar")

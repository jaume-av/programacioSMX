# -*- coding: utf-8 -*-
# Reforç guiat 4. Els límits es comproven en ordre ascendent.
edat = int(input("Edat: "))
if edat < 18:
    print("Menor d'edat")
elif edat < 65:
    print("Adult")
else:
    print("Jubilat")

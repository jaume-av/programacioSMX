# -*- coding: utf-8 -*-
# Reforç IF 4. La comparació transforma si/no en un booleà.
vip = input("Eres VIP? (si/no): ") == "si"
soci = input("Eres soci? (si/no): ") == "si"
# N'hi ha prou que una de les dues situacions siga certa.
if vip or soci:
    print("Accés especial concedit")

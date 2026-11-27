# -*- coding: utf-8 -*-
# Reforç autònom 7. Intervals continus, també amb decimals.
temperatura = float(input("Temperatura: "))
if temperatura < 0:
    categoria = "Gel"
elif temperatura <= 15:
    categoria = "Fred"
elif temperatura <= 25:
    categoria = "Temperatura suau"
else:
    categoria = "Calor"
print(categoria)

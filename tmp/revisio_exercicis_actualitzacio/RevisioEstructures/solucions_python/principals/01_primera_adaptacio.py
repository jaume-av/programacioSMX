# -*- coding: utf-8 -*-
# Activitat 1. Una decisió amb continuació del flux.
# input retorna text: int el convertix a un enter.
numero = int(input("Introduïx un número enter: "))

# Només el missatge de positiu depén de la condició.
if numero > 0:
    print("El número és positiu")

# Fora del bloc: s'executa també amb zero i nombres negatius.
print("Comprovació acabada")

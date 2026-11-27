# -*- coding: utf-8 -*-
# Activitat 5. Selecció d'una operació i comprovació del divisor.
primer = float(input("Primer número: "))
segon = float(input("Segon número: "))
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
opcio = int(input("Opció: "))

# Esta bandera impedix mostrar un resultat si hi ha algun error.
operacio_valida = True

if opcio == 1:
    operacio = "Suma"
    resultat = primer + segon
elif opcio == 2:
    operacio = "Resta"
    resultat = primer - segon
elif opcio == 3:
    operacio = "Multiplicació"
    resultat = primer * segon
elif opcio == 4:
    # Comprovem ABANS de calcular la divisió.
    if segon == 0:
        print("No es pot dividir entre zero")
        operacio_valida = False
    else:
        operacio = "Divisió"
        resultat = primer / segon
else:
    print("Opció no vàlida")
    operacio_valida = False

# Un únic bloc d'eixida, compartit per les operacions vàlides.
if operacio_valida:
    print(f"Operació: {operacio}")
    print(f"Resultat: {resultat}")

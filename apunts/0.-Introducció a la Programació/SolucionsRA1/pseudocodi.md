
## COM ESCRIURE PSEUDOCODI

El **pseudocodi** serveix per escriure la solució d'un problema de manera ordenada **abans de programar-la**.

No és Python ni cap altre llenguatge de programació.

---

## Estructura bàsica

```text
INICI

    instruccions

FI
```

Tot algorisme comença amb **INICI** i acaba amb **FI**.

---

## LLEGIR — Introduir dades

Quan necessitem que l'usuari introduïsca una dada:

```text
LLEGIR nota
LLEGIR preu
LLEGIR edat
```

**LLEGIR = ENTRADA**

---

## ← — Guardar un valor

La fletxa `←` significa **guardar el valor de la dreta en el nom de l'esquerra**.

```text
suma ← nota1 + nota2
mitjana ← suma / 2
preuFinal ← preu - descompte
```

Es llig:

> «Guarda en `mitjana` el resultat de `suma / 2`.»

---

## Operacions

Podem realitzar càlculs:

| Operació    | Símbol | Exemple                    |
| ----------- | :----: | -------------------------- |
| Sumar       |   `+`  | `total ← preu1 + preu2`    |
| Restar      |   `-`  | `final ← preu - descompte` |
| Multiplicar |   `*`  | `cost ← litres * preu`     |
| Dividir     |   `/`  | `mitjana ← suma / 3`       |

---

## MOSTRAR — Obtindre un resultat

Quan volem mostrar un resultat:

```text
MOSTRAR mitjana
MOSTRAR preuFinal
MOSTRAR cost
```

**MOSTRAR = EIXIDA**

---

# LA PLANTILLA

Per a la majoria dels problemes d'aquesta missió podeu començar així:

```text
INICI

    LLEGIR dada1
    LLEGIR dada2

    resultat ← operació amb les dades

    MOSTRAR resultat

FI
```

---

# EXEMPLE COMPLET

### Problema

Calcular la mitjana de tres notes.

```text
INICI

    LLEGIR nota1
    LLEGIR nota2
    LLEGIR nota3

    suma ← nota1 + nota2 + nota3
    mitjana ← suma / 3

    MOSTRAR mitjana

FI
```

Visualment:

```text
        INICI
          ↓
        LLEGIR
          ↓
    FER ELS CÀLCULS
          ↓
        MOSTRAR
          ↓
          FI
```

---

## Recorda

```text
LLEGIR      → ENTRADA de dades

←           → GUARDAR un valor

+ - * /     → FER operacions

MOSTRAR     → EIXIDA de dades
```

### La regla més important

> **Cada línia del pseudocodi ha d'indicar una acció clara i concreta.**

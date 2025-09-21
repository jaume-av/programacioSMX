### Exercici 1. Preparar un suc de taronja

Has de dissenyar un **algorisme** que explique com preparar un suc de taronja natural.

**El que has de fer:**

1. Escriu les **entrades** (què necessites).
2. Escriu el **procés** (els passos que cal seguir).
3. Escriu la **eixida** (quin resultat obtens).
4. Redacta l’**algorisme complet** amb les dades d’entrada, les dades d’eixida i el procediment pas a pas.

---

#### Solució

* **Entrades**: taronges, ganivet, espremedora, got.
* **Procés**: tallar les taronges, espremre-les, omplir el got.
* **Eixida**: got amb suc de taronja.

**Algorisme per a preparar un suc de taronja**

* Dades d’entrada: taronges, ganivet, espremedora, got.
* Dades d’eixida: suc de taronja en un got.

**Procediment**:

1. Tallar les taronges per la meitat amb el ganivet.
2. Posar mitja taronja en l’espremedora.
3. Espremre fins que traga tot el suc.
4. Repetir el procés amb totes les meitats.
5. Abocar el suc obtingut en un got.
6. Servir el suc de taronja.

---

### Exercici 2. Enviar un missatge amb el mòbil

Has de dissenyar un **algorisme** que descriga com enviar un missatge de text (WhatsApp, Telegram o SMS) amb el mòbil.

**El que has de fer:**

1. Escriu les **entrades** (què necessites: dispositiu, dades, connexió...).
2. Escriu el **procés** (els passos fins que envies el missatge).
3. Escriu la **eixida** (quin resultat obtens).
4. Redacta l’**algorisme complet** amb les dades d’entrada, les dades d’eixida i el procediment pas a pas.

---

#### Solució

* **Entrades**: mòbil, aplicació de missatgeria, contacte del destinatari, text del missatge, connexió a internet (o cobertura).
* **Procés**: obrir l’aplicació, escriure el missatge, seleccionar el contacte, enviar.
* **Eixida**: missatge enviat al destinatari.

**Algorisme per a enviar un missatge amb el mòbil**

* Dades d’entrada: mòbil, aplicació de missatgeria, text del missatge, destinatari, connexió.
* Dades d’eixida: missatge enviat correctament.

**Procediment**:

1. Encendre el mòbil.
2. Obrir l’aplicació de missatgeria.
3. Seleccionar el contacte destinatari.
4. Escriure el text del missatge.
5. Premre el botó d’enviar.
6. Esperar la confirmació que el missatge ha sigut enviat.

---
### Exercici 3 (Qüestions)





1.-**En quina fase del cicle de vida decidiries quines dades són d’entrada i quines són d’eixida d’un programa? Explica-ho amb un exemple.**

**Solució:**
A la **fase de definició**.
Exemple: en un programa per calcular notes, les **entrades** serien les qualificacions dels alumnes i l’**eixida** seria la nota mitjana.

---

2.-**Per què és útil dividir un problema gran en subproblemes més menuts abans de programar? Escriu un exemple quotidià.**

**Solució:**
Perquè així és més fàcil entendre’l, comprovar-lo i modificar-lo.
Exemple: si vull fer un programa de “compres online”, puc dividir-lo en subproblemes: registrar usuari, afegir productes al carro, calcular total, processar el pagament.

---

3.- **Imagina que un company troba un error en un programa que has fet. A quina fase del cicle de vida correspon arreglar-lo? Com ajudaria la documentació interna?**

**Solució:**
Correspon a la **fase de manteniment**.
La **documentació interna** (comentaris dins del codi) ajudaria perquè indica què fa cada part del programa, i així és més fàcil localitzar i corregir l’error.

---

### Exercici 4. 

La següent taula mostra un **algorisme pas a pas** (llista d’instruccions).
Utilitza tres variables `A`, `B` i `C` que inicialment valen `4`, `2` i `3` respectivament.

**Valors inicials**:

* `A = 4`, `B = 2`, `C = 3`

---

### Pas a pas

1. **`A = B`**
   `A` pren el valor de `B` → `A = 2`
   → Resultat: `A = 2`, `B = 2`, `C = 3`

2. **`C = A`**
   `C` pren el valor de `A` → `C = 2`
   → Resultat: `A = 2`, `B = 2`, `C = 2`

3. **`B = (A + B + C) / 2`**
   `B = (2 + 2 + 2) / 2 = 6 / 2 = 3`
   → Resultat: `A = 2`, `B = 3`, `C = 2`

4. **`A = A + C`**
   `A = 2 + 2 = 4`
   → Resultat: `A = 4`, `B = 3`, `C = 2`

5. **`C = B - A`**
   `C = 3 - 4 = -1`
   → Resultat: `A = 4`, `B = 3`, `C = -1`

6. **`C = C - A`**
   `C = -1 - 4 = -5`
   → Resultat: `A = 4`, `B = 3`, `C = -5`

7. **`A = A * B`**
   `A = 4 * 3 = 12`
   → Resultat: `A = 12`, `B = 3`, `C = -5`

8. **`A = A + 3`**
   `A = 12 + 3 = 15`
   → Resultat: `A = 15`, `B = 3`, `C = -5`

9. **`A = A % B`**
   `A = 15 % 3 = 0` (residu de dividir 15 entre 3)
   → Resultat: `A = 0`, `B = 3`, `C = -5`

10. **`C = C + A`**
    `C = -5 + 0 = -5`
    → Resultat: `A = 0`, `B = 3`, `C = -5`

---

### Taula resolta

| Instrucció               | A  | B | C  |
| ------------------------ | -- | - | -- |
| **Inicial**              | 4  | 2 | 3  |
| 1. `A = B`               | 2  | 2 | 3  |
| 2. `C = A`               | 2  | 2 | 2  |
| 3. `B = (A + B + C) / 2` | 2  | 3 | 2  |
| 4. `A = A + C`           | 4  | 3 | 2  |
| 5. `C = B - A`           | 4  | 3 | -1 |
| 6. `C = C - A`           | 4  | 3 | -5 |
| 7. `A = A * B`           | 12 | 3 | -5 |
| 8. `A = A + 3`           | 15 | 3 | -5 |
| 9. `A = A % B`           | 0  | 3 | -5 |
| 10. `C = C + A`          | 0  | 3 | -5 |

---

## Excerci 5.  Avalua les següents expressions



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

## Excerci 5. Avalua les següents expressions

**Enunciat**
Avalua pas a pas cada expressió. Respecta l’**ordre d’avaluació**:

1. parèntesis, 2) potència `^`, 3) multiplicació i divisió `* /`, 4) suma i resta `+ -`, 5) concatenació (quan hi ha text), 6) relacionals (`==`, `<`, `>`, `<=`, `>=`, `!=`), 7) `NOT`, 8) `AND`, 9) `OR`.

---

### 1) Sense variables prèvies

#### 1. `((3 + 2) ^ 2 – 15) / 2 * 5`

**Què s’avalua primer?** Parèntesis → potència → restes/sumes → divisions → multiplicació.

1. Parèntesis interns: `3 + 2 = 5` ⇒ `((5) ^ 2 – 15) / 2 * 5`
2. Potència: `5 ^ 2 = 25` ⇒ `(25 – 15) / 2 * 5`
3. Resta: `25 – 15 = 10` ⇒ `10 / 2 * 5`
4. Divisió: `10 / 2 = 5` ⇒ `5 * 5`
5. Multiplicació: `5 * 5 = 25`
   **Resultat:** **25**

#### 2. `5 – 2 > 4 AND NOT 0.5 == 1 / 2`

**Què s’avalua primer?** Operacions aritmètiques → relacionals → `NOT` → `AND`.

1. Aritmètica: `5 – 2 = 3` i `1 / 2 = 0.5` ⇒ `3 > 4 AND NOT 0.5 == 0.5`
2. Relacionals: `3 > 4` és **Fals**; `0.5 == 0.5` és **Vertader** ⇒ `Fals AND NOT Vertader`
3. `NOT`: `NOT Vertader` és **Fals** ⇒ `Fals AND Fals`
4. `AND`: `Fals AND Fals` és **Fals**
   **Resultat:** **Fals**

---

### 2) Donades les variables i constants

```
x = 1
y = 4
z = 10
pi = 3.14
e = 2.71
```

#### 3. `2 * x + 0.5 + y – 1 / 5 * z`

**Què s’avalua primer?** Multiplicacions/divisions, després sumes/restes.

1. `2 * x = 2 * 1 = 2`
2. `1 / 5 = 0.2`
3. `0.2 * z = 0.2 * 10 = 2`
4. Sumes/restes: `2 + 0.5 + 4 – 2 = 4.5`
   **Resultat:** **4.5**

#### 4. `pi * x ^ 2 > y OR 2 * pi * x <= z`

**Què s’avalua primer?** Potència → multiplicacions → relacionals → `OR`.

1. Potència: `x ^ 2 = 1`
2. Multiplicació esquerra: `pi * 1 = 3.14`
3. Comparació esquerra: `3.14 > y` és `3.14 > 4` → **Fals**
4. Multiplicació dreta: `2 * pi * x = 2 * 3.14 * 1 = 6.28`
5. Comparació dreta: `6.28 <= z` és `6.28 <= 10` → **Vertader**
6. `OR`: `Fals OR Vertader` → **Vertader**
   **Resultat:** **Vertader**

#### 5. `'Don ' + 'Juan' == 'Don Juan' OR 'A' == 'a'`

**Què s’avalua primer?** Concatenació de text → comparacions → `OR`.

1. Concatenació: `'Don ' + 'Juan'` → `'Don Juan'`
2. Comparació esquerra: `'Don Juan' == 'Don Juan'` → **Vertader**
3. Comparació dreta: `'A' == 'a'` → **Fals** (majúscula ≠ minúscula)
4. `OR`: `Vertader OR Fals` → **Vertader**
   **Resultat:** **Vertader**

#### 6. `e ^ (x – 1) / (x * z) / (x / z)`

**Què s’avalua primer?** Parèntesis → potència → multiplicacions/divisions d’esquerra a dreta.

1. Parèntesi 1: `x – 1 = 0` ⇒ `e ^ 0`
2. Potència: `e ^ 0 = 1` (qualsevol nombre a 0 és 1)
3. Parèntesi 2: `x * z = 1 * 10 = 10`
4. Parèntesi 3: `x / z = 1 / 10 = 0.1`
5. Divisions d’esquerra a dreta:

   * `1 / 10 = 0.1`
   * `0.1 / 0.1 = 1`
     **Resultat:** **1**



## Excerci 6. Diferència entre **variable** i **constant**

**Enunciat:**
Explica amb les teues paraules quina és la diferència entre una **variable** i una **constant** dins d’un programa.
Inclou **2 o 3 exemples de la vida real** per a cada cas (variable i constant).

**Solució (model breu):**

* **Variable**: valor que **pot canviar** durant l’execució del programa.

  * Exemples:

    * `temperaturaActual` d’una aula.
    * `saldoCompte` després de cada compra.
    * `notaMitjana` quan afegim noves notes.
* **Constant**: valor que **no canvia** mentre s’executa el programa.

  * Exemples:

    * `IVA = 0.21` (si el fixem per al programa).
    * `PI = 3.141592`.
    * `HORES_PER_DIA = 24`.

---


## Excerci 7. Solucions pas a pas

> Recorda l’ordre: 1) parèntesis, 2) potència, 3) \* / (d’esquerra a dreta), 4) + -, 5) concatenació (text), 6) relacionals, 7) NOT, 8) AND, 9) OR.

---

### 1) `24 % 5`

* 24 ÷ 5 = 4, **residu 4**
  **Resultat:** **4**

---

### 2) `7 / 2 + 2.5`

* `7 / 2 = 3.5`
* `3.5 + 2.5 = 6.0`
  **Resultat:** **6.0**

---

### 3) `10.8 / 2 + 2`

* `10.8 / 2 = 5.4`
* `5.4 + 2 = 7.4`
  **Resultat:** **7.4**

---

### 4) `(4 + 6) * 3 + 2 * (5 - 1)`

* Parèntesis: `4+6=10`, `5-1=4` → `10 * 3 + 2 * 4`
* Multiplicacions: `10*3=30`, `2*4=8` → `30 + 8`
* Suma: `38`
  **Resultat:** **38**

---

### 5) `5 / 2 + 17 % 3`

* `5 / 2 = 2.5`
* `17 % 3 = 2` (residu de 17 ÷ 3)
* `2.5 + 2 = 4.5`
  **Resultat:** **4.5**

---

### 6) `7 >= 5 OR 27 <> 8`

* Comparacions: `7 >= 5` → **Vertader**; `27 <> 8` (distint) → **Vertader**
* `Vertader OR Vertader` → **Vertader**
  **Resultat:** **Vertader**

---

### 7) `(45 <= 7) OR NOT (5 >= 7)`

* Parèntesis: `45 <= 7` → **Fals**; `5 >= 7` → **Fals**
* `NOT (Fals)` → **Vertader**
* `Fals OR Vertader` → **Vertader**
  **Resultat:** **Vertader**

---

### 8) `27 % 4 + 15 / 4`

* `27 % 4 = 3`
* `15 / 4 = 3.75`
* `3 + 3.75 = 6.75`
  **Resultat:** **6.75**

---

### 9) `37 / 4 * 4 – 2`

* D’esquerra a dreta en \* i /: `37 / 4 = 9.25` → `9.25 * 4 = 37.0`
* Resta: `37.0 – 2 = 35.0`
  **Resultat:** **35.0**

---

### 10) `(25 >= 7) AND NOT (7 <= 2)`

* Parèntesis: `25 >= 7` → **Vertader**; `7 <= 2` → **Fals**
* `NOT (Fals)` → **Vertader**
* `Vertader AND Vertader` → **Vertader**
  **Resultat:** **Vertader**

---

### 11) `('H' < 'J') AND ('9' <> '7')`

* Comparacions de caràcters (ordre ASCII): `'H' < 'J'` → **Vertader**; `'9' <> '7'` → **Vertader**
* `Vertader AND Vertader` → **Vertader**
  **Resultat:** **Vertader**

---

### 12) `25 > 20 AND 13 > 5`

* `25 > 20` → **Vertader**
* `13 > 5` → **Vertader**
* `Vertader AND Vertader` → **Vertader**
  **Resultat:** **Vertader**

---

### 13) `10 + 4 < 15 - 3 OR 2 * 5 + 1 > 14 – 2 * 2`

* Aritmètica esquerra: `10+4=14`; `15-3=12` → `14 < 12` → **Fals**
* Aritmètica dreta: `2*5+1 = 10+1 = 11`; `2*2=4` → `14-4=10` → `11 > 10` → **Vertader**
* `Fals OR Vertader` → **Vertader**
  **Resultat:** **Vertader**

---

### 14) `4 * 2 <= 8 OR 2 * 2 < 5 AND 4 > 3 + 1`

> **AND** té més prioritat que **OR**.

* Aritmètica: `4*2=8` → `8 <= 8` → **Vertader**
* `2*2=4` → `4 < 5` → **Vertader**
* `3+1=4` → `4 > 4` → **Fals**
* Bloc AND: `Vertader AND Fals` → **Fals**
* OR final: `Vertader OR Fals` → **Vertader**
  **Resultat:** **Vertader**

---

### 15) `10 <= 2 * 5 AND 3 < 4 OR NOT (8>7) AND 3 * 2 <= 4 * 2 - 1`

> Resolem \* i /; després comparacions; després `NOT`; després tots els **AND**; finalment **OR**.

* Aritmètica: `2*5=10` → `10 <= 10` → **Vertader**
* `3 < 4` → **Vertader**
* Primer bloc AND: `Vertader AND Vertader` → **Vertader**
* Parèntesi: `8 > 7` → **Vertader** → `NOT Vertader` → **Fals**
* Aritmètica: `3*2=6`; `4*2=8`; `8 - 1 = 7` → `6 <= 7` → **Vertader**
* Segon bloc AND: `Fals AND Vertader` → **Fals**
* OR final: `Vertader OR Fals` → **Vertader**
  **Resultat:** **Vertader**

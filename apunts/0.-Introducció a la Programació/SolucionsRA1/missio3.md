# MISSIÓ 3 — Exemple pràctic: preparar un entrepà

Imagineu que sou un equip de 3 persones i la vostra missió és:

---

## ALUMNE 1 — PROGRAMADOR

El programador ha d’escriure les instruccions.

### Algorisme inicial

1. Agafa el pa.
2. Obri el pa.
3. Posa pernil.
4. Posa formatge.
5. Tanca l’entrepà.

**Atenció:** encara no intentem que siga perfecte. Aquesta és la primera versió.

---

## ALUMNE 2 — ORDINADOR

Ara l’ordinador ha d’executar les instruccions.

Però hi ha una norma molt important:

> **L’ordinador només pot fer exactament el que diu la instrucció.**

No pot imaginar què volíem dir.

### Executem el programa

**Instrucció 1:**

> “Agafa el pa.”

L’ordinador agafa **tota la bossa de pa**.

Per què?

Perquè no hem especificat quina peça de pa ha d’agafar.

---

**Instrucció 2:**

> “Obri el pa.”

L’ordinador intenta obrir **la bossa de pa**.

Per què?

Perquè això és el que té a les mans.

---

**Instrucció 3:**

> “Posa pernil.”

L’ordinador agafa **tot el paquet de pernil** i el posa damunt del pa.

Per què?

Perquè no hem dit quina quantitat de pernil volem.

---

**Instrucció 4:**

> “Posa formatge.”

L’ordinador posa **tot el paquet de formatge**.

---

**Instrucció 5:**

> “Tanca l’entrepà.”

L’ordinador intenta tancar-lo, però tenim un problema: l’entrepà està format per una bossa de pa i paquets sencers de pernil i formatge.

---

# ALUMNE 3 — DEBUGGER

El debugger observa l’execució i registra els problemes.

### Taula d’errors

| Pas | Instrucció      | Què ha fet l’ordinador?       | Problema detectat                                     |
| --- | --------------- | ----------------------------- | ----------------------------------------------------- |
| 1   | Agafa el pa     | Ha agafat tota la bossa       | No s’especifica quina peça ha d’agafar                |
| 2   | Obri el pa      | Ha intentat obrir la bossa    | No s’indica quina peça ha d’obrir                     |
| 3   | Posa pernil     | Ha posat tot el paquet        | No s’indica la quantitat                              |
| 4   | Posa formatge   | Ha posat tot el paquet        | No s’indica la quantitat                              |
| 5   | Tanca l’entrepà | No pot tancar-lo correctament | Les instruccions anteriors no han sigut prou precises |

---

# ARA DEPUREM

Hem descobert que les instruccions que nosaltres entenem fàcilment poden ser massa poc precises per a un ordinador.

Ara corregim l’algorisme.

## Algorisme corregit

1. Agafa una peça de pa de la bossa.
2. Col·loca la peça de pa sobre un plat.
3. Talla la peça de pa per la meitat.
4. Agafa una llesca de pernil.
5. Col·loca la llesca de pernil sobre la meitat inferior del pa.
6. Agafa una llesca de formatge.
7. Col·loca la llesca de formatge damunt del pernil.
8. Agafa la meitat superior del pa.
9. Col·loca-la damunt del formatge.
10. El resultat és un entrepà de pernil i formatge.

---

# QUÈ HEM APRÉS?

Un ordinador **no sap què volem dir**, només sap què li hem indicat.

Per això, un bon algorisme ha de ser:

* **Ordenat:** els passos tenen un ordre.
* **Finit:** en algun moment acaba.
* **Precís:** cada instrucció explica què cal fer.
* **No ambigu:** una instrucció no permet diferents interpretacions.

### La pregunta clau és:

> **Si jo fora un ordinador i només poguera fer exactament el que està escrit, sabria què fer?**

Si la resposta és **no**, cal millorar la instrucció.

---

# ARA ÉS EL VOSTRE TORN

En grups de 3:

### 1. Trieu una tasca

Per exemple:

* Preparar un entrepà.
* Enviar un missatge.
* Connectar-se a una xarxa Wi-Fi.
* Traure diners d’un caixer.
* Instal·lar una aplicació.
* Preparar la motxilla.

### 2. Repartiu els papers

**Programador** → escriu les instruccions.

**Ordinador** → executa literalment les instruccions.

**Debugger** → detecta i registra els errors.

### 3. Executeu l’algorisme inicial

No el corregiu mentre l’esteu executant.

### 4. Registreu els errors

Feu una taula com aquesta:

| Pas | Instrucció | Què ha fet l’ordinador? | Problema |
| --- | ---------- | ----------------------- | -------- |
| 1   | ...        | ...                     | ...      |
| 2   | ...        | ...                     | ...      |

### 5. Corregiu l’algorisme

Feu una versió més precisa.

### 6. Feu el diagrama de flux

Representeu visualment els passos de la **versió corregida**.

---

## PRODUCTE FINAL

El document que entregareu haurà de contenir:

**1. Algorisme inicial**
↓

**2. Taula d’errors detectats**
↓

**3. Algorisme corregit**
↓

**4. Diagrama de flux de la solució final**

> **No elimineu l’algorisme inicial.**
>
> Els errors són una part important de l’activitat: ens permeten veure com heu millorat la vostra solució.

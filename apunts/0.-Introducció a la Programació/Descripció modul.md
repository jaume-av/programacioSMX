---
title: 1. Introducció a la Programació
parent: Índex
layout: default
has_children: true
nav_order: 2
---

# RA1 — DESCOBRIM EL MÓN DE LA PROGRAMACIÓ

## El repte

Durant este primer RA descobrirem què significa **programar**, com ens comuniquem amb un ordinador, com han evolucionat els llenguatges de programació i com podem transformar un problema en una solució que després podrem programar.

Però no fareu un treball tradicional de buscar informació i copiar-la en un document.

El treball està dividit en **5 missions**. En cada missió rebreu primer una breu explicació dels conceptes necessaris i després haureu de **investigar, comprendre, relacionar i aplicar** el que heu aprés.

El procés serà sempre:

> **BUSCAR → COMPRENDRE → SELECCIONAR → RELACIONAR → CREAR**

**Duració:** 8 sessions
**Organització:** individual, parelles o grups segons la missió
**Lliurament:** Aules
**Productes:** 5 missions

---

# MISSIÓ 1 — LA MÀQUINA DEL TEMPS

## Què necessitem saber?

Un **llenguatge de programació** és un llenguatge formal que permet escriure les instruccions que formen un programa informàtic.

Els primers ordinadors no es programaven amb llenguatges com Python. Inicialment s'utilitzaven instruccions molt pròximes al funcionament de la màquina i, amb el temps, aparegueren llenguatges cada vegada més comprensibles per a les persones.

De manera simplificada:

```text
LLENGUATGE MÀQUINA
        ↓
   ASSEMBLADOR
        ↓
LLENGUATGES D'ALT NIVELL
        ↓
 C · C++ · JAVA · PYTHON...
```

La vostra primera missió serà descobrir **com hem arribat fins als llenguatges actuals**.

## Què heu de fer?

Creeu una **línia del temps visual** sobre l'evolució dels llenguatges de programació.

Ha d'incloure com a mínim:

* Llenguatge màquina
* Assemblador
* FORTRAN
* COBOL
* C
* C++
* Python
* Java
* JavaScript

Podeu afegir altres llenguatges si considereu que han sigut importants.

### De cada fita heu d'investigar

* Any aproximat d'aparició.
* Creador o creadors.
* Per què va aparéixer o quin problema intentava resoldre.
* Principal ús.
* Una aportació o característica important.

No volem nou definicions independents. La línia del temps ha de permetre observar **com ha evolucionat la programació**.

### Condicions

* Màxim **30 paraules de text explicatiu per llenguatge**.
* La informació ha d'estar resumida amb les vostres paraules.
* Utilitzeu imatges, icones, connexions o altres recursos visuals quan aporten informació.
* La informació ha de poder llegir-se i entendre's amb facilitat.

### Producte final

Una **línia del temps visual digital**.

Podeu utilitzar Canva, Genially, TimelineJS o una ferramenta equivalent.

Al final incloureu una breu conclusió:

> **Quins tres canvis considereu més importants en l'evolució dels llenguatges de programació? Per què?**

Màxim **100 paraules**.

---

# MISSIÓ 2 — EL MAPA DELS LLENGUATGES

## Què necessitem saber?

No tots els llenguatges de programació són iguals.

Segons la seua proximitat al maquinari podem parlar, de manera general, de **llenguatges de baix nivell** i **llenguatges d'alt nivell**.

El programa que escriu una persona s'anomena **codi font**, però el processador necessita instruccions que puga executar. Per això intervenen mecanismes com els **compiladors** i els **intèrprets**.

També existeixen diferents maneres d'organitzar els programes, anomenades **paradigmes de programació**, com la programació procedimental, l'orientada a objectes o la funcional.

Python és un llenguatge d'alt nivell que permet treballar amb diferents paradigmes.

Ara heu de descobrir **com encaixen totes estes peces**.

## Què heu de fer?

Construïu un **mapa conceptual** que relacione, com a mínim:

* llenguatge màquina;
* assemblador;
* llenguatges de baix nivell;
* llenguatges d'alt nivell;
* codi font;
* codi màquina;
* compilador;
* intèrpret;
* llenguatges compilats;
* llenguatges interpretats;
* programació procedimental;
* programació orientada a objectes;
* programació funcional;
* Python.

### Important

No heu de crear un diccionari de definicions.

El més important són les **relacions entre els conceptes**.

Les connexions han de tindre significat:

```text
és un...
pertany a...
permet...
es transforma mitjançant...
s'executa mitjançant...
genera...
```

Per exemple:

```text
                         PYTHON
                            │
               ┌────────────┴────────────┐
               │                         │
             és un                    permet
               │                         │
               ▼                         ▼
      LLENGUATGE D'ALT NIVELL      DIFERENTS PARADIGMES
```

### Producte final

Un **mapa conceptual digital** en una única pàgina o espai de treball.

Podeu utilitzar diagrams.net, Excalidraw, Canva, Miro, Genially o una ferramenta equivalent.

No utilitzeu paràgrafs llargs. Utilitzeu **conceptes, paraules clau i connexions**.

### Comprovació

El professor podrà seleccionar qualsevol membre del grup perquè explique durant aproximadament **2 minuts** una part del mapa.

No cal memoritzar definicions: heu de ser capaços d'explicar **per què heu relacionat els conceptes d'eixa manera**.

---

# MISSIÓ 3 — TU ERES L'ORDINADOR

## Què necessitem saber?

Abans d'escriure codi necessitem saber **com resoldre el problema**.

Un **algorisme** és una seqüència finita, ordenada i precisa de passos que permet resoldre un problema.

Un bon algorisme ha de ser:

* **ordenat**, perquè els passos segueixen una seqüència;
* **finit**, perquè ha d'acabar;
* **precís**, perquè cada instrucció indica què s'ha de fer;
* **no ambigu**, perquè una mateixa instrucció no hauria de permetre diferents interpretacions.

Les persones interpretem contínuament informació que no està escrita.

Un ordinador no ho farà.

Ho comprovarem.

## Organització

Treballareu en grups de **3 persones**.

Cada membre assumirà inicialment un paper:

### PROGRAMADOR

Escriu les instruccions.

### ORDINADOR

Executa les instruccions **literalment**.

No pot corregir, interpretar ni completar passos que no estiguen escrits.

### DEBUGGER

Observa l'execució i registra els problemes.

## El repte

Cada grup rebrà una tasca quotidiana.

Per exemple:

* preparar un entrepà;
* enviar un missatge amb el mòbil;
* connectar-se a una xarxa Wi-Fi;
* traure diners d'un caixer;
* instal·lar una aplicació;
* preparar la motxilla per anar a classe.

### Primera fase — Programar

Escriviu una primera versió de l'algorisme.

No intenteu corregir-lo mentre s'està executant.

### Segona fase — Executar

L'alumne que representa l'ordinador intentarà seguir **exactament** les instruccions.

### Tercera fase — Depurar

El debugger registrarà els problemes detectats.

Utilitzeu una taula semblant a esta:

| Pas | Instrucció  | Què ha fet l'ordinador | Problema detectat              |
| --- | ----------- | ---------------------- | ------------------------------ |
| 1   | Agafa el pa | Agafa tota la bossa    | No s'ha especificat quina peça |
| 2   | ...         | ...                    | ...                            |

### Quarta fase — Corregir

Reescriviu l'algorisme solucionant els problemes detectats.

## Producte final

Entregareu un únic document amb:

1. **Algorisme inicial.**
2. **Taula d'errors detectats.**
3. **Algorisme corregit.**
4. **Diagrama de flux de la solució final.**

No elimineu la primera versió encara que continga molts errors.

> **Els errors formen part del producte:** volem observar com heu millorat la solució després de provar-la.

---

# MISSIÓ 4 — DEL PROBLEMA A LA SOLUCIÓ

## Què necessitem saber?

La major part dels programes parteixen d'un problema.

Abans de començar a escriure Python, aprendrem a identificar tres elements:

```text
ENTRADA → PROCÉS → EIXIDA
```

**Entrada:** dades que necessita el programa.

**Procés:** operacions que realitzarem amb les dades.

**Eixida:** resultat que volem obtindre.

Per exemple:

> Calcular la mitjana de tres notes.

```text
ENTRADA
nota1, nota2, nota3

        ↓

PROCÉS
(nota1 + nota2 + nota3) / 3

        ↓

EIXIDA
mitjana
```

Podem representar després la solució mitjançant un **algorisme**, **pseudocodi** i un **diagrama de flux**.

Esta missió serà la més important del RA perquè és el pas immediatament anterior a començar a programar amb Python.

## El problema

Cada grup rebrà un problema diferent.

Per exemple:

* calcular la mitjana de diverses notes;
* calcular el preu final d'un producte amb descompte;
* repartir el compte d'un sopar;
* convertir temperatures;
* calcular el cost d'un viatge;
* calcular el cost d'omplir un depòsit.

> **No podeu començar a programar en Python.**

Primer heu de demostrar que sabeu resoldre el problema.

## Què heu de fer?

Analitzeu el problema i determineu:

### 1. Problema

Què ens estan demanant?

### 2. Entrada

Quines dades necessitem?

### 3. Eixida

Quin resultat hem d'obtindre?

### 4. Procés

Quines operacions necessitem realitzar?

### 5. Algorisme

Quins passos seguiríem i en quin ordre?

### 6. Pseudocodi

Representeu la solució utilitzant pseudocodi.

### 7. Diagrama de flux

Representeu gràficament la mateixa solució.

### 8. Cas de prova

Comproveu que la vostra solució funciona utilitzant dades concretes.

Per exemple:

```text
PROBLEMA
Repartir un compte entre diverses persones.

ENTRADA
Total = 84 €
Persones = 4

RESULTAT ESPERAT
21 € per persona
```

## Producte final

Creareu una **infografia tècnica** en una única pàgina.

Ha de permetre seguir visualment tot el procés:

```text
PROBLEMA
   ↓
ENTRADES
   ↓
PROCÉS
   ↓
EIXIDA
   ↓
ALGORISME
   ↓
PSEUDOCODI
   ↓
DIAGRAMA DE FLUX
   ↓
CAS DE PROVA
```

No es valorarà que la infografia tinga molta decoració.

Es valorarà que **una altra persona puga entendre perfectament la vostra solució només observant el producte**.

> **Guardeu esta missió.** En el RA2 recuperarem alguns d'estos problemes i convertirem la solució en un programa real escrit en Python.

---

# MISSIÓ 5 — PYTHON CONTRA EL MÓN

## Què necessitem saber?

Existeixen centenars de llenguatges de programació i no existeix un llenguatge perfecte per a totes les situacions.

Durant el curs utilitzarem **Python**.

Python és un llenguatge d'alt nivell, de propòsit general i multiparadigma, amb una sintaxi relativament clara.

Per exemple:

```python
nom = input("Com et dius? ")
print("Hola", nom)
```

S'utilitza en àmbits molt diferents:

* automatització;
* administració de sistemes;
* desenvolupament web;
* dades;
* intel·ligència artificial;
* ciberseguretat;
* ciència.

Però altres llenguatges poden resultar més adequats en altres situacions.

La missió final serà comprovar-ho.

## Què heu de fer?

Cada grup compararà **Python amb un altre llenguatge**.

Per exemple:

* Python vs Java
* Python vs C
* Python vs C++
* Python vs JavaScript
* Python vs C#

## Producte final

Creareu una **fitxa comparativa visual**.

Ha d'incloure com a mínim:

| Característica         | Python | Altre llenguatge |
| ---------------------- | ------ | ---------------- |
| Any d'aparició         |        |                  |
| Creador                |        |                  |
| Tipus / nivell         |        |                  |
| Forma d'execució       |        |                  |
| Facilitat inicial      |        |                  |
| Llegibilitat           |        |                  |
| Principals usos        |        |                  |
| Avantatge principal    |        |                  |
| Inconvenient principal |        |                  |

## El mateix problema, dos llenguatges

Incloeu també el codi necessari en els dos llenguatges per realitzar una mateixa tasca senzilla:

> **Demanar el nom d'una persona i mostrar una salutació.**

Situeu els dos fragments de codi **un al costat de l'altre** i compareu-los.

No és necessari que sapieu programar encara en cap dels dos llenguatges. Investigueu com es realitza i intenteu comprendre les diferències que observeu.

## Veredicte final

Responeu:

> **Si haguérem d'ensenyar a programar a una persona que mai ha programat, quin dels dos llenguatges elegiríeu? Per què?**

Màxim **50 paraules**.

I també:

> **En quina situació podria resultar més adequat l'altre llenguatge?**

Màxim **50 paraules**.

No heu de demostrar que Python és millor.

Heu de **comparar i justificar la vostra decisió**.

---

# ÚS D'INTERNET I INTEL·LIGÈNCIA ARTIFICIAL

Durant les cinc missions podeu utilitzar **Internet i eines d'Intel·ligència Artificial**.

Podeu utilitzar-les per:

* buscar informació;
* entendre conceptes;
* consultar exemples;
* comparar fonts;
* resoldre dubtes;
* revisar el vostre treball.

Però **copiar una resposta no significa haver resolt una missió**.

El procés ha de ser:

```text
BUSCAR
   ↓
COMPRENDRE
   ↓
COMPROVAR
   ↓
SELECCIONAR
   ↓
RELACIONAR
   ↓
CREAR
```

Qualsevol membre del grup ha de ser capaç d'explicar el contingut que heu entregat.

El professor podrà preguntar:

> Per què heu posat açò?

> Què significa este concepte?

> Per què heu relacionat estos dos elements?

> Com heu arribat a esta solució?

> Què canviaria si modificàrem esta dada?

Si no podeu explicar una informació o una solució que apareix en el vostre treball, **no heu demostrat que l'enteneu**.

---

# QUÈ ENTREGAREM?

Al final del RA haureu completat cinc productes diferents:

| Missió                           | Producte final                                             |
| -------------------------------- | ---------------------------------------------------------- |
| **1. La màquina del temps**      | Línia del temps visual sobre l'evolució dels llenguatges   |
| **2. El mapa dels llenguatges**  | Mapa conceptual de tipus, execució i paradigmes            |
| **3. Tu eres l'ordinador**       | Algorisme inicial + errors + algorisme corregit + diagrama |
| **4. Del problema a la solució** | Infografia tècnica completa + cas de prova                 |
| **5. Python contra el món**      | Comparativa visual entre Python i un altre llenguatge      |

Els productes s'entregaran en **Aules** en el format indicat pel professor.

---

# QUÈ S'AVALUARÀ?

No s'avaluarà la quantitat de text ni la decoració del treball.

Es valorarà principalment:

* la **correcció dels conceptes**;
* la capacitat per **seleccionar la informació important**;
* la capacitat per **relacionar conceptes**;
* la representació clara i visual de la informació;
* la capacitat per **analitzar i resoldre problemes**;
* la correcció dels algorismes, pseudocodi i diagrames;
* la capacitat per detectar i corregir errors;
* la justificació de les decisions;
* la capacitat per **explicar el treball realitzat**.

La **Missió 4 — Del problema a la solució** tindrà especial importància, ja que comprova si sou capaços de realitzar el procés que utilitzarem durant la resta del curs:

```text
PROBLEMA
   ↓
ANÀLISI
   ↓
ALGORISME
   ↓
PROGRAMA
```

---

# TEMPORALITZACIÓ

El treball es desenvoluparà durant un màxim de **8 sessions de classe**.

| Sessió | Treball previst                                      |
| ------ | ---------------------------------------------------- |
| **1**  | Conceptes inicials + Missió 1                        |
| **2**  | Finalització Missió 1 + conceptes i inici Missió 2   |
| **3**  | Finalització Missió 2 + algorismes i inici Missió 3  |
| **4**  | Missió 3: execució, depuració i correcció            |
| **5**  | Pseudocodi, diagrames i inici Missió 4               |
| **6**  | Desenvolupament i finalització Missió 4              |
| **7**  | Introducció a Python + Missió 5                      |
| **8**  | Finalització Missió 5 + posada en comú i conclusions |

Les missions s'aniran obrint **progressivament**.

No començareu una missió fins que hàgem treballat a classe els conceptes necessaris.

---

# I DESPRÉS?

Quan acabe este RA haureu aprés a passar d'un problema a una possible solució:

```text
PROBLEMA → ALGORISME
```

En el següent RA afegirem la peça que ens falta:

```text
PROBLEMA → ALGORISME → PYTHON
```

I començarem a escriure els nostres **primers programes reals**.

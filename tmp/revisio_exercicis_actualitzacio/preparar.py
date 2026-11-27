from pathlib import Path
import shutil, re, json, difflib
src=Path('/home/jaume/Escritorio/RevisioEstructures')
root=Path('/home/jaume/Documentos/programacioSMX/tmp/revisio_exercicis_actualitzacio/RevisioEstructures')
root.mkdir(parents=True,exist_ok=True)
for name in ['2.2.-Estructures']:
 shutil.copytree(src/name,root/name,dirs_exist_ok=True)
for name in ['README.md','REGISTRE_REVISIO.md','comprovacio.json','originals_sha256.json','_config.yml','Gemfile','Gemfile.lock','index.md','python.md']:
 shutil.copy2(src/name,root/name)
d=root/'2.2.-Estructures'
f1=d/'2.2.2.1-Exercicis IF.md';f2=d/'2.2.3.1 -Exercicis IF-ELSE.md'
s1=f1.read_text();s2=f2.read_text()
bank1='## Exercici 2 — `if` amb igualtat'+s1.split('## Exercici 2 — `if` amb igualtat',1)[1].split('## Proves mínimes dels sis exercicis',1)[0]
bank1=re.sub(r'^## Exercici (\d+) —',r'### Reforç \1 —',bank1,flags=re.M)
guided='## Exercici 1 — `if ... else` bàsic'+s2.split('## Exercici 1 — `if ... else` bàsic',1)[1].split('# Exercicis tipus examen',1)[0]
guided=re.sub(r'^## Exercici (\d+) —',r'### Reforç guiat \1 —',guided,flags=re.M)
exam=s2.split('# Exercicis tipus examen',1)[1].split('# CAS PRÀCTIC 1 — TRANSPORT PÚBLIC',1)[0]
exam=re.sub(r'## Exercici 2 — Major de tres números.*?(?=## Exercici 3)','',exam,flags=re.S)
exam=re.sub(r'## Exercici 5 — Calculadora amb menú.*?(?=## Exercici 6)','',exam,flags=re.S)
exam=re.sub(r'^## Exercici (\d+) —',r'### Reforç autònom \1 —',exam,flags=re.M)
transport=s2.split('# CAS PRÀCTIC 1 — TRANSPORT PÚBLIC',1)[1].split('# CAS PRÀCTIC 2 — FACTURA DE LLUM',1)[0].strip().rstrip('-\n ')
light=s2.split('# CAS PRÀCTIC 2 — FACTURA DE LLUM',1)[1].split('## Proves mínimes dels exercicis guiats',1)[0].strip().rstrip('-\n ')
fm1=s1.split('---',2)[1];fm2=s2.split('---',2)[1]
f1.write_text('---'+fm1+'---\n\n'+'''# Del pseudocodi a Python: primeres decisions

Ja heu treballat condicionals amb pseudocodi. Ara ens centrarem en la sintaxi de Python, la lectura de dades i el disseny de condicions. El recorregut principal consta de huit activitats entre els dos documents. Els exercicis elementals anteriors es conserven en bancs opcionals, no com una segona tanda obligatòria.

## Recorregut principal

| Activitat | Repte nou |
|---|---|
| 1. Primera adaptació | Sintaxi, entrada i continuació del flux |
| 2. Accés al taller | Regles combinades, vies alternatives i bloqueig |
| 3. Qualificació vàlida | Validació i classificació de decimals |
| 4. Major de tres | Comparacions i empats |
| 5. Calculadora | Selecció d’operació i prevenció d’errors |
| 6. Transport públic | Prioritats i un encàrrec de canvi |
| 7. Factura de llum | Ajustos compatibles i càlculs successius |
| 8. Reserva d’una sala | Transferència autònoma a un problema nou |

Les activitats 3 a 8 estan en [el document de condicionals amb alternatives](<2.2.3.1 -Exercicis IF-ELSE.html>).

## Instruccions comunes

- En este primer document utilitza `if` sense `else` ni `elif`.
- No calen bucles, funcions pròpies, classes, col·leccions ni `try/except`.
- Les edats són enters no negatius. Es pressuposa el format numèric correcte.
- Les preguntes afirmatives o negatives admeten `si/no` en minúscula, sense accent. Compara el text amb `"si"` per a obtindre un booleà; no utilitzes `bool(input(...))`.
- En estes activitats pressuposem que les respostes tenen el format indicat. Encara no cal tornar a preguntar.
- Prediu les eixides abans d’executar i registra les proves.

## Activitat 1 — Primera adaptació a Python

**Activitat breu de diagnòstic.** Demana un número enter. Si és major que zero, mostra «El número és positiu». Després de la comprovació, mostra sempre «Comprovació acabada».

Si és zero o negatiu, només ha d’aparéixer el missatge final, a més de la pregunta d’entrada.

| Entrada | Eixida esperada després de la pregunta |
|---:|---|
| -1 | Comprovació acabada |
| 0 | Comprovació acabada |
| 1 | El número és positiu; Comprovació acabada |

Explica quina instrucció ha d’estar dins del bloc i quina fora. Compara la indentació de Python amb la representació en pseudocodi.

**Microrepte oral:** si calguera mostrar també un missatge quan no és positiu, quina alternativa necessitaríem? No cal programar-la encara.

## Activitat 2 — Accés al taller de robòtica

Demana l’edat i si la persona és sòcia del centre, té autorització i està bloquejada temporalment. Les tres respostes són `si/no`.

Regles:

1. Una persona bloquejada no pot accedir en cap cas.
2. Una persona no bloquejada pot accedir si té 18 anys o més i és sòcia.
3. També pot accedir si no està bloquejada, té entre 16 i 17 anys inclosos i té autorització.
4. L’autorització no dona accés als menors de 16 anys ni als adults que no són socis.

Guarda en una variable booleana si pot accedir i utilitza-la per a mostrar «Accés al taller autoritzat» només quan corresponga. Al final mostra sempre «Sol·licitud revisada».

Tria tu els operadors i els parèntesis. Abans de programar, identifica la regla que anul·la les altres i les dues vies d’accés.

### Proves pròpies

Dissenya almenys sis casos que cobrisquen els límits d’edat, les dues vies d’accés, un menor sense autorització, un adult no soci i una persona bloquejada que compliria una via d’accés. Escriu el resultat esperat abans d’executar.

### Depuració integrada

Una altra persona proposa:

```python
pot_entrar = not bloquejat and edat >= 18 and soci or edat >= 16 and edat <= 17 and autoritzacio
```

Les variables d’estat són booleanes i `edat` és un enter. La condició és incorrecta per a estes regles. Troba un contraexemple, explica quina regla vulnera i corregix-la. Justifica què queda protegit pel bloqueig.

## Abans de continuar

Si pots llegir dades, crear booleans i justificar la condició amb autonomia, passa a l’activitat 3. Si tens una dificultat concreta, selecciona el reforç corresponent. No cal fer tot el banc.

## Banc de reforç opcional

El positiu ja s’ha integrat en l’activitat 1. Es conserven les altres cinc activitats elementals:

<details markdown="1">
<summary>Desplegar cinc exercicis de reforç</summary>

'''+bank1+'''
</details>

## Registre de proves

| Activitat i cas | Entrades | Resultat esperat | Resultat obtingut | Correcció necessària |
|---|---|---|---|---|
| | | | | |

No copies el codi en el registre: explica els casos que comproven les regles.
''')
f2.write_text('---'+fm2+'---\n\n'+'''# Condicionals: de les alternatives a la resolució autònoma

Continua les activitats 1 i 2 del [document anterior](<2.2.2.1-Exercicis IF.html>). Cada activitat incorpora un repte diferent i menys indicacions sobre l’estructura que has de triar.

## Instruccions comunes

- Utilitza els continguts de 2.1 i 2.2: variables, entrada i eixida, operadors i condicionals.
- No utilitzes bucles, funcions pròpies, classes, col·leccions ni `try/except`.
- Pressuposem entrades numèriques amb el format correcte; valida els valors que demane cada activitat.
- Les respostes afirmatives o negatives són `si/no`. Quan es demane validar-les, qualsevol altre text és incorrecte.
- Una dada invàlida provoca l’avís indicat i evita el càlcul. No cal tornar a preguntar ni utilitzar `exit()`.
- Tria les estructures a partir de les regles. Guarda els resultats en variables i reunix la presentació final per a evitar repetir-la en cada alternativa.
- Mostra els imports amb dos decimals i conserva la precisió dels càlculs intermedis.

## Activitat 3 — Una qualificació amb dades vàlides

Demana una nota decimal. Si no està entre 0 i 10 inclosos, mostra «Nota no vàlida» i no mostres qualificació.

Per a una nota vàlida, mostra una sola categoria:

- De 9 a 10 inclosos: «Excel·lent».
- Des de 5 inclòs fins a menys de 9: «Aprovat».
- Des de 0 inclòs fins a menys de 5: «Suspés».

Decidix com separar validació i classificació. Justifica l’ordre i prepara almenys sis proves que cobrisquen 0, 5, 9 i 10, un decimal pròxim a un canvi i una nota invàlida.

### Predicció integrada

```python
nota = 9
if nota >= 5:
    print("Aprovat")
if nota >= 9:
    print("Excel·lent")
```

Quants missatges apareixen? Complix l’enunciat? Explica què canviaries sense fer un altre programa complet.

## Activitat 4 — Major de tres números, també amb empats

Demana tres números decimals i mostra el valor més gran una sola vegada. Els empats són vàlids: no cal identificar posicions ni informar de l’empat.

No utilitzes `max()`, ordenació ni col·leccions. Guarda el màxim en una variable i mostra’l al final.

Exemple: amb 8, 8 i 5, el resultat és 8.

Prepara proves amb el màxim en cada posició, dos màxims iguals, els tres valors iguals i tots els valors negatius. Explica per què el procediment funciona encara que hi haja empats.

## Activitat 5 — Calculadora amb una operació segura

Demana dos números decimals i una opció entera:

| Opció | Operació |
|---:|---|
| 1 | Primer més segon |
| 2 | Primer menys segon |
| 3 | Primer per segon |
| 4 | Primer dividit entre segon |

Fes una sola operació. Si l’opció no és vàlida, mostra «Opció no vàlida» i cap resultat. Si es tria dividir i el segon número és zero, mostra «No es pot dividir entre zero» sense calcular la divisió. En els altres casos, mostra l’operació i el resultat.

El menú es pregunta una vegada, sense bucles. Prepara proves de les quatre operacions, una opció invàlida, un divisor zero i un operand negatiu. Explica quina comprovació impedix la divisió per zero: no servix avisar després de calcular-la.

## Activitat 6 — Transport públic

'''+transport+'''

### Prioritats, proves i encàrrec de canvi

Explica per què no es poden aplicar tots els descomptes de manera independent. Comprovació inicial: trajecte urbà, 10 anys i discapacitat costa 0.75 €; sense discapacitat costa 0.00 €.

Afig proves per als límits 12, 25, 26 i 65 anys, un trajecte invàlid i un perfil que complisca diverses regles.

Quan funcione, fes-ne una còpia. L’empresa demana que **la gratuïtat dels menors de 12 anys tinga prioritat sobre qualsevol descompte**, també amb discapacitat. Canvia només allò necessari i conserva la resta de les regles. Identifica una prova que canvia i dues que es mantenen. Entrega el programa base i la còpia modificada.

## Activitat 7 — Factura de llum

'''+light+'''

### Disseny i depuració

Indica quines decisions seleccionen una tarifa i quines poden ajustar conjuntament la mateixa factura.

Comprovació: consum 200 kWh, potència 3 kW, nocturna si i bo social si. El cost previ és 52.00 € i el total final 37.05 €.

Dissenya almenys huit proves: consum i potència invàlids, canvis de tarifa en 100 i 250 kWh, un decimal pròxim a un límit i les quatre combinacions dels ajustos quan poden aplicar-se.

Una solució amb booleans ha escrit:

```python
if nocturna:
    total = total * 0.95
elif bo_social:
    total = total * 0.75
```

Explica per què no representa dos ajustos compatibles i quina condició de consum falta. Proposa una correcció justificada.

## Activitat 8 — Reserva d’una sala: repte de transferència

Un centre vol acceptar o rebutjar sol·licituds i calcular-ne el pressupost.

### Dades

Demana hores de reserva i nombre d’assistents com a enters. Demana també cinc respostes `si/no`: si la persona responsable és major d’edat, si representa una associació registrada, si la sala està disponible, si necessita projector i si necessita neteja addicional.

### Validació

Les hores han d’estar entre 1 i 8 i els assistents entre 1 i 30, amb tots els extrems inclosos. Les cinc respostes han de ser exactament `si` o `no`. Si alguna dada no és vàlida, mostra «Dades no vàlides» i no decidisques la reserva ni calcules imports.

### Acceptació

Amb dades vàlides, aplica estes prioritats:

1. Si no hi ha disponibilitat, mostra «Sala no disponible».
2. Si està disponible però la persona responsable no és major d’edat, mostra «Cal una persona responsable major d’edat».
3. Si està disponible i la persona responsable és major d’edat, accepta i calcula el pressupost.

Si coincidixen les dues causes de rebuig, preval la falta de disponibilitat. No calcules imports de reserves rebutjades.

### Pressupost

- D’1 a 3 hores incloses: 12 € per hora.
- Més de 3 i fins a 8 hores: 10 € per hora, aplicats a totes les hores.
- Una associació registrada té un 20% de descompte només sobre el lloguer per hores.
- El projector suma 8 € una sola vegada.
- La neteja addicional suma 15 € una sola vegada.
- Els complements són compatibles i no tenen descompte.

Mostra hores, assistents, tarifa horària, lloguer abans del descompte, descompte aplicat, cost de cada complement i total amb dos decimals. Els assistents només intervenen en la capacitat, no en el preu.

### Treball autònom

No s’indica l’estructura. Separa validació, rebuig i pressupost; identifica decisions excloents i compatibles. Prepara almenys huit proves de límits, dades invàlides, les causes de rebuig i la seua coincidència, i complements compatibles. Calcula manualment dos pressupostos acceptats abans d’executar.

## Entrega del recorregut principal

Un programa per activitat; per a la 6, també la còpia amb el canvi. Afig les justificacions i un registre breu d’entrades, resultats esperats i obtinguts i correccions. No calen captures de totes les execucions ni repetir el codi en el registre.

## Banc de reforç opcional

Els exercicis elementals no integrats directament es conserven ací. No són una segona llista obligatòria. Els dos plantejaments de classificació per edat poden servir per a comparar estructures sobre el mateix codi; no cal repetir-ne el programa complet.

<details markdown="1">
<summary>Desplegar sis exercicis guiats de reforç</summary>

'''+guided+'''
</details>

<details markdown="1">
<summary>Desplegar cinc exercicis de reforç autònom</summary>

'''+exam+'''
</details>

Utilitza [Repàs i proves](<2.2.4-Repas i proves.html>) quan aparega cada dificultat: no cal reservar-ho tot per al final ni fer més programes complets amb el mateix esquema.
''')
solutions=root/'solucions_python';principal=solutions/'principals';reforc=solutions/'reforc_opcional'
principal.mkdir(parents=True,exist_ok=True);reforc.mkdir(parents=True,exist_ok=True)
def py(name,code,folder=principal):
 (folder/name).write_text('# -*- coding: utf-8 -*-\n'+code.strip()+'\n')
py('01_primera_adaptacio.py','''# Activitat 1. Una decisió amb continuació del flux.
# input retorna text: int el convertix a un enter.
numero = int(input("Introduïx un número enter: "))

# Només el missatge de positiu depén de la condició.
if numero > 0:
    print("El número és positiu")

# Fora del bloc: s'executa també amb zero i nombres negatius.
print("Comprovació acabada")
''')
py('02_acces_taller.py','''# Activitat 2. Dues vies d'accés i una prohibició comuna.
# Pressuposem una edat no negativa i respostes si/no.
edat = int(input("Edat: "))
soci = input("Eres soci? (si/no): ") == "si"
autoritzacio = input("Tens autorització? (si/no): ") == "si"
bloquejat = input("Estàs bloquejat? (si/no): ") == "si"

# Cada variable representa una via d'accés completa.
via_adult = edat >= 18 and soci
via_menor = edat >= 16 and edat <= 17 and autoritzacio

# El bloqueig afecta les DUES vies, gràcies als parèntesis.
pot_entrar = not bloquejat and (via_adult or via_menor)

# Podem utilitzar directament una variable booleana en un if.
if pot_entrar:
    print("Accés al taller autoritzat")

print("Sol·licitud revisada")
''')
py('03_qualificacio_valida.py','''# Activitat 3. Primer validem; després classifiquem.
nota = float(input("Nota: "))

if nota < 0 or nota > 10:
    print("Nota no vàlida")
else:
    # L'ordre evita classificar un 9 com un simple aprovat.
    if nota >= 9:
        qualificacio = "Excel·lent"
    elif nota >= 5:
        qualificacio = "Aprovat"
    else:
        qualificacio = "Suspés"

    # Només arribem ací quan la nota és vàlida.
    print(qualificacio)
''')
py('04_major_de_tres.py','''# Activitat 4. Conservem el màxim conegut fins al moment.
primer = float(input("Primer número: "))
segon = float(input("Segon número: "))
tercer = float(input("Tercer número: "))

# Començar amb el primer valor funciona també si tots són negatius.
major = primer

# Són decisions independents: cal comparar els dos candidats.
if segon > major:
    major = segon
if tercer > major:
    major = tercer

# En un empat no cal substituir: el màxim continua sent correcte.
print(f"El major és {major}")
''')
py('05_calculadora.py','''# Activitat 5. Selecció d'una operació i comprovació del divisor.
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
''')
transport_code='''# Activitat 6. Versió base: la discapacitat té la primera prioritat.
# Pressuposem edat no negativa i respostes si/no.
trajecte = input("Trajecte (urbà/interurbà): ")
edat = int(input("Edat: "))
carnet_jove = input("Tens carnet jove? (si/no): ") == "si"
discapacitat = input("Discapacitat reconeguda? (si/no): ") == "si"

# Un trajecte incorrecte no ha de produir cap càlcul de preu.
if trajecte != "urbà" and trajecte != "interurbà":
    print("Trajecte no vàlid")
else:
    if trajecte == "urbà":
        preu_base = 1.50
    else:
        preu_base = 3.00

    # Una sola regla de descompte: les alternatives són excloents.
    if discapacitat:
        factor = 0.50
        descripcio = "50% per discapacitat"
    elif edat < 12:
        factor = 0
        descripcio = "Gratuït per edat"
    elif edat >= 12 and edat <= 25 and carnet_jove:
        factor = 0.70
        descripcio = "30% amb carnet jove"
    elif edat >= 65:
        factor = 0.60
        descripcio = "40% per edat"
    else:
        factor = 1
        descripcio = "Sense descompte"

    preu_final = preu_base * factor

    # Presentem una vegada les dades de qualsevol trajecte vàlid.
    print(f"Trajecte: {trajecte}")
    print(f"Preu base: {preu_base:.2f} €")
    print(f"Condició aplicada: {descripcio}")
    print(f"Preu final: {preu_final:.2f} €")
'''
py('06_transport_public.py',transport_code)
changed=transport_code.replace('Versió base: la discapacitat té la primera prioritat.','Encàrrec de canvi: menors de 12 anys gratuïts abans de qualsevol descompte.')
changed=changed.replace('''    if discapacitat:
        factor = 0.50
        descripcio = "50% per discapacitat"
    elif edat < 12:
        factor = 0
        descripcio = "Gratuït per edat"''','''    # Canvi local: prioritzem la gratuïtat, mantenint la resta de regles.
    if edat < 12:
        factor = 0
        descripcio = "Gratuït per edat"
    elif discapacitat:
        factor = 0.50
        descripcio = "50% per discapacitat"''')
py('06b_transport_prioritat_gratuitat.py',changed)
py('07_factura_llum.py','''# Activitat 7. Una tarifa excloent i dos ajustos compatibles.
consum = float(input("Consum mensual (kWh): "))
potencia = float(input("Potència contractada (kW): "))
bo_social = input("Tens bo social? (si/no): ") == "si"
nocturna = input("Tarifa nocturna? (si/no): ") == "si"

if consum < 0 or potencia <= 0:
    print("Dades no vàlides")
else:
    # Una tarifa per a TOT el consum. No són trams acumulatius.
    if consum <= 100:
        preu_kwh = 0.15
    elif consum <= 250:
        preu_kwh = 0.20
    else:
        preu_kwh = 0.25

    cost_consum = consum * preu_kwh
    cost_potencia = potencia * 4.00
    total = cost_consum + cost_potencia
    nocturn_aplicat = "no"
    social_aplicat = "no"

    # Dos if independents: es poden aplicar els dos ajustos.
    if nocturna and consum <= 200:
        total = total * 0.95
        nocturn_aplicat = "si"
    if bo_social:
        # El 25% s'aplica al total que ja inclou l'ajust nocturn.
        total = total * 0.75
        social_aplicat = "si"

    # El format afecta la presentació, no els càlculs intermedis.
    print(f"Preu per kWh: {preu_kwh:.2f} €")
    print(f"Cost de consum: {cost_consum:.2f} €")
    print(f"Cost de potència: {cost_potencia:.2f} €")
    print(f"Descompte nocturn aplicat: {nocturn_aplicat}")
    print(f"Bo social aplicat: {social_aplicat}")
    print(f"Total final: {total:.2f} €")
''')
py('08_reserva_sala.py','''# Activitat 8. Validació, rebuig amb prioritats i pressupost.
hores = int(input("Hores de reserva: "))
assistents = int(input("Nombre d'assistents: "))
resposta_major = input("Responsable major d'edat? (si/no): ")
resposta_associacio = input("Associació registrada? (si/no): ")
resposta_disponible = input("Sala disponible? (si/no): ")
resposta_projector = input("Necessites projector? (si/no): ")
resposta_neteja = input("Necessites neteja addicional? (si/no): ")

# Comprovem els valors ABANS de convertir qualsevol altre text en False.
numeros_valids = hores >= 1 and hores <= 8 and assistents >= 1 and assistents <= 30
respostes_valides = (
    (resposta_major == "si" or resposta_major == "no")
    and (resposta_associacio == "si" or resposta_associacio == "no")
    and (resposta_disponible == "si" or resposta_disponible == "no")
    and (resposta_projector == "si" or resposta_projector == "no")
    and (resposta_neteja == "si" or resposta_neteja == "no")
)

if not numeros_valids or not respostes_valides:
    print("Dades no vàlides")
elif resposta_disponible == "no":
    # La falta de disponibilitat preval sobre l'edat del responsable.
    print("Sala no disponible")
elif resposta_major == "no":
    print("Cal una persona responsable major d'edat")
else:
    # Només calculem imports quan la reserva es pot acceptar.
    if hores <= 3:
        tarifa = 12.00
    else:
        tarifa = 10.00

    lloguer_base = hores * tarifa
    descompte = 0.00
    if resposta_associacio == "si":
        descompte = lloguer_base * 0.20

    # Els complements són independents i no tenen descompte.
    cost_projector = 0.00
    if resposta_projector == "si":
        cost_projector = 8.00
    cost_neteja = 0.00
    if resposta_neteja == "si":
        cost_neteja = 15.00

    total = lloguer_base - descompte + cost_projector + cost_neteja
    print("Reserva acceptada")
    print(f"Hores: {hores}")
    print(f"Assistents: {assistents}")
    print(f"Tarifa horària: {tarifa:.2f} €")
    print(f"Lloguer abans del descompte: {lloguer_base:.2f} €")
    print(f"Descompte: {descompte:.2f} €")
    print(f"Projector: {cost_projector:.2f} €")
    print(f"Neteja addicional: {cost_neteja:.2f} €")
    print(f"Total final: {total:.2f} €")
''')
# Reinforcement solutions: independent scripts with the same assumptions as their statements.
optional={
'if_02_igual_a_deu.py':'''# Reforç IF 2. Igualtat, no assignació.
numero = int(input("Número enter: "))
if numero == 10:
    print("El número és 10")''',
'if_03_adolescent.py':'''# Reforç IF 3. Cal complir els dos límits al mateix temps.
edat = int(input("Edat: "))
if edat >= 12 and edat <= 17:
    print("Ets adolescent")''',
'if_04_vip_o_soci.py':'''# Reforç IF 4. La comparació transforma si/no en un booleà.
vip = input("Eres VIP? (si/no): ") == "si"
soci = input("Eres soci? (si/no): ") == "si"
# N'hi ha prou que una de les dues situacions siga certa.
if vip or soci:
    print("Accés especial concedit")''',
'if_05_no_repetidor.py':'''# Reforç IF 5. not invertix la condició booleana.
repetidor = input("Eres repetidor? (si/no): ") == "si"
if not repetidor:
    print("Pot passar de curs")''',
'if_06_condicio_combinada.py':'''# Reforç IF 6. El VIP és una via alternativa a adult i soci.
edat = int(input("Edat: "))
vip = input("Eres VIP? (si/no): ") == "si"
soci = input("Eres soci? (si/no): ") == "si"
if (edat >= 18 and soci) or vip:
    print("Pot entrar")''',
'guiat_01_major_edat.py':'''# Reforç guiat 1. S'executa exactament una alternativa.
edat = int(input("Edat: "))
if edat >= 18:
    print("Ets major d'edat")
else:
    print("Ets menor d'edat")''',
'guiat_02_zero.py':'''# Reforç guiat 2. L'else cobrix tots els enters diferents de zero.
numero = int(input("Número enter: "))
if numero == 0:
    print("El número és zero")
else:
    print("El número no és zero")''',
'guiat_03_notes.py':'''# Reforç guiat 3. Esta versió elemental no demana validar el rang.
nota = float(input("Nota: "))
# Comprovem primer el llindar més alt per a evitar solapaments.
if nota >= 9:
    print("Excel·lent")
elif nota >= 5:
    print("Aprovat")
else:
    print("Suspés")''',
'guiat_04_classificacio_edat.py':'''# Reforç guiat 4. Els límits es comproven en ordre ascendent.
edat = int(input("Edat: "))
if edat < 18:
    print("Menor d'edat")
elif edat < 65:
    print("Adult")
else:
    print("Jubilat")''',
'guiat_05_condicional_anidat.py':'''# Reforç guiat 5. La segona decisió només té sentit si pot entrar.
edat = int(input("Edat: "))
soci = input("Eres soci? (si/no): ") == "si"
if edat < 18:
    print("Accés denegat")
else:
    # El descompte només es comprova per a les persones adultes.
    if soci:
        print("Entrada amb descompte")
    else:
        print("Entrada normal")''',
'guiat_06_alternatives_edat.py':'''# Reforç guiat 6. Mateixes categories amb una cadena llegible.
# Es pot comparar amb el guiat 4, sense repetir tota la pràctica.
edat = int(input("Edat: "))
if edat < 18:
    print("Menor d'edat")
elif edat < 65:
    print("Adult")
else:
    print("Jubilat")''',
'autonom_01_parell_imparell.py':'''# Reforç autònom 1. El residu determina la paritat.
numero = int(input("Número enter: "))
# També funciona amb zero i nombres negatius.
if numero % 2 == 0:
    print("Parell")
else:
    print("Imparell")''',
'autonom_03_descompte.py':'''# Reforç autònom 3. Una sola franja de descompte.
# L'enunciat pressuposa un import de compra no negatiu.
import_compra = float(input("Import de la compra: "))
if import_compra < 100:
    percentatge = 0
elif import_compra <= 200:
    percentatge = 10
else:
    percentatge = 20
# Calculem i mostrem el preu una vegada, fora de les alternatives.
preu_final = import_compra * (1 - percentatge / 100)
print(f"Preu final: {preu_final:.2f} €")''',
'autonom_04_nota_valida.py':'''# Reforç autònom 4. Els extrems del rang són vàlids.
nota = float(input("Nota: "))
if nota >= 0 and nota <= 10:
    print("Nota correcta")
else:
    print("Nota incorrecta")''',
'autonom_06_acces_sistema.py':'''# Reforç autònom 6. Ser VIP no anul·la el requisit d'edat.
edat = int(input("Edat: "))
vip = input("Eres VIP? (si/no): ") == "si"
if edat < 18:
    print("Accés denegat")
else:
    if vip:
        print("Accés premium")
    else:
        print("Accés normal")''',
'autonom_07_temperatura.py':'''# Reforç autònom 7. Intervals continus, també amb decimals.
temperatura = float(input("Temperatura: "))
if temperatura < 0:
    categoria = "Gel"
elif temperatura <= 15:
    categoria = "Fred"
elif temperatura <= 25:
    categoria = "Temperatura suau"
else:
    categoria = "Calor"
print(categoria)'''
}
for name,code in optional.items():py(name,code,reforc)
(solutions/'README.md').write_text('''# Solucions comentades de condicionals

## Recorregut principal

| Activitat | Fitxer |
|---|---|
| 1. Primera adaptació | `principals/01_primera_adaptacio.py` |
| 2. Accés al taller | `principals/02_acces_taller.py` |
| 3. Qualificació vàlida | `principals/03_qualificacio_valida.py` |
| 4. Major de tres | `principals/04_major_de_tres.py` |
| 5. Calculadora | `principals/05_calculadora.py` |
| 6. Transport, regles base | `principals/06_transport_public.py` |
| 6. Encàrrec de canvi | `principals/06b_transport_prioritat_gratuitat.py` |
| 7. Factura de llum | `principals/07_factura_llum.py` |
| 8. Reserva de sala | `principals/08_reserva_sala.py` |

## Reforç opcional

`reforc_opcional/` conté setze programes independents. Els prefixos `if`, `guiat` i `autonom` coincidixen amb els bancs dels dos documents d’exercicis; la numeració conservada permet localitzar l’exercici anterior.

No són una segona llista obligatòria. Els dos fitxers de classificació per edat es conserven per a comparar-los si cal.

## Execució

En Ubuntu:

```bash
python3 principals/02_acces_taller.py
```

En Windows, amb el llançador instal·lat:

```text
py principals/02_acces_taller.py
```

Executa cada fitxer per separat en un terminal. No necessita biblioteques externes. Tots els fitxers estan en UTF-8 i utilitzen variables, entrada i eixida, operadors i condicionals, sense bucles, funcions pròpies ni classes.

Es pressuposa el format numèric correcte, tal com indiquen els enunciats. No s'ha afegit `try/except`. Només es validen els dominis i les opcions demanats; en la reserva de sala també es validen explícitament les cinc respostes si/no.

Els comentaris expliquen el motiu de cada decisió i la ubicació dels càlculs. Són solucions de referència: l'alumnat pot proposar altres estructures correctes.

## Proves importants

- Taller: persona bloquejada de 16 anys amb autorització; ha de quedar sense accés.
- Major: valors negatius i empats.
- Calculadora: opció incorrecta i divisor zero, sense mostrar resultat.
- Transport base: urbà, 10 anys i discapacitat dona 0.75 €; en la versió amb canvi dona 0.00 €.
- Llum: 200 kWh, 3 kW, bo social si i nocturna si dona 37.05 €.
- Sala: 4 hores, 20 assistents, responsable adult, associació si, disponible si, projector si i neteja si dona 55.00 €.
- Sala: si falten alhora disponibilitat i responsable adult, preval «Sala no disponible»; si hi ha una dada invàlida, preval «Dades no vàlides».
''')
# Keep the review's support files consistent with the newly authorised exercise sequence.
p=root/'README.md';p.write_text(p.read_text()+'''

## Actualització dels exercicis i solucions comentades

Els dos documents d'exercicis s'han reorganitzat en huit activitats principals, amb menys repetició i més autonomia. Les activitats anteriors es conserven integrades o en setze reforços opcionals desplegables. La teoria no s'ha canviat.

`solucions_python/` conté nou programes del recorregut principal (inclòs el canvi del transport) i setze de reforç. El README de la carpeta indica la correspondència i l'execució.
''')
p=root/'REGISTRE_REVISIO.md';p.write_text(p.read_text()+'''

## Actualització: progressió amb pseudocodi previ i solucions Python

Els dos documents d'exercicis s'han refet amb huit activitats principals i setze exercicis bàsics de reforç opcional. Cinc activitats anteriors s'integren en el recorregut principal (positiu, màxim, calculadora, transport i llum); les altres setze es conserven en bancs desplegables. No són una segona tanda obligatòria. Les taules resoltes s'han substituït per exemples seleccionats i criteris per a dissenyar proves amb autonomia.

S'incorporen predicció i depuració dins de les activitats, un encàrrec explícit de canvi sobre una còpia del transport i un repte autònom de reserva de sala. Es conserven íntegrament les regles base i els camps d'eixida dels casos de transport i llum. La teoria i la pàgina de repàs no s'han modificat.

S'afigen 25 fitxers Python comentats: huit activitats principals, una variant del transport i setze reforços. No utilitzen funcions pròpies, classes, bucles ni col·leccions. Les hipòtesis d'entrada i les validacions respecten els enunciats.
''')
original=Path('/home/jaume/Documentos/programacioSMX/apunts/2.-Python/2.2.-Estructures')
patch=''
for f in sorted(d.glob('*.md')):
 before=original/f.name
 patch+=''.join(difflib.unified_diff(before.read_text().splitlines(True) if before.exists() else [],f.read_text().splitlines(True),fromfile='original/'+f.name if before.exists() else '/dev/null',tofile='revisio/'+f.name))
(root/'revisio.patch').write_text(patch)
print('Preparats dos documents i',len(list(solutions.rglob('*.py'))),'programes comentats.')

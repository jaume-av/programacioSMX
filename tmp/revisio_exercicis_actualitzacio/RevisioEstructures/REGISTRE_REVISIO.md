# Registre de revisió de 2.2 Estructura

## Criteri de treball

Conservar explicacions, exemples, activitats i regles vàlides. Corregir errors o ambigüitats localitzades i afegir suport didàctic. Els originals no s’han editat.

## Recomanacions aplicades

| Observació | Aplicació |
|---|---|
| Introducció repetida en dos pàgines | La portada ara orienta i enllaça; la introducció completa queda en 2.2.1 |
| Lectura de booleans sense explicar | Lectura si/no amb comparació i avís sobre bool("False") |
| Afirmació que un if sempre compara | Es permeten comparacions, booleans directes i combinacions |
| Generalització que només s’executa un camí | Regla delimitada a una cadena; comparació amb if independents |
| Terminologia simple/compost ambigua | Taula inicial i exemple específic |
| Curtcircuit absent | Explicació i divisió protegida amb and |
| Sortida d’un bloc confosa amb fi del programa | Aclariment i exemple amb missatge Final |
| Regla d’ordre massa general | Es distingixen llindars solapats i prioritats de l’enunciat |
| Else presentat com a imprescindible sempre | Es delimita quan cal cobrir el cas restant |
| Valors decimals sense categoria | Temperatura i consum amb intervals continus |
| Empats en el màxim | Es mostra el valor màxim una sola vegada |
| Opció incorrecta de calculadora | Missatge explícit i absència d’operació |
| Prioritat de discapacitat sorprenent | Es conserva i s’explica amb el cas d’un menor amb discapacitat |
| «Para» sense eina coneguda | Evitar càlculs mitjançant if/else, sense exit |
| Ajustos de llum compatibles | Aplicació successiva explicada, sense convertir-los en elif |
| Falta de proves de límits | Taules per a totes les activitats i casos pràctics |
| Falta de predicció i depuració | Pàgina 2.2.4 amb seguiment, quatre prediccions i cinc depuracions |
| Numeració i navegació incoherents | Títols, parent i ordres corregits; noms de fitxer conservats |
| Explicació dins de l’eixida i errades tipogràfiques | Correccions locals sense reescriure la resta |

## Regles que es conserven

- Els sis exercicis de condicional simple.
- Els sis exercicis guiats de condicionals amb alternatives.
- Els set exercicis tipus examen.
- Els dos casos pràctics complets i tots els seus camps d’eixida.
- Tarifes, percentatges, límits d’edat i prioritats originals de transport.
- Tarifes per consum, cost de potència i descomptes successius de llum.
- Exemples incorrectes intencionats d’indentació i assignació: continuen identificats com a errors.
- Nom i ascendent de la unitat per a integrar-la en el curs existent.

En el transport, «quin títol es pot usar» s’ha precisat com «quin tipus de trajecte s’aplica», perquè l’original només definix urbà/interurbà i no proporciona un catàleg de títols. No s’han inventat tarifes ni productes nous.

El concepte de «condició no executa accions» es manté dins del context dels exemples introductoris: es distingix entre calcular un valor i seleccionar un bloc. No es presenta com una explicació avançada de possibles efectes laterals d’expressions.

## Canvis per fitxer

### 2.2.3.1 -Exercicis IF-ELSE.md

- Numeració de la pàgina d’exercicis corregida.
- Parent actualitzat perquè coincidisca exactament amb el nou títol de 2.2.3.
- Pàgina d’exercicis sense descendents.
- Ordre coherent dins de la seua pàgina pare.
- Criteri comú per a tipus de dades, si/no i validacions sense eixides anticipades.
- Correcció ortogràfica del títol.
- Tractament d’empats i objectiu d’usar condicionals.
- Extrems del descompte explícits.
- Extrems de la validació de nota explícits.
- Opció incorrecta i divisió per zero amb comportament especificat.
- Intervals continus per a temperatures decimals: 15,5 té categoria.
- Objectiu alineat amb les eixides definides: no s’inventa un catàleg de títols de transport absent de l’original.
- Prioritat de discapacitat conservada i exemplificada, sense canviar unilateralment la regla vàlida.
- Interpretació de parar sense eines fora del temari.
- Interval de consum continu que inclou 100,5 kWh.
- Compatibilitat i ordre dels descomptes explicitats sense canviar-ne el càlcul.
- Afegides proves de tots els exercicis i dels dos casos pràctics, amb prioritats, empats i valors límit.

### 2.2.1-Introducció als codicionals.md

- Marcatge com a pàgina sense descendents.
- Precisió de l’explicació dels resultats de and/or, sense introduir-ne un ús avançat en els exercicis.
- Explicació de la lectura de booleans amb comparacions i de l’error bool("False").
- Criteri explícit d’indentació amb quatre espais.

### 2.2.-estructura.md

- Substitució de la introducció duplicada per una portada i índex; tota la introducció es conserva en 2.2.1.

### 2.2.3-Condicionals Compostos.md

- Numeració de la pàgina 2.2.3 corregida.
- Abast de la regla d’un únic camí i cas sense else.
- Cas sense alternativa final i precisió del flux posterior.
- Explicació precisa d’else, que no té una condició que es comprove.
- Correcció tipogràfica.
- Precisió de la regla d’ordre segons llindars o prioritats.
- Else com a cobertura del cas restant, sense presentar-lo com una obligació universal.
- Exemple complet de condició impossible, sense un error de sintaxi addicional per bloc buit.
- Afegits if independents versus elif i patró complet de validació sense bucles.

### 2.2.2.1-Exercicis IF.md

- Pàgina d’exercicis sense descendents.
- Ordre coherent dins de la seua pàgina pare.
- Instruccions comunes i connexió amb la lectura d’enters i booleans.
- Format de resposta si/no en els exercicis 4, 5 i 6; la lògica i els missatges es mantenen.
- Taula de proves per a tots els exercicis, inclosos els extrems dels intervals.

### 2.2.2-Condicionals Simples.md

- Explicació de l’eixida buida fora del bloc d’eixida.
- Correcció de la nota sobre not i de les errades tipogràfiques.
- Correcció de l’afirmació que sempre cal comparar en un if.
- Afegits curtcircuit amb protecció de divisió i reforç de la distinció entre condició i estructura.

### Pàgina nova: 2.2.4-Repas i proves.md

Seguiment de condicions i cadenes, taules de veritat, quatre prediccions, cinc depuracions, selecció de casos de prova i autocomprovació final.

## Compatibilitat amb Just the Docs

- Front matter YAML amb layout default, títols, parent i nav_order.
- Títols de pare coincidents i numeració 2.2.3/2.2.3.1 corregida conjuntament.
- Jerarquia completa en el lloc independent amb Índex i 2. Python.
- Enllaços relatius a les pàgines HTML que genera Jekyll, sense dependre de la ruta absoluta del repositori original.
- Taules i blocs de codi compatibles amb Kramdown/GFM, sense JavaScript, extensions Mermaid ni plugins afegits.
- Tema i versions de dependències coincidents amb el curs.

Referència de navegació: [documentació oficial de Just the Docs](https://just-the-docs.com/docs/navigation/main/).

## Comprovacions

Els resultats de les comprovacions automatitzades es registren en `comprovacio.json`. Inclouen integritat dels originals, metadades, pares, enllaços locals, conservació de les activitats, sintaxi dels fragments i casos de prova dels càlculs.

Els fragments incorrectes intencionats i els esquemes de sintaxi no es tracten com si foren programes independents. No es penalitzen com a errors del temari.

La còpia s’ha compilat amb Jekyll i Just the Docs 0.10.1 en un contenidor Ruby, sense canviar l’entorn ni el repositori originals. El tema emet avisos de deprecació de Sass, però la compilació acaba correctament. No s’han canviat les versions del tema per a silenciar-los.

La carpeta `_site` permet revisar el resultat compilat sense instal·lar Ruby. Les dependències descarregades per a la comprovació no formen part de l’entrega.


## Actualització: progressió amb pseudocodi previ i solucions Python

Els dos documents d'exercicis s'han refet amb huit activitats principals i setze exercicis bàsics de reforç opcional. Cinc activitats anteriors s'integren en el recorregut principal (positiu, màxim, calculadora, transport i llum); les altres setze es conserven en bancs desplegables. No són una segona tanda obligatòria. Les taules resoltes s'han substituït per exemples seleccionats i criteris per a dissenyar proves amb autonomia.

S'incorporen predicció i depuració dins de les activitats, un encàrrec explícit de canvi sobre una còpia del transport i un repte autònom de reserva de sala. Es conserven íntegrament les regles base i els camps d'eixida dels casos de transport i llum. La teoria i la pàgina de repàs no s'han modificat.

S'afigen 25 fitxers Python comentats: huit activitats principals, una variant del transport i setze reforços. No utilitzen funcions pròpies, classes, bucles ni col·leccions. Les hipòtesis d'entrada i les validacions respecten els enunciats.

La portada de la unitat actualitza únicament les dues descripcions d'enllaços als exercicis perquè reflectisquen la nova progressió. Les explicacions teòriques es mantenen.

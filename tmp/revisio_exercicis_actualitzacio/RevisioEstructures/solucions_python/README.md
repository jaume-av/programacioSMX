# Solucions comentades de condicionals

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

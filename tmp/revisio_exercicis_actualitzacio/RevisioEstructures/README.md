# RevisioEstructures

Còpia revisada de **2.2 Estructura**, preparada per a Just the Docs i separada del curs original.

## Què conté?

- `2.2.-Estructures/`: els sis fitxers originals revisats, amb els mateixos noms, i una pàgina nova de repàs i proves.
- `REGISTRE_REVISIO.md`: problemes detectats, decisions, canvis i comprovacions.
- `revisio.patch`: diferències textuals respecte de l’original.
- `originals_sha256.json`: empremtes dels originals, per a comprovar que no s’han modificat.
- `_config.yml`, `Gemfile`, `index.md` i `python.md`: suport per a previsualitzar esta còpia de manera independent.

## Revisar el lloc ja compilat, sense instal·lar Ruby

La carpeta `_site/` conté la versió HTML generada amb el tema Just the Docs real. Per a veure-la, obri un terminal en esta carpeta i executa:

```bash
python3 -m http.server 8000 --bind 127.0.0.1 --directory _site
```

Després obri `http://127.0.0.1:8000`. Prem `Ctrl+C` en el terminal per a parar el servidor. Cal servir la carpeta per HTTP perquè els enllaços i els recursos del tema utilitzen rutes des de l’arrel; no n’hi ha prou amb fer doble clic en un HTML.

Esta vista és una còpia compilada. Si edites els Markdown, torna a compilar amb Jekyll per a actualitzar-la.

## Previsualitzar amb Just the Docs

Cal tindre Ruby i Bundler disponibles. Des d’esta carpeta:

```bash
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

Obri `http://127.0.0.1:4000` i entra en **Índex → 2. Python → 2.2 Estructura**.

El Gemfile manté Jekyll 4.4 i Just the Docs 0.10.1, igual que el repositori del curs. `bundle install` necessita connexió per a descarregar les dependències si encara no estan instal·lades. El tema s’instal·la com a gem: no s’ha substituït per un disseny HTML propi.

Per a generar el lloc sense iniciar un servidor:

```bash
bundle exec jekyll build
```

## Substitució manual quan aproves el contingut

1. Fes una còpia de seguretat de `apunts/2.-Python/2.2.-Estructures`.
2. Copia els set fitxers de la carpeta `2.2.-Estructures` d’esta revisió dins de la carpeta equivalent del curs.
3. No copies els fitxers de previsualització sobre l’índex ni la configuració del curs.
4. Revisa la navegació i executa la compilació habitual del teu lloc.

Els noms dels sis fitxers existents s’han conservat, inclòs `codicionals` en el nom de fitxer, per a no canviar adreces externes innecessàriament. Els títols visibles i les referències de la navegació sí que s’han corregit quan calia.

El pare `2.2 Estructura` i l’ascendent `2. Python` mantenen els mateixos noms. La pàgina 2.2.3 i la seua pàgina d’exercicis tenen la numeració corregida i el `parent` corresponent actualitzat.

## Abast didàctic

Es conserva el contingut vàlid, els sis exercicis de `if`, els sis exercicis guiats amb alternatives, els set exercicis tipus examen i els dos casos pràctics. Les ampliacions no necessiten bucles, funcions pròpies, classes ni col·leccions.

Les dades afirmatives o negatives es demanen com `si/no`. No s’ha afegit normalització amb mètodes de cadenes ni gestió d’excepcions. Les validacions sense bucles es resolen amb condicionals.

La regla del transport que prioritza la discapacitat es conserva expressament i s’explica amb proves. No s’han alterat els percentatges ni les tarifes originals.


## Actualització dels exercicis i solucions comentades

Els dos documents d'exercicis s'han reorganitzat en huit activitats principals, amb menys repetició i més autonomia. Les activitats anteriors es conserven integrades o en setze reforços opcionals desplegables. La teoria no s'ha canviat.

`solucions_python/` conté nou programes del recorregut principal (inclòs el canvi del transport) i setze de reforç. El README de la carpeta indica la correspondència i l'execució.

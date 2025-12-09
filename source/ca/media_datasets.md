---
toc: "media"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Dissenya i emmagatzema dades tabulars i usa-les amb Widgets de dades per afegir a Dissenys"
keywords: "conjunt de dades remot, font json, font csv, columnes de conjunt de dades, files de conjunt de dades, dades de conjunt de dades, veure rss"
---

# Conjunts de Dades (DataSets)

Els Conjunts de Dades s'utilitzen per dissenyar i emmagatzemar dades tabulars que es creen i gestionen independentment dels [Dissenys](layouts.html) i [Llistes de Reproducció](media_playlists.html). Un cop creats, els Conjunts de Dades s'afegeixen a Dissenys i Llistes de Reproducció utilitzant el Widget de [Conjunt de Dades](media_module_dataset.html).

Els Conjunts de Dades també es poden utilitzar per crear els teus propis [Feeds RSS](media_datasets.html#content-view-rss) per afegir al Widget [Ticker](media_module_ticker.html).

## Resum de Característiques:

- Definir l'estructura de dades.
- Les dades es poden afegir manualment.
- Importar dades des d'un fitxer CSV.
- Usar una font de dades formatada en JSON a través de l'API.
- Sincronitzar des d'una font de dades de tercers de forma remota en un horari.
- Mantenir contingut sense accedir a Dissenys/Llistes de Reproducció.
- Reutilitzar a través de múltiples Widgets/Dissenys/Llistes de Reproducció.
- Crear un feed RSS des d'un Conjunt de Dades.

Els Conjunts de Dades han estat dissenyats per ser versàtils de manera que puguin configurar-se de diverses maneres amb el Widget de Conjunt de Dades així com una font de dades per a un Mòdul personalitzat. Un Conjunt de Dades proporciona una forma convenient d'importar i mostrar dades d'altres sistemes en [[PRODUCTNAME]].

Exemples d'on podrien utilitzar-se els Conjunts de Dades:

- Un menú de begudes en un bar
- Horaris de sortida en un club de golf
- Reserves de sales de reunions
- Horaris d'autobusos

Els Conjunts de Dades es creen i gestionen independentment dels Dissenys i Llistes de Reproducció i, per tant, no requereixen accés d'usuari als Dissenys, l'Editor de Dissenys o Llistes de Reproducció per afegir o gestionar les dades contingudes dins d'un Conjunt de Dades.

![DataSet Flow](img/v4_media_dataset_flow.png)

## Creant un Conjunt de Dades

Els Conjunts de Dades es creen i gestionen seleccionant **Conjunts de Dades** sota la secció **Biblioteca** del menú principal del CMS:

![DataSet Grid](img/v4_media_dataset_grid.png)

- Selecciona el botó **Afegir Conjunt de Dades** i completa els camps del formulari per crear un nou registre:

![DataSet Add](img/v4_media_dataset_add.png)

- Dóna al teu Conjunt de Dades un **Nom** per a una identificació fàcil al CMS. Proporciona una **Descripció** interna opcional i ingressa un **Codi** si fas referència a aquest Conjunt de Dades a través de l'API.

Si el Conjunt de Dades es va a connectar per sincronitzar amb una font de dades **Remota**, marca per habilitar i continuar amb la configuració de [Creant Conjunts de Dades Remotes](media_datasets.html#content-creating-remote-datasets).

Si el Conjunt de Dades **no és Remot**, fes clic per Guardar el registre del Conjunt de Dades i continua des de la secció [Crear i Configurar Columnes](media_datasets.html#content-create-and-configure-columns).

### Creant Conjunts de Dades Remots

Els Conjunts de Dades Remots són un tipus especial de Conjunt de Dades que se sincronitzarà periòdicament des d'una font de dades de tercers. [[PRODUCTNAME]] cridarà a la URL en un període de temps escollit i analitzarà les dades d'acord amb les instruccions establertes en el registre del Conjunt de Dades i qualsevol Columna que s'hagi definit com a **Remota**.

Al seleccionar Remot, es posen a disposició camps amb pestanyes addicionals perquè el registre del Conjunt de Dades Remot es pugui completar completament:

![Remote DataSet Options](img/v4_media_dataset_remote.png)

- #### Remot

  Estableix el tipus de mètode de sol·licitud i ingressa la URL per a la font de dades remota.

- #### Autenticació

  Proporciona informació d'autenticació. Els Encapçalaments Personalitzats estan disponibles per proporcionar una cadena opcional d'encapçalaments HTTP personalitzats.

- #### Dades

  Estableix la font de dades remota:

### Font JSON

Les dades JSON es poblen d'acord amb les Columnes definides com tipus Remots. Al especificar una **Columna Remota** es necessita ingressar una 'ruta de dades' que és la ruta de sintaxi JSON a les dades per a aquesta columna, amb respecte a la **Arrel de Dades** especificada.

{tip}
Considera una font de dades JSON d'exemple:

```json
{
    "base": "EUR",
    "date": "2017-12-22",
    "rates": {
        "GBP": 0.88568,
        "THB": 38.83,
        "USD": 1.1853
    }
}
```

Si volguéssim dues columnes per capturar el **Símbol** i el **Valor** de la moneda, necessitaríem establir la **Arrel de Dades** en `rates` i tenir Columnes per:

- **Símbol** - ruta de dades = 0
- **Valor** - ruta de dades = 1

{/tip}

Usa la **URL de dades de prova** per assegurar que es retorni l'estructura desitjada.

### Font CSV

La font de dades remota es pot seleccionar com un CSV.

Si la font CSV conté encapçalaments, marca per ignorar la primera fila.

Usa la **URL de dades de prova** per assegurar que es retorni l'estructura desitjada.

#### Avançat

- Estableix amb quina freqüència s'han d'obtenir i importar les dades remotes.

{tip}
La tasca d'obtenir conjunt de dades remot s'executa cada hora per defecte. Els Conjunts de Dades Remots estan destinats a dades que s'actualitzen amb poca freqüència i no en temps real.
{/tip}

- Estableix una escala de temps per Truncar dades.

- Usa el menú desplegable per seleccionar un Conjunt de Dades si uses dependents.

- Opcionalment estableix un límit de files i què ha de passar si s'excedeix aquest límit.

{nonwhite}

{noncloud}
Si no s'estableix un **Límit de Files** aquí, s'utilitzarà el Límit de Files aplicat en la [Configuració del CMS](tour_cms_settings.html#content-defaults) per clients no Cloud.
{/noncloud}

{cloud}
Si no s'estableix un **Límit de Files** aquí, s'aplicarà el predeterminat que és 10,000 files per Conjunt de Dades per clients Cloud.
{/cloud}
{/nonwhite}

- Fes clic en **Guardar**.

## Crear i Configurar Columnes

Les Columnes defineixen l'estructura de les teves dades:

- Usa el menú de fila per a un registre de Conjunt de Dades i selecciona **Veure Columnes**:

![DataSets Add columns](img/v4_media_datasets_add_columns.png)

{tip}
Per defecte, tots els nous Conjunts de Dades tindran una **Col1** afegida. ¡Això s'ha d'editar o eliminar usant el menú de fila per Col1!
{/tip}

- Elimina Col1 des del menú de fila i fes clic al botó **Afegir Columna** per crear una nova columna

o

- Usa el menú de fila per Col1 i selecciona **Editar**.

![DataSet Columns Form](img/v4_media_columns_form.png)

- Inclou un **Encapçalament** per identificar aquesta Columna.
- Usa el menú desplegable per seleccionar un **Tipus** de Columna a usar.

### Tipus de Columna:

#### Valor

Ingressa una llista d'elements per presentar en un quadre combinat.

- Usa el menú desplegable per seleccionar el **Tipus de Dades**.
- Proporciona una llista separada per comes de valors que es poden seleccionar per a aquesta columna.
- Estableix la posició en què aquesta Columna ha d'aparèixer al veure/editar Dades.
- Proporciona un missatge d'informació sobre eines opcional per mostrar a l'ingressar dades per a aquesta columna.

Usa les opcions addicionals per habilitar **Filtres**, **Ordenació** i **Valors Requerits** per a aquesta columna.

#### Fórmula

Ingressa una declaració MySQL.

- Usa el menú desplegable per seleccionar el Tipus de Dades.
- Estableix la posició en què aquesta Columna ha d'aparèixer al veure/editar Dades.
- Proporciona una declaració MySQL adequada per usar en una declaració 'SELECT' o una cadena per formatar un camp de data.

{tip}
`	$dateFormat(<col>,<format>,<idioma>)`
	Assegura't que `<col>` tingui una data i hora especificades perquè funcioni el format de data. Si no s'ha configurat l'idioma, per defecte serà Anglès.

Dos substitucions estan disponibles per columnes de Fórmula: `[DisplayId]` i `[DisplayGeoLocation]` que se substituiran en temps d'execució amb l'ID de Pantalla / Ubicació Geo de Pantalla (MySQL GEOMETRY).
{/tip}

Usa les opcions addicionals per habilitar **Filtres** i **Ordenació** per a aquesta columna.

#### Remot

Proporciona una cadena de sintaxi JSON.

- Usa el menú desplegable per seleccionar el Tipus de Dades.
- Ingressa una cadena de sintaxi JSON que mostri com accedir a les dades d'una font de dades de tercers.
- Estableix la posició en què aquesta Columna ha d'aparèixer al veure/editar Dades.

Usa les opcions addicionals per habilitar **Filtres** i **Ordenació** per a aquesta columna.

Continua afegint i configurant Columnes segons sigui necessari. No hi ha límit teòric per al nombre de Columnes que [[PRODUCTNAME]] pot suportar, encara que un Conjunt de Dades més petit és sovint més fàcil de gestionar i mostrar.

{tip}
Les Columnes es poden veure/afegir i editar usant el menú de fila per a un registre de Conjunt de Dades des de la pàgina de Conjunts de Dades.

L'ordre i el contingut de la llista de Columnes es poden canviar després que s'hagin recopilat les Dades.
{/tip}

## Afegint Dades a les Columnes

Un cop que s'han definit les Columnes, s'han d'afegir dades. Això es pot aconseguir de diverses maneres:

- Manualment a través de la interfície d'usuari del CMS
- Importat a través d'un fitxer CSV
- Usant l'API
- Sincronització Remota

### Manualment

Les dades s'afegeixen usant el botó **Veure Dades** a la pàgina de Columnes.

{tip}
¡Les dades es poden veure/afegir i editar usant el menú de fila per a un registre de Conjunt de Dades des de la pàgina de Conjunts de Dades!
{/tip}

La taula de dades mostrarà cadascuna de les Columnes afegides al Conjunt de Dades tal com s'han configurat.

![Dataset Row](img/v4_media_dataset_row.png)

- Afegeix una nova fila de dades fent clic al botó **Afegir Fila** i completa per a cada tipus de Columna no fórmula.
- Fes clic en **Següent** per continuar afegint dades per afegir més files.
- Quan s'hagin completat totes les dades, fes clic en **Guardar**

{tip}
Fes clic en qualsevol fila per Editar Dades. Fes clic a la creu al final d'una fila seleccionada per Eliminar.

Els Usuaris poden canviar a un **Mode de Selecció Múltiple** usant el botó a la part superior de la quadrícula. En aquest mode, els Usuaris poden seleccionar múltiples files i fer clic en **Eliminar Files** per eliminar en bloc.

Un cop complet, fes clic al botó **Mode d'Edició** per sortir del mode de selecció múltiple.
{/tip}

### Important un CSV

El CMS té un importador CSV de Conjunt de Dades que es pot usar per extreure dades d'un **fitxer CSV** i posar-los en un Conjunt de Dades. La funció **Importar CSV** es pot accedir a través del menú de fila de qualsevol registre de Conjunt de Dades (amb l'excepció de Conjunts de Dades configurats per fonts de dades Remotes).

![Dataset Import CSV](img/v4_media_dataset_importcsv_form.png)

L'importador té opcions per sobreescriure les dades existents contingudes en el fitxer d'importació, així com una opció per ignorar la primera fila del CSV l'importar si el teu fitxer té encapçalaments.

Les Columnes Remotes en el Conjunt de Dades s'enumeraran amb un camp al costat d'elles per indicar el nombre de columna en el fitxer CSV que correspon amb l'Encapçalament de Columna llistat.

{tip}
És important assegurar que el teu fitxer CSV tingui la codificació de fitxer correcta si estàs usant caràcters no ASCII. Els caràcters no ASCII són molt comuns per idiomes fora de l'anglès. La codificació de fitxer més comunament utilitzada és UTF-8.

Si has editat el teu fitxer CSV usant Excel, necessitaràs assegurar-te de seleccionar "Unicode (UTF-8)" des de Eines -> Opcions Web -> pestanya Codificació en el diàleg 'Guardar com'.
{/tip}

### A través de l'API

Pots escriure la teva pròpia aplicació que sincronitzi dades en un Conjunt de Dades usant l'API de [[PRODUCTNAME]]. Les dades es poden afegir fila per fila o important estructures JSON completes.

{nonwhite}
Es pot veure més discussió sobre l'API a la [documentació per a Desenvolupadors](/docs/developer).
{/nonwhite}

### Remotament

Els Conjunts de Dades Remots es mantenen sincronitzats amb una Tasca anomenada **Obtenir Conjunts de Dades Remots**. Aquesta tasca està configurada per defecte i s'executa una vegada per minut.

- #### Dependents

  Un Conjunt de Dades remot pot dependre d'un altre Conjunt de Dades per formular la seva sol·licitud. Cada fila en el Conjunt de Dades dependent s'utilitzarà per crear una sol·licitud utilitzant els paràmetres de sol·licitud del Conjunt de Dades principal.

## Menú de Fila

Cada Conjunt de Dades té un menú de fila on els Usuaris poden accedir a una llista d'accions/dreceres.

- Les configuracions notables s'enumeren a continuació:

### Veure RSS

Crea el teu propi feed RSS usant les dades contingudes en un Conjunt de Dades.

- Selecciona **Veure RSS** des del menú de fila d'un Conjunt de Dades.
- Fes clic al botó **Afegir RSS**.

![Add RSS](img/v4_media_datasets_add_rss.png)

- Completa els camps del formulari, seleccionant les Columnes a usar.
- Al Guardar es generarà una URL que es pot copiar i afegir al Widget [Ticker](media_module_ticker.html).

### Eliminar

Els Conjunts de Dades només es poden eliminar si no estan en ús.

Múltiples Conjunts de Dades es poden seleccionar i eliminar en bloc usant l'opció Amb Seleccionats a la part inferior de la quadrícula de Conjunts de Dades.

### Compartir

Estableix opcions de Compartir per accés d'Usuari/Grup d'Usuaris a Conjunts de Dades individuals.

{nonwhite}
Fes un cop d'ull a la nostra guia per veure un exemple de com utilitzar Conjunts de Dades per a les teves Pantalles: [Usant Conjunts de Dades per mostrar pròxims aniversaris](https://community.xibo.org.uk/t/using-datasets-to-show-upcoming-birthdays/31617)
{/nonwhite}

#### Següent...

[Widget de Conjunt de Dades](media_module_dataset.html)

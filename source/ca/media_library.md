---
toc: "media"
maxHeadingLevel: 3
minHeadingLevel: 2
aliases:
  - "media"
  - "media_tidylibrary"
  - "media_resizing_images"
excerpt: "Gestiona mitjans basats en fitxers des de la Biblioteca del CMS"
keywords: "pujar mitjans a biblioteca, afegir mitjans via url, dates de venciment de biblioteca de mitjans, retirar mitjans, habilitar recol·lecció d'estadístiques de mitjans, actualitzar mitjans, reemplaçar mitjans, informe d'ús, netejar biblioteca, llista de purga, programació"
---

# Biblioteca de Mitjans

[[PRODUCTNAME]] admet una àmplia varietat de tipus de mitjans, des de Widgets que es creen i emmagatzemen directament en Dissenys i Llistes de Reproducció fins a mitjans basats en fitxers que es pugen i emmagatzemen a la Biblioteca del CMS que després es poden reutilitzar a través de múltiples Dissenys i Llistes de Reproducció.

{version}
**NOTA:** [[PRODUCTNAME]] no pren mesures per controlar quin contingut es col·loca a les teves Pantalles. És la teva responsabilitat assegurar que el teu contingut sigui material apropiat per a la teva audiència desitjada. El contingut ha d'atribuir-se adequadament si no en posseeixes els drets.
{/version}

Gestiona tots els mitjans basats en fitxers seleccionant **Mitjans** sota la secció **Biblioteca** del menú principal del CMS:

![Media Library](img/v4_media_library_grid.png)

Usa els múltiples camps de filtre a la part superior de la quadrícula per restringir els criteris per als resultats retornats.

{tip}
Usa l'opció **O/I** per a **Noms** i per filtrar elements que s'han assignat a múltiples **Etiquetes**.

Les Imatges i Vídeos que tenen una miniatura configurada també es poden filtrar per **Orientació** un cop configurada:

- Usa el menú de fila per a l'element i selecciona **Editar** per un fitxer d'Imatge/Vídeo.

- Desplaça't fins a la part inferior del formulari i estableix l'**Orientació** prevista.
{/tip}

## Afegint Mitjans a la Biblioteca

Els mitjans de la biblioteca es poden pujar directament usant el botó **Afegir Mitjans** o proporcionant una URL usant el botó **Afegir Mitjans (URL)**.

{tip}
Afegeix Mitjans a la Biblioteca del CMS i guarda en Carpetes per tenir mitjans llestos per usar per als Usuaris/Grups d'Usuaris apropiats!

Els fitxers afegits a la Biblioteca del CMS es poden afegir fàcilment a Dissenys i Llistes de Reproducció usant una [Cerca a la Biblioteca](layouts_editor_library_search)
{/tip}

### Afegir Mitjans (Pujar)

- Selecciona el botó **Afegir Mitjans**

  ![Upload Media](img/v4_media_library_upload.png)

- Fes clic a **Afegir fitxers** i selecciona el(s) fitxer(s) que desitges pujar.

{tip}
Es poden especificar llindars i límits predeterminats que després es consideren en el cas que una [Imatge](media_module_image.html) hagi de redimensionar-se al pujar una imatge, per exemple. Es pot trobar més informació en **Configuració del CMS**.
{/tip}

- Dóna-li al teu fitxer un **Nom** per una identificació més fàcil en el CMS.

{tip}
Si el camp Nom es deixa en blanc, el fitxer es nomenarà segons el nom del fitxer original al pujar!
{/tip}

Puja fitxers a una ubicació de Carpeta especificada per heretar les opcions de Veure, Editar, Eliminar Compartir que s'han aplicat a la Carpeta de destí per un fàcil accés d'Usuari/Grup d'Usuaris:

- Fes clic al botó **Seleccionar Carpeta** i expandeix per seleccionar la Carpeta en la qual guardar.

- Fes clic a la Carpeta a la qual desitges pujar el fitxer i fes clic a **Fet**.
- La **Carpeta Actual** ara mostrarà la ruta del fitxer seleccionat.

- Fes clic al botó **Iniciar càrrega** per començar la càrrega de tots els fitxers. Si s'ha seleccionat una Carpeta i has afegit múltiples fitxers, tots els fitxers es pujaran a aquesta ubicació.

Els fitxers també es poden pujar individualment i tenir diferents ubicacions de Carpeta especificades:

- En lloc de fer clic al botó Iniciar càrrega, fes clic al botó **càrrega blau** que es mostra al final de la fila per un fitxer afegit.

- Canvia la ubicació de la Carpeta usant el botó **Seleccionar Carpeta** com abans i després fes clic al botó blau al final de la fila per pujar només aquest fitxer singular.

![Single Upload](img/v4_media_library_single_upload.png)

- Un cop que tots els fitxers s'hagin pujat amb èxit, fes clic a **Fet**.

{tip}
Els fitxers de mitjans també es poden pujar directament a Dissenys/Llistes de Reproducció usant l'eina de càrrega des d'una Cerca a la Biblioteca. Els mitjans pujats a una Llista de Reproducció tenen una opció addicional per establir [Dates de Venciment de Widget](media_playlists.html#content-widget-expiry-dates).

Els fitxers de mitjans que es pugen i afegeixen directament a Dissenys/Llistes de Reproducció també es guarden per defecte a la Biblioteca de Mitjans del CMS.
{/tip}

### Afegir Mitjans via URL

- Selecciona el botó **Afegir Mitjans (URL)**:

![Upload via URL](img/v4_media_library_upload_url.png)

- Guarda en una Carpeta per heretar les opcions de Veure, Editar, Eliminar Compartir que s'han aplicat a la Carpeta de destí per un fàcil accés d'Usuari/Grup d'Usuaris.
- Proporciona la URL remota per al fitxer.
- Dóna-li al teu fitxer un **Nom** per una identificació més fàcil en el CMS.

{tip}
Si el camp Nom es deixa en blanc, el fitxer es nomenarà segons el nom del fitxer original!
{/tip}

- Fes clic a **Guardar**.

## Menú de Fila

Cada element a la **Biblioteca** té un menú de fila on els Usuaris poden accedir a una llista d'accions/dreceres

## Editar

Selecciona **Editar** per fer canvis en les ubicacions de **Carpeta**, **Durades** i **Etiquetes** i altres configuracions.

- Les configuracions notables s'enumeren a continuació:

### Dates de Venciment

Estableix una Data de Venciment per als Mitjans de la Biblioteca per eliminar el fitxer de qualsevol Disseny/Llista de Reproducció en el que s'hagi utilitzat.

### Retirar Mitjans

Marcar **Retirar aquest Mitjà** mantindrà el fitxer de mitjans assignat a qualsevol Disseny/Llista de Reproducció existent però no estarà disponible per a una selecció addicional per afegir a Dissenys/Llistes de Reproducció.

### Habilitar Recol·lecció d'Estadístiques de Mitjans

- Estableix la recol·lecció d'estadístiques de [Prova de Reproducció](displays_metrics.html#proof_of_play) en Encès / Apagat / Heretar per al fitxer de mitjans seleccionat.

{tip}
Assegura't que **Habilitar Informes d'Estadístiques** s'hagi marcat en Configuració de Pantalla per recopilar estadístiques de Prova de Reproducció!
{/tip}

### Actualitzar Mitjans

Usa la casella de verificació **Actualitzar aquest Mitjà en tots els Dissenys als quals està assignat** perquè qualsevol edició es reflecteixi en els Dissenys/Llistes de Reproducció als quals aquest fitxer de mitjans està assignat actualment.

{tip}
Les edicions només s'actualitzaran en Dissenys/Llistes de Reproducció que tinguis accés per editar!
{/tip}

### Reemplaçar Mitjans

Pot ser necessari pujar una nova revisió d'un fitxer existent usant el botó **Reemplaçar** a la part inferior del formulari.

- Puja un fitxer de reemplaçament usant els mateixos passos que abans per [Afegir Mitjans (Pujar).](media_library.html#content-add-media-upload)
- Marca per **Actualitzar** el fitxer de reemplaçament a tots els Dissenys/Llistes de Reproducció als quals està assignat actualment.
- Marca per **Eliminar** la versió anterior del fitxer completament del CMS.

## Eliminar

Els fitxers de mitjans només es poden eliminar del CMS si **no** s'estan utilitzant en cap **Disseny/Llista de Reproducció** existent.

{version}
L'opció per forçar una eliminació ha d'usar-se amb precaució ja que eliminar un fitxer no es pot revertir.
{/version}

{tip}
[Retirar Contingut](media_library.html#content-retire-media) en lloc d'eliminar-lo mantindrà el fitxer de mitjans en qualsevol Disseny/Llista de Reproducció existent al qual s'hagi assignat, amb qualsevol contingut programat no afectat. Els mitjans no estaran disponibles per afegir a nous Dissenys/Llistes de Reproducció.
{/tip}

{feat}Purge List|v4{/feat}

- Marca a la casella per habilitar una empenta forta usant XMDS per eliminar completament el fitxer de l'emmagatzematge local d'un Reproductor.

### Informe d'Ús

{tip}
Aquest informe és excel·lent per usar per fer comprovacions finals abans de netejar fitxers de mitjans!
{/tip}

Això mostrarà si el **fitxer de mitjans** seleccionat està assignat/programat directament a **Pantalles**.

![Library Usage Report](img/v4_media_library_usage_report.png)

- Usa la pestanya Disseny per veure en quins **Dissenys** està inclòs actualment el fitxer de mitjans.

### Programació

Els fitxers de mitjans d'Imatge i Vídeo de la Biblioteca es poden Programar directament a una Pantalla com contingut de pantalla completa des del menú de fila.

- Fes clic a **Programació**

![Schedule Library Media](img/v4_media_library_schedule_fullscreen.png)

- Estableix la **Durada** de l'element per determinar quant de temps ha d'いてrar-se aquest fitxer de mitjans cada vegada que apareix a la programació. Usa la durada, tal com s'estableix a la Biblioteca de Mitjans deixant aquest camp en blanc.
- Opcionalment selecciona una **Resolució** per usar. Si es deixa en blanc, s'usarà una resolució que coincideixi més en mida amb el fitxer de mitjans seleccionat.
- Es pot establir un **Color de Fons** opcional per omplir qualsevol buit si el mitjà no omple tota la pantalla.
- **Guardar**
- Completa la resta dels camps del formulari per completar la nova Programació.

## Netejar Biblioteca

A mesura que s'usa el CMS i s'afegeixen Dissenys/Llistes de Reproducció i Mitjans, amb el temps la Biblioteca pot omplir-se de contingut antic que ja no està en ús.

La Biblioteca pot ser *netejada* per un Usuari o Super Administrador perquè es mantingui neta i petita.
**Les accions no es poden revertir, per la qual cosa això ha d'usar-se amb precaució.**

{tip}
Això podria ser particularment útil si el CMS està instal·lat en un servidor web que té quotes o si als Usuaris se'ls han assignat les seves pròpies quotes!
{/tip}

Hi ha dos llocs on es pot netejar la Biblioteca:

1. Des de **Configuració del CMS** - disponible només per a tots els Super Administradors.
2. Des de la **Biblioteca** - per a tots els Usuaris quan **Habilitar Neteja de Biblioteca** està marcat.

{nonwhite}
{cloud}
La funció Netejar Biblioteca està desactivada per defecte per clients de **Xibo Cloud Hosting** ja que pot ser potencialment destructiva si les opcions no s'entenen completament. Usa la casella de verificació per habilitar si és necessari.
{/cloud}
{/nonwhite}

Un cop habilitat, els Usuaris poden fer clic a un botó **Netejar Biblioteca** ubicat a la part superior de la pàgina de la Biblioteca:

![Tidy from Library](img/v4_media_library_tidylibrary.png)

El formulari mostrarà el nombre de fitxers que s'eliminaran i quant espai ocupen aquests fitxers.

{tip}
Això només eliminarà fitxers que són propietat de l'Usuari connectat que ja no estan en ús en un Disseny o Assignats a un Grup de Pantalles/Pantalla.
{/tip}

#### Següent...

[Mòduls i Connectors](media_modules.html)
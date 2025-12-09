---
toc: "media"
maxHeadingLevel: 3
minHeadingLevel: 2
aliases:
  - "layouts_timeline"
  - "media_module_spacer"
  - "media_module_text"
excerpt: "Les Llistes de Reproducció contenen una línia de temps de contingut ordenat que pot reutilitzar-se en múltiples Dissenys"
keywords: "reutilitzable, presentació de diapositives, afegir múltiples elements, mostrar una seqüència de contingut, programar llistes de reproducció, llista de reproducció dinàmica, editor de llista de reproducció, widget espaciador, widget de text, dates de venciment de widget, spots, ordre de reproducció, incrustar llistes de reproducció"
---

# Llistes de Reproducció

Les Llistes de Reproducció s'utilitzen per mostrar una seqüència d'elements multimèdia (com una presentació d'imatges). Hi ha dues formes de crear una Llista de Reproducció:

- Crear [Llistes de Reproducció](media_playlists) de forma independent a un Disseny. Les Llistes de Reproducció Globals poden programar-se en Pantalles sense la creació d'un Disseny. Les Llistes de Reproducció creades fora de l'Editor de Dissenys encara es mostren per a la seva selecció des de la funció Afegir Llista de Reproducció des de l'Editor de Dissenys.
- Afegir Llistes de Reproducció directament a un Disseny des de l'Editor de Dissenys. Les Llistes de Reproducció Locals poden convertir-se per guardar-se per a la seva reutilització com una Llista de Reproducció global. Les Llistes de Reproducció guardades es mostraran en l'Editor de Dissenys per afegir als Dissenys.

## Resum de Característiques:

- Crear i configurar independentment dels Dissenys.
- Afegir i mantenir contingut [dinàmicament](media_playlists.html#content-dynamically-adding-media).
- Actualitzar contingut de Llista de Reproducció sense accedir als Dissenys.
- Programar directament des de la quadrícula de Llistes de Reproducció sense necessitat d'afegir a un Disseny.
- Combinar contingut d'una varietat de Llistes de Reproducció per mostrar.
- Establir el nombre màxim d'elements a mostrar d'una Llista de Reproducció.
- Controlar quant de temps ha de mostrar-se cada element en una Llista de Reproducció abans de passar al següent element.
- Establir Dates de Venciment per elements multimèdia afegits a una Llista de Reproducció.

## Creant una Llista de Reproducció

Optimitza recursos i estalvia temps creant Llistes de Reproducció per mantenir múltiples elements de contingut per mostrar en Pantalles. Crea Llistes de Reproducció per dirigir i recopilar contingut per requisits específics, ubicacions, categories de temes, etc.

Les Llistes de Reproducció que es creen independentment dels Dissenys i no requereixen accés addicional d'Usuari a Dissenys o a l'Editor de Dissenys per afegir o gestionar contingut en Llistes de Reproducció. Qualsevol canvi realitzat en una Llista de Reproducció s'actualitzarà en tots els Dissenys/Programacions que ja contenen aquesta Llista de Reproducció.

- Selecciona **Llistes de Reproducció** sota la secció **Biblioteca** del menú principal del CMS.

- Fes clic al botó **Afegir Llista de Reproducció** i completa els camps del formulari:

![Add Playlist](img/v4_media_playlists_add.png)

- Dóna-li a la teva Llista de Reproducció un **Nom** per una identificació fàcil en el CMS.

Hi ha dues opcions per afegir contingut de [Mitjans](media_library) a Llistes de Reproducció:

- Assignar automàticament mitjans basats en Biblioteca segons criteris usant l'opció [Dinàmica](media_playlists.html#content-dynamically-adding-media).
- Assignar manualment mitjans usant l'[Editor de Llistes de Reproducció](media_playlists.html#content-media-playlists), que s'obrirà al guardar el formulari.

## Afegint Mitjans Dinàmicament

- Un cop marcat, fes clic a la pestanya **Filtre** i estableix els criteris requerits per poblar Mitjans de Biblioteca coincidents.
- Proporciona un **nombre màxim** de fitxers de Mitjans de Biblioteca per limitar el nombre que pot assignar-se automàticament.

Es mostraran els Mitjans ja a la Biblioteca del CMS que coincideixen amb els criteris establerts:

![Dynamic Assignment](img/v4_media_playlists_dynamic.png)

Qualsevol fitxer de mitjans futur que s'afegeixi a la Biblioteca que compleixi amb els criteris establerts per aquesta Llista de Reproducció s'afegirà automàticament a aquesta llista.

{tip}
Els Mitjans de Biblioteca també poden prepoblar-se com una assignació única a una Llista de Reproducció establint criteris però deixant l'opció Dinàmica desmarcada!
{/tip}

- Fes clic a **Guardar**.

{tip}
Sabies que una Llista de Reproducció Dinàmica pot programar-se per mostrar-se a Pantalles a pantalla completa sense afegir-la primer a un Disseny? Usa el menú de fila per la Llista de Reproducció i selecciona Programar!
{/tip}

## Editor de Llistes de Reproducció

- Des de la Caixa d'Eines, selecciona contingut per afegir a la Llista de Reproducció.
- Les opcions de configuració es carregaran en el panell de propietats.

![Playlist Timeline](img/v4_media_playlists_timeline.png)

{tip}
L'**Editor de Llistes de Reproducció** conté dos Widgets addicionals, un **Editor de Text Enriquit** per proporcionar text, Html o JavaScript i un **Espaciador** per crear un 'espai' buit dins d'una Llista de Reproducció.
{/tip}

Les durades s'actualitzaran per mostrar els minuts/segons a mesura que s'afegeixen elements a la línia de temps de la Llista de Reproducció.

- Reordena la seqüència arrossegant i deixant anar.

- Fes clic a la icona de regla per **Canviar mode d'Escala**:

![Scale Mode](img/v4_media_playlists_scale_mode.png)

Usa les opcions d'escala per apropar i allunyar per disminuir/augmentar el lapse de temps visible.

Els elements poden afegir-se a un punt específic en la llista, arrossega o fes clic per afegir contingut a un marcador de posició dins de la Llista de Reproducció.

![Add to Timeline](img/v4_media_playlists_add_timeline.png)

{tip}
Usa el botó Desfer a la part inferior de la barra d'eines per revertir un canvi.
{/tip}

Es pot accedir a un Menú Contextual addicional d'opcions fent clic dret en un element que inclou establir [Dates de Venciment de Widget](media_playlists.html#content-widget-expiry-dates) i Transicions de Llista de Reproducció.

{tip}
Quan les Transicions s'apliquen a un Widget per defecte, el panell de propietats estarà en blanc. Només les Transicions ingressades manualment es mostraran en els formularis!
{/tip}

Usa el botó **Seleccionar Múltiples Widgets** a la part inferior de l'Editor de Llistes de Reproducció per eliminar múltiples seleccions amb un sol clic:

![Mutli Select](img/v4_media_playlists_multi_select.png)

{tip}
Sabies que una Llista de Reproducció 'global' pot programar-se per mostrar-se a Pantalles a pantalla completa sense afegir-la primer a un Disseny? Usa el menú de fila per la Llista de Reproducció i selecciona Programar!
{/tip}

## Dates de Venciment de Widget

Els elements afegits a una Llista de Reproducció tenen una opció addicional d'establir temps d'Inici i Fi.

{feat}Widget Expiry Dates|v4{/feat}

- Fes clic dret en un element en una Llista de Reproducció per **Editar Dates de Venciment** o establir al pujar mitjans directament a una Llista de Reproducció.

Pujar des d'una [Cerca a la Biblioteca](layouts_editor_using_library_search.html) tindrà una opció addicional **Establir Data de Venciment**:

![Expiry Dates](img/v4_media_playlists_upload_expiry.png)

Al pujar múltiples fitxers de mitjans, fer clic al botó **Iniciar càrrega** pujarà tots els fitxers amb la mateixa data/hora i ubicació de Carpeta establertes.

{tip}
Els elements també poden pujar-se individualment usant el botó **càrrega blau** al final de la fila perquè un fitxer tingui diferents Dates de Venciment i ubicacions de Carpeta establertes per a cada fitxer pujat.
{/tip}

Qualsevol element en una Llista de Reproducció que tingui **Dates de Venciment** establertes mostra una icona, que al passar el ratolí mostrarà més informació:

![Expiry Dates](img/v4_media_playlists_expiry_dates.png)

{tip}
Un cop que la data de Finalització ha passat, l'element s'eliminarà de la Llista de Reproducció. Els elements vençuts que no s'hagin configurat per Eliminar al Vèncer romandran visibles en l'Editor de Llistes de Reproducció només perquè els temps d'Inici i Fi puguin reajustar-se si és necessari.
{/tip}

- Fes clic a una icona per obrir i realitzar qualsevol canvi/eliminar de l'element.

## Incrustant Llistes de Reproducció

Les Llistes de Reproducció es poden afegir a altres línies de temps de Llistes de Reproducció per definir que tant contingut ha de mostrar-se, per quant de temps, així com determinar un ordre de reproducció.

- Des de l'Editor de Llistes de Reproducció selecciona afegir una Nova o selecciona de la llista de Llistes de Reproducció 'globals' disponibles des de la Caixa d'Eines.
- Les opcions de configuració es mostren al Panell de Propietats:

![Embedding Playlists](img/v4.1_media_playlists_embedding.png)

- Usa el menú desplegable per seleccionar **Llistes de Reproducció** usant el botó `+` per afegir i configurar múltiples Llistes de Reproducció si és necessari.

- Les opcions de **Spot** s'utilitzen per definir que tant contingut de les Llistes de Reproducció ha de mostrar-se i per quant de temps.

Els Spots també tenen una opció per usar el contingut d'una Llista de Reproducció com farcit només i afegir contingut d'aquesta Llista de Reproducció per **Omplir** o **Farcir** altres Llistes de Reproducció seleccionades:

- Aquesta Llista de Reproducció ha de ser la **primera** Llista de Reproducció afegida a la llista.
- Ingressa un **0** al camp **Spots** perquè tota la Llista de Reproducció sigui ignorada i omesa de l'ordre de reproducció. Selecciona com ha de distribuir-se el contingut d'aquesta Llista de Reproducció amb les altres Llistes de Reproducció usant les opcions **Farcit de Spot**.

{version}
**Nota:** Tingues en compte que al establir **Dates d'Inici** als Widgets pot causar que es mostrin menys Spots que la quantitat total especificada.
{/version}

Usa el menú desplegable per al camp **Farcit de Spot** per seleccionar com han d'omplir-se els Spots restants en el cas que no hi hagi suficients Widgets a la Llista de Reproducció seleccionada per complir amb els spots de reproducció especificats.

{tip}
¡**Spots**, **Durada de Spot** i **Farcit de Spot** són tots opcionals i poden deixar-se en blanc si aquesta funcionalitat no és requerida!
{/tip}

Usa el desplegable per **Ordre de Llista de Reproducció** per seleccionar com han d'ordenar-se totes les Llistes de Reproducció per reproduir-se.

{tip}
**Auto** usa el recompte total d'elements a cada llista i ho divideix per la llista més petita per determinar amb quina freqüència prendre elements de cada llista per assegurar una reproducció uniforme de cada Llista de Reproducció.
{/tip}

Selecciona de les opcions **Widgets Restants** per gestionar qualsevol contingut que quedi sense ordenar al final d'una Llista de Reproducció.

{tip}
Afegir Llistes de Reproducció a una **Nova Llista de Reproducció** en un Disseny té una opció addicional de Reproducció Basada en Cicles que inclou una funció de **Widget Aleatori**.
¡La reproducció basada en cicles no és compatible al afegir Llistes de Reproducció a una Llista de Reproducció global!
{/tip}

## Quadrícula de Llista de Reproducció

Les Llistes de Reproducció guardades es poden veure des de **Llistes de Reproducció** sota la secció **Biblioteca** del menú principal del CMS:

![Playlist Grid](img/v4.1_media_playlists_grid.png)

Cada Llista de Reproducció té un menú de fila que s'utilitza per accedir a un menú d'accions/dreceres, les configuracions notables s'enumeren a continuació:

- **Línia de Temps** - obre l'Editor de Llistes de Reproducció per fer canvis en el contingut a la línia de temps.
- **Editar** - usa la pestanya Filtre per Llistes de Reproducció Dinàmiques per veure la llista de mitjans assignats dinàmicament i fer canvis en els criteris.
- **Informe d'ús** - veu on es mostren les Llistes de Reproducció i en quins Dissenys s'han inclòs.
- **Programar** - Programa directament una Llista de Reproducció perquè es mostri a pantalla completa en Pantalles.

{tip}
Qualsevol canvi realitzat en una Llista de Reproducció Programada s'enviarà automàticament als Reproductors a mesura que es realitzin.
{/tip}

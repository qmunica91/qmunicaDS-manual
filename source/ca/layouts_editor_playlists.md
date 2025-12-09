---
toc: "layouts"
maxHeadingLevel: 3
minHeadingLevel: 2
aliases: 
   - "media_module_subplaylist"   
excerpt: "Crea o Afegeix Llistes de Reproducció directament a un Disseny des de l'Editor de Dissenys"
keywords: "línia de temps de contingut, passi de diapositives, clau de sincronització de contingut, afegint llistes de reproducció a un disseny, convertir llista de reproducció, llista de reproducció guardada, reproducció basada en cicles, widget aleatori"
persona: "content creator, super administrator, user"
---

# Llistes de Reproducció

Les Llistes de Reproducció s'usen per mostrar una seqüència d'elements multimèdia (com una presentació d'imatges). Hi ha dues formes de crear una Llista de Reproducció:

- Afegir Llistes de Reproducció directament a un Disseny des de l'Editor de Dissenys. Les Llistes de Reproducció locals es poden convertir per guardar-les per a la seva reutilització com una Llista de Reproducció global. Les Llistes de Reproducció guardades es mostraran en l'Editor de Dissenys per afegir-les als Dissenys.
- Crear [Llistes de Reproducció](media_playlists.html#content-creating-a-playlist) independentment d'un Disseny. Les Llistes de Reproducció globals poden programar-se en Pantalles sense la creació d'un Disseny. Les Llistes de Reproducció creades fora de l'Editor de Dissenys encara es mostren per a selecció des de la funció Afegir Llista de Reproducció de l'Editor de Dissenys.

## Afegir Llistes de Reproducció

Crea noves o selecciona Llistes de Reproducció existents per usar des de l'**Editor de Dissenys** per crear una línia de temps de contingut per mostrar en un Disseny.

## Resum de Característiques:

- Crea i configura directament en un Disseny.
- Converteix una Llista de Reproducció creada en un Disseny a una Llista de Reproducció Global per guardar-la per a ús futur.
- Mostra fàcilment un 'passi de diapositives' de contingut contingut en una o més Llistes de Reproducció.
- Sincronitza amb Llistes de Reproducció en altres Dissenys que són part d'un Esdeveniment Sincronitzat.
- Combina contingut d'una varietat de Llistes de Reproducció per mostrar.
- Estableix el nombre màxim d'elements a mostrar d'una Llista de Reproducció.
- Controla quant temps ha de mostrar-se cada element en una Llista de Reproducció abans de passar al següent element.
- Estableix Dates de Caducitat per elements multimèdia afegits a una Llista de Reproducció.
- Reprodueix un element per cicle per a un recompte de reproducció especificat.
- Selecciona un Widget Aleatori per reproduir en cada cicle.
- Cicla a través dels elements continguts en una Llista de Reproducció en el visor per veure fàcilment la seqüència.

## Afegint Llistes de Reproducció a un Disseny

- Des de l'[Editor de Dissenys](layouts_editor), fes clic en **Afegir Llistes de Reproducció** des de la **Caixa d'Eines**:

![Add Playlists](img/v4.1_layouts_editor_add_playlists.png)

- Fes clic per Afegir o arrossega una **Nova Llista de Reproducció** o una Llista de Reproducció amb nom que ja hagi estat creada.
- Redimensiona i posiciona:

![Content Synchronisation Key](img/v4.1_layouts_editor_synchronisation_key.png)

Des del **Panell de Propietats**, usa la **Clau de Sincronització de Contingut** per sincronitzar amb Llistes de Reproducció en altres Dissenys. Les Llistes de Reproducció amb la mateixa clau es sincronitzaran quan el Disseny es programi com un [Esdeveniment Sincronitzat.](scheduling_events.html#content-synchronised-events)

{tip}
**Escenari:**

Tens un Esdeveniment Sincronitzat amb 3 Pantalles i 3 Dissenys diferents. Cada Disseny té un Text a la part superior i una Llista de Reproducció al mig que les 3 necessiten reproduir en sincronia. 

També podries establir dues Llistes de Reproducció diferents per sincronitzar de manera diferent, el que podries establir en `sync_1` i `sync-2` per exemple.
{/tip}

- Opcionalment, estableix **Transicions** per elements en una Llista de Reproducció des del Panell de Propietats.

{tip}
Quan s'han aplicat Transicions per defecte, el panell de propietats estarà en blanc. Només les Transicions ingressades manualment es mostraran en els formularis.
Els valors predeterminats poden anul·lar-se desmarcant la casella de verificació **Aplicar Transicions automàticament** des del Panell de Propietats per al Disseny.
{/tip}

- Fes clic a la icona a la cantonada dreta de la Llista de Reproducció per obrir l'[Editor de Llistes de Reproducció](media_playlists.html#content-playlist-editor) per afegir i configurar contingut.

{tip}
L'[Editor de Llistes de Reproducció](media_playlists.html#content-playlist-editor) inclou Widgets d'**Espaiador** i **Text Enriquit** que només estan disponibles per al seu ús amb Llistes de Reproducció.

Els mitjans afegits a una Llista de Reproducció també poden tenir hores d'Inici i Fi usant [Dates de Caducitat](media_playlists.html#content-widget-expiry-dates).
{/tip}

{version}
**Nota:** Si afegeixes una Llista de Reproducció amb nom que ja ha estat creada, qualsevol edició realitzada en la Llista de Reproducció s'aplicarà a tot arreu on s'estigui utilitzant la Llista de Reproducció actualment.
{/version}

- Fes clic al botó **Enrere** a la part superior per sortir de l'Editor de Llistes de Reproducció i tornar a l'Editor de Dissenys.

Mira tot el contingut que s'ha afegit a la Línia de Temps de la Llista de Reproducció utilitzant les fletxes a la part inferior dreta de la Llista de Reproducció en el Disseny.

- Cicla a través de l'ordre del contingut:

![Preview Timeline Content](img/v4.1_layouts_editor_playlists_preview_content.png)

## Convertir Llista de Reproducció

Si afegeixes una **Nova Llista de Reproducció** al Disseny, pots optar per convertir-la en una Llista de Reproducció guardada. Les Llistes de Reproducció convertides es mostraran per a la selecció de Llistes de Reproducció en l'Editor de Dissenys i des de la quadrícula de [Llistes de Reproducció](media_playlists.html#content-playlists-grid).

- Fes clic en la Llista de Reproducció en el Disseny per seleccionar-la i dóna-li un **Nom** des de la pestanya **General** del **Panell de Propietats**.
- Fes clic dret i selecciona **Convertir Llista de Reproducció** des del menú.

![Convert Playlist](img/v4.1_layouts_editor_convert_playlist.png)

Veuràs un missatge emergent a la part inferior de l'Editor de Dissenys per dir que la Llista de Reproducció s'ha guardat com una Llista de Reproducció Global.

{tip}
¡Fes clic al botó **Mostrar més** per veure la teva Llista de Reproducció afegida a la llista de Llistes de Reproducció disponibles!
{/tip}

Les Llistes de Reproducció convertides es guardaran en la [Quadrícula de Llistes de Reproducció](media_playlists.html#content-playlist-grid).

## Afegir a la Llista de Reproducció

Si tens una **Nova Llista de Reproducció** en un Disseny, pots afegir una nova o global Llista de Reproducció a la Línia de Temps per obrir més opcions en el Panell de Propietats per configuració:

![Playlist Spots](img/v4.1_layouts_editor_playlist_spots.png)

- Selecciona Llistes de Reproducció, Opcions de Lloc i Ordenació de Llista de Reproducció, al seleccionar més d'una Llista de Reproducció per [Incrustar](media_playlists.html#content-embedding-playlists) des del Panell de Propietats.

Afegir una **Llista de Reproducció** a una **Nova Llista de Reproducció** en un Disseny té opcions addicionals de [Reproducció Basada en Cicles](layouts_editor_playlists.html#content-cycle-based-playback) que inclou una característica de Widget Aleatori.

{tip}
Si desitges afegir més d'una Llista de Reproducció per combinar l'ordre de reproducció, recomanem que només afegeixis una Llista de Reproducció a la Línia de Temps i després usis les opcions en el Panell de Propietats per seleccionar les Llistes de Reproducció addicionals i configurar.
{/tip}

- ### Reproducció Basada en Cicles

Un cop habilitada, totes les Llistes de Reproducció seleccionades es tractaran com una "llista" i només mostraran un Widget cada cop que es reprodueixi el Disseny, ciclant a través del contingut de totes les Llistes de Reproducció afegides:

- Marca Habilitar reproducció basada en cicles des del Panell de Propietats.
- Proporciona un **Recompte de Reproducció** per determinar quantes reproduccions ha de tenir cada Widget en la Llista de Reproducció abans de passar al següent Widget en la línia de temps.

![Cycle Playback](img/v4.1_layouts_editor_playlist_cycle_playback.png)

Usar l'opció **Widget aleatori en cada cicle** reproduirà un Widget de la línia de temps a l'atzar per a cada cicle.

{version}
**Nota:** ¡Aquestes opcions addicionals **no** estan disponibles al afegir una o més Llistes de Reproducció a una línia de temps de [Llista de Reproducció Global](media_playlists.html#content-feature-overview), que s'ha afegit directament al Disseny!
{/version}

{tip}
¿Sabies que les [Llistes de Reproducció](media_playlists.html) creades i gestionades independentment dels Dissenys no requereixen més drets d'accés d'usuari als Dissenys o a l'Editor de Dissenys per afegir i gestionar contingut?
{/tip}

---
toc: "layouts"
maxHeadingLevel: 3
minHeadingLevel: 2    
excerpt: "Usa Widgets de Dades per crear Dissenys atractius"
keywords: "widgets, widgets de dades, elements, elements de dades, elements globals, grups d'elements, plantilles, dades de suport, plantillas html, plantillas css, plantillas javascript, plantillas personalizadas"
---

# Widgets de Dades

Els Widgets de Dades depenen d'una font de dades externa per mostrar informació en els Dissenys utilitzant **Elements**.

## Resum de Característiques

- Contingut impulsat per font de dades.
- Elements separats permeten flexibilitat.
- Proporcionar dades de suport per mostrar.
- Controlar la paginació de dades amb Espais de Dades.
- Crear Grups per fàcil duplicació.
- Extreure dades d'una font alternativa en el mateix Disseny.
- Utilitzar dissenys prefabricats.

Cada Widget de Dades té un conjunt d'**Elements** que s'alimenten d'una font de dades que permet a l'Usuari flexibilitat en la col·locació de les dades retornades en lloc d'estar obligats a un disseny rígid de **Plantilla Estàtica**:

- Fes clic en un **Widget de Dades** per mostrar tots els **Elements** disponibles.

![Data Elements](img/v4_layouts_data_elements.png)

{version}
**NOTA:** Els Elements de Dades només estan disponibles des de l'Editor de Dissenys i no estan disponibles en l'[Editor de Llistes de Reproducció.](media_playlists.html#content-playlist-editor) No obstant això, els Usuaris poden afegir Widgets de Dades utilitzant Plantilles Estàtiques.
{/version}

### Configurar

Cada Element té un conjunt d'opcions configurables disponibles des del **Panell de Propietats** un cop afegit:

![Element Properties](img/v4_layouts_element_properties.png)

{tip}
Es mostrarà una icona d'exclamació per avisar l'Usuari sobre el que necessita ser accionat. ¡L'exemple anterior encara no té una URL ingressada per a un feed ICS!
{/tip}

Les opcions establertes des de la pestanya **Configurar** s'aplicaran a tots els Elements afegits al Disseny del mateix tipus de Widget.

{tip}
¡Crea una [Nova Configuració](layouts_data_widgets.html#content-new-configuration) per seleccionar dades de fonts de dades alternatives associades amb el Widget!
{/tip}

### Aparença

La pestanya **Aparença** inclou opcions per configurar com han de veure's les dades retornades per l'Element i inclou efectes de transició i configuració d'[Espai de Dades](layouts_data_widgets.html#content-data-slots).

### Dades de Suport

Crea **Dades de Suport** per Widgets de Dades seleccionats i especifica sota quines condicions han de mostrar-se:

![Fallback Data](img/v4_layouts_editor_data_widgets_fallback.png)

- Fes clic en **Afegir Nou**.
- Completa els camps del formulari amb la informació requerida.
- Guardar.

{tip}
¡Les opcions de Dades de Suport variaran depenent del Widget de Dades seleccionat!
{/tip}

### Avançat

La pestanya Avançat s'usa per establir Noms, proporcionar durades específiques, establir el nivell de col·lecció d'estadístiques de prova de reproducció i habilitar elements per repetir-se per omplir tots els [Espais de Dades](layouts_data_widgets.html#content-data-slots).

### Posicionament

Usa la pestanya **Posicionament** (icona de quadrícula) per establir un posicionament precís i Capes.

{tip}
¡Els Elements tenen la seva pròpia Capa de Llenç, que es pot usar per determinar on apareixen en relació amb altres Elements renderitzats nativament com Llistes de Reproducció i Vídeos!
{/tip}

## Espais de Dades

Al afegir més d'un mateix **Element**, gestiona la paginació de les dades retornades especificant un **Espai de Dades** per usar per cada Element:

![Data Slots](img/v4_layouts_editor_data_slots.png)

{tip}
Per exemple, la imatge de dalt mostra que s'han afegit 2 **Elements de Descripció** del **Widget de Calendari**. Un té un **Espai de Dades de 1** i l'altre un **Espai de Dades de 2.** Si es debolevien 10 elements (Esdeveniments de Calendari), l'Espai de Dades 1 mostraria els elements 1,3,5,7,9 amb l'Espai de Dades 2 mostrant els elements 2,4,6,8,10.
{/tip}

Els Espais de Dades s'estableixen des de la pestanya **Aparença** del **Panell de Propietats** per a l'Element seleccionat.

{tip}
¡Afegir més d'un mateix Element augmentarà automàticament el nombre d'**Espai de Dades**!
{/tip}

A més, els Elements tenen l'opció de **Fixar aquest espai** perquè el primer element de dades que aparegui en aquest espai romangui durant tota la durada del Widget i no cicli a través dels elements de dades.

{tip}
¡Els Usuaris poden establir si **Repetir elements** per omplir tots els espais de dades per assegurar que no hi hagi espais buits usant la casella de verificació en la pestanya **Avançat** del Panell de Propietats!
{/tip}

## Agrupant Elements

Agrupa Elements del mateix Widget de Dades junts per facilitar la construcció de dissenys:

- Afegeix Elements al Disseny, posiciona i estilitza usant la pestanya **Aparença**.
- Mantingues pressionada la tecla shift i fes clic en cada Element que vulguis agrupar.
- Un cop seleccionats, deixa anar la tecla shift i fes clic dret.
- Selecciona **Agrupar elements**.

![Grouping Elements](img/v4_layouts_grouping_elements.png)

{tip}
Els Grups també poden incloure **Elements Globals**.
{/tip}

{version}
**NOTA:** ¡Tots els Elements de Dades necessiten compartir el mateix **Espai de Dades** i **Efecte** al agrupar!
{/version}

Els Grups es poden duplicar fàcilment:

- Fes clic dret i selecciona **Duplicar**.

![Duplicated Elements](img/v4_layouts_duplicated_elements.png)

Edita **Espais de Dades** per cada grup per controlar la paginació de dades:

![Data Slots Groups](img/v4_layouts_data_slots_groups.png)

Fes edicions a l'**Aparença** de cada Element en un grup:

- Fes clic a la icona de llapis a la cantonada superior dreta.

- Fes clic en cada Element i usa la pestanya Aparença per fer canvis.
- Fes clic fora del grup o fes clic a la X per sortir de l'edició.

{tip}

Es poden fer edicions a la **Configuració** però s'aplicarà a tots els Elements afegits.

¡Desagrupa elements des del menú de clic dret!
{/tip}

## Noves Configuracions

Es poden crear Noves Configuracions per tenir opcions de configuració alternatives/diferent font de dades associada amb el Widget:

- Fes clic dret en un Element o Grup d'Elements i selecciona **Nova Configuració** des del menú.
- Selecciona una font de dades alternativa / configuració alternativa des de la pestanya **Configurar**.

## Plantilles (Stencils)

Els Widgets de Dades seleccionats inclouen dissenys prefabricats de Grups d'Elements anomenats **Plantillas** per ajudar els Usuaris a crear contingut de manera simple i ràpida:

- Les Plantilles s'afegeixen exactament de la mateixa manera, posicionades i redimensionades.
- Completa els camps per **Configurar**.
- Edita l'**Aparença** fent clic a la icona de llapis a la part superior dreta del grup.
- Selecciona un Element en el grup per fer edicions.

{tip}
¡Fes clic dret per desagrupar i personalitzar encara més!
{/tip}

## Plantilles Estàtiques

Les Plantilles Estàtiques s'inclouen per Widgets específics. Les Plantilles poden configurar-se per afectar el comportament dels resultats retornats, així com alterar les opcions d'estil.

{version}
Per a ús avançat, ¡es poden crear **Plantilles de Mòdul** per usar amb Widgets de Dades usant HTML/CSS i JavaScript des de la secció **Desenvolupador** del menú principal del CMS!
{/version}

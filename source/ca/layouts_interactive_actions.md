---
toc: "layouts"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Afegeix Accions Interactives als Dissenys per activar canvis de contingut a les Pantalles"
keywords: "webhook, touch, botó, enllaç, zona interactiva, widgets interactius, codi d'activació, codi de disseny, identificador de codi"
---

# Accions Interactives

Crea **Accions** Interactives en **Dissenys** per activar canvis de contingut per mostrar a les teves **Pantalles**.

Pots tenir una exhibició de producte que inclogui un dispositiu 'internet de les coses', com un sensor de llum, que podria usar-se per activar un webhook per mostrar un Disseny amb informació específica del producte en una Pantalla per al producte amb el qual ha interactuat un client.

Podries utilitzar pantalles tàctils per mostrar informació específica activada al pressionar un botó en un Disseny, mostrat a la Pantalla.

Les Accions poden adjuntar-se a un **Disseny** complet, **Widgets** individuals en un Disseny o en una **Imatge dins d'una Llista de Reproducció** en un Disseny, activades per **Toc/Clic** o programàticament per un **Webhook**.

Dissenya el teu Disseny, afegint **Widgets** per configurar com **Activadors** i **Objectius** interactius.

Més **Widgets Interactius** estan disponibles des de la **Caixa d'Eines**:

- **Botó** es pot usar com un Activador que es pot personalitzar completament per adaptar-se als teus dissenys.
- **Enllaç** es pot afegir per proporcionar text per ser usat com un Activador.
- **Zona Interactiva** per definir una àrea en el Disseny per ser usada com Objectiu o Activador.

Per usar una **Imatge** com activador, primer afegeix una **Llista de Reproducció** des de la **Caixa d'Eines** i afegeix una Imatge a la Línia de Temps de la Llista de Reproducció.

Un cop dissenyat, canvia el **Mode Interactiu a ON**, ubicat a la part superior de l'Editor de Dissenys.

Els elements de disseny es bloquejaran per centrar-se en afegir i editar **Accions** només.

Les Accions es creen fent clic en un element en el Disseny com un Activador per arrossegar una fletxa a un element Objectiu, fent clic en **Guardar** des del Panell de Propietats.

També es poden crear fent clic en **Afegir Acció** des del **Panell de Propietats**, i seleccionant el Tipus d'Acció i Tipus d'Activador.

- Seleccionar **Toc/Clic**, requereix que els dispositius que s'usaran com pantalla tàctil tinguin capacitats tàctils habilitades.

- Per utilitzar un **Webhook** es necessita ingressar un **Codi d'Activador** que ha d'estar present en el paràmetre URL `trigger=`.

Selecciona quin element en el Disseny ha de ser l'**Activador**.

- Fes clic a **Guardar**.

Es mostraran fletxes per veure fàcilment la relació entre Activadors i Objectius.

### Tipus d'Acció

- **Disseny Següent/Anterior** mostrarà el Disseny següent o anterior en la programació per la(es) Pantalla(es) seleccionada(es).
- **Navegar a Disseny** usa un **Codi** per identificar el Disseny al qual canviar. Usa el botó **Cercar Dissenys** a la part inferior del llenç, per cercar Dissenys per Codi. Assegura't que els Dissenys que s'usaran com Objectius Interactius tinguin un **Identificador de Codi** assignat en el **formulari Editar Disseny**.
- **Widget Següent/Anterior** s'usa amb contingut des de dins d'una **Llista de Reproducció** i mostrarà l'element següent/anterior en aquesta Línia de Temps de la Llista de Reproducció.
- **Navegar a Widget** per especificar quin Widget carregar o fes clic en **Crear Widget** perquè es pugui seleccionar un element de la Caixa d'Eines per afegir a l'Objectiu especificat.

## Lectures Addicionals

{nonwhite}
[Control del Reproductor amb Webhooks](/docs/developer/player-control/webhooks)
{/nonwhite}

[Usant l'Editor de Dissenys](layouts_editor)

[Usant Llistes de Reproducció en Dissenys](layouts_editor_playlists)

## Preguntes Freqüents

***On habilito les capacitats tàctils per al meu dispositiu Android?***

Des de Configuració de Pantalla sota la secció Pantalles del menú principal del CMS i usa el menú de fila per seleccionar Editar. Des de la pestanya Avançat, marca la configuració Habilitar capacitats tàctils en el dispositiu a la part inferior del formulari.

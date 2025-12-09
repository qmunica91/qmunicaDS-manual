---
toc: "layouts"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Accelera el procés de disseny usant Plantilles"
keywords: "zones, marcadors de posició, alterar plantilla, xibo exchange"
persona: "content creator, super administrator, user"
---

# Plantilles

Usa Plantilles per accelerar el procés de disseny i assegurar que es mantingui un estàndard corporatiu.

## Resum de Característiques:

- Usa dissenys de Disseny publicats existents per guardar-los fàcilment com Plantilles.
- Crea i gestiona Plantilles des d'una pàgina dedicada per a una gestió més fàcil.
- Afegeix Zones a les Plantilles perquè actuïn com marcadors de posició de contingut en un Disseny.
- Estableix opcions de Compartir per restringir l'accés de l'Usuari a zones seleccionades en una Plantilla.
- Mostra Plantilles Publicades per selecció en l'Editor de Dissenys.
- Accelera tot el procés de disseny de Dissenys per a tots els Usuaris.
- Aplica una aparença estandarditzada a tots els Dissenys.

Crea noves Plantilles o guarda els teus dissenys de Disseny existents per usar-los com Plantilles per a futurs Dissenys.

{nonwhite}
Selecciona una de les nostres plantilles dissenyades des del [Xibo Exchange.](layouts_editor_using_templates.html#content-xibo-exchange) fent clic al botó sota Plantilles des de la Caixa d'Eines.
{/nonwhite}

{version}
Seleccionar una Plantilla reemplaçarà el disseny de Disseny actual amb la Plantilla escollida. Aquesta acció és irreversible i ha d'usar-se amb precaució.
{/version}

## Crear Plantilla

Les Plantilles es creen seleccionant **Plantilles** sota la secció **Disseny** del menú principal del CMS.

- Selecciona el botó **Afegir Plantilla** i completa els camps del formulari.

![Add Template Form](img/v4_layouts_add_template_form.png)

- Dóna a la teva Plantilla un **Nom** per facilitar la seva identificació en el CMS.

- Selecciona la Resolució.

Al **Guardar**, l'[Editor de Dissenys](layouts_editor.html) s'obrirà automàticament amb una **Zona** de mida completa.

Les Zones s'usen per definir àrees en un Disseny a les quals es pot afegir contingut.

{tip}
Si no vols incloure cap Zona i afegir contingut directament a la Plantilla, elimina la Zona del llenç fent clic dret i seleccionant **Eliminar**. Afegeix contingut de la mateixa manera que creant un Disseny.
{/tip}

### Afegir Zones

{tip}
¡Les Zones només estan disponibles per al seu ús amb Plantilles!
{/tip}

- Fes clic en qualsevol lloc de la zona per redimensionar i posicionar:

![Template Layout Editor](img/v4_layouts_templates_editor.png)

{tip}
Usa els botons a la part inferior dreta per seleccionar **Ajustar a la Quadrícula**, **Ajustar als Bordes** o **Ajustar a Elements** per facilitar el posicionament al agregar elements.
{/tip}

Les **Zones** es poden afegir des de la barra d'eines:

- Fes clic al botó superior **Widget**.

![Add Zone](img/v4_layouts_templates_add_zone.png)

- Selecciona la Zona i arrossega i deixa anar o fes clic per afegir.
- Redimensiona i Posiciona.

{tip}
Estableix en **Bucle** només si la Zona conté un Widget que necessita actualitzar-se periòdicament (per exemple, RSS Ticker) i necessita actualitzar-se amb més freqüència que la durada del Disseny general.
{/tip}

### Capes

Des del Panell de Propietats, selecciona la pestanya Posicionament per establir Capes per Zones superposades / contingut afegit.

Afegeix tant contingut des de la Caixa d'Eines com Zones per construir el teu disseny de Plantilla.

Un cop que la teva Plantilla estigui completa, usa el menú a la part superior de l'editor per **Publicar**:

![Publish Template](img/v4_layouts_templates_publish.png)

Les **Plantilles** Publicades es mostraran per selecció des de la Caixa d'Eines de l'Editor de Dissenys.

## Guardar Disseny com Plantilla

Els Dissenys Publicats es poden guardar com una **Plantilla** des de dues ubicacions:

- Des de l'[Editor de Dissenys](layouts_editor.html):
  - Després de **Publicar** torna al menú i selecciona **Guardar Plantilla**:

![Save Template Editor](img/v4_layouts_templates_save_as_template.png)

- Des de la quadrícula de Dissenys:
  - Usa el menú de fila per a un Disseny **Publicat** i **selecciona Guardar Plantilla**.

Completa tots els camps rellevants del formulari per guardar el Disseny seleccionat com una Plantilla.

{tip}
¡Opcionalment usa la casella de verificació per incloure també tots els **Widgets** afegits a la Plantilla!
{/tip}

- **Guardar**

{tip}
Els Dissenys que es guarden com una Plantilla es poden veure i editar des de la quadrícula de **Plantilles** sota la secció **Disseny** del menú principal del CMS.

¡**Etiquetar** un Disseny com una 'Plantilla' també afegirà els teus dissenys a la teva llista de Plantilles!
{/tip}

## Menú de Fila

Totes les Plantilles tenen un menú de fila on els Usuaris poden accedir a una llista d'accions/dreceres.

- Els ajustos notables s'enumeren a continuació:

#### Alterar Plantilla

Selecciona per fer canvis de disseny a la Plantilla en l'Editor de Dissenys.

#### Checkout

Per realitzar edicions en una Plantilla Publicada fes clic en **Checkout** i crea un esborrany. Un cop editada la Plantilla es pot publicar per fer permanents els canvis sobreescrivint la Plantilla existent. Descartar revertirà la Plantilla al seu estat original publicat.

{tip}
Pren-te el teu temps amb qualsevol edició que necessitis fer, ja que usar **Checkout** assegura que no es realitzin canvis en la teva versió publicada ni es mostrin en **Pantalles** programades fins que triïs fer-ho. **Publicar** confirma que s'han realitzat canvis i sobreescriurà la teva versió publicada. **Descartar** eliminarà l'esborrany romanent la versió publicada intacta.
{/tip}

#### Publicar

Publicar assegurarà que la Plantilla es mostri per selecció des de la Caixa d'Eines.

#### Descartar

Descartar tots els canvis realitzats en un esborrany i revertir a la versió Publicada anterior.

#### Compartir

Estableix opcions de Compartir per a l'accés d'Usuari/Grup d'Usuaris a Plantilles individuals.

#### Exportar

Exporta la Plantilla incloent tots els Widgets/Multimèdia/Conjunts de Dades associats a un fitxer ZIP, perquè pugui compartir-se fàcilment.

{tip}
Al exportar una Plantilla, s'exportaran totes les **Etiquetes de Disseny**, **Llista de Reproducció** i **Etiquetes Multimèdia** assignades. Selecciona l'opció **Importar Etiquetes** per afegir aquestes Etiquetes en la Importació de Disseny.

¡Usa l'opció **Amb Seleccionats** a la part inferior de la quadrícula de Plantilles per realitzar accions massives per múltiples Plantilles!
{/tip}

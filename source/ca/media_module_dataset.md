---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
aliases:
  - "media_module_dataset_ticker"
  - "media_module_dataset_view"
excerpt: "Mostra informació continguda en Conjunts de Dades com Tickers o Taules"
keywords: "ticker de conjunt de dades, vista de conjunt de dades, taules de conjunt de dades, elements de conjunt de dades, plantilles de conjunt de dades"
---

# Conjunt de Dades (DataSet)

Mostra dades contingudes en un Conjunt de Dades en qualsevol lloc d'un Disseny usant **Elements** o inclou **Plantilles Estàtiques** per mostrar Tickers i Taules de dades en Dissenys/Llistes de Reproducció.

{feat}DataSets|v4{/feat}

El Widget de Conjunt de Dades consisteix principalment en una font de Conjunt de Dades que alimenta els Elements configurats i les Plantillas Estàtiques.

{tip}
Els [Conjunts de Dades](media_datasets.html) han de crear-se i definir-se abans d'afegir el Widget de Conjunt de Dades a Dissenys/Llistes de Reproducció.
{/tip}

## Elements de Conjunt de Dades

Els [Elements](layouts_editor#content-data-widgets-and-elements) estan disponibles per selecció al afegir un Widget de Conjunt de Dades a un [Disseny](layouts_editor.html) per donar als Usuaris més control sobre quins components del Widget de Conjunt de Dades usar i on es poden col·locar.

![DataSet Elements](img/v4_media_module_dataset_elements.png)

{tip}
¡Veuràs un missatge al panell de propietats si intentes usar un Element que no té un tipus de camp coincident en el teu Conjunt de Dades!
{/tip}

Cada Element té un conjunt d'opcions de configuració en el Panell de Propietats. S'ha de seleccionar un Conjunt de Dades per usar com a font de dades des de la pestanya **Configurar** per a cada Element usat en el Disseny. Controla com els articles han de ciclar-se especificant una [Ranura de Dades](layouts_editor.html#content-data-slots) per usar per a cadascun dels Elements afegits. Els Elements de Dades poden complementar-se encara més afegint Elements Globals per afegir formes i text que es poden posar en un Grup d'Elements per a una configuració i posicionament més fàcils.

## Plantilles Estàtiques de Conjunt de Dades

Les Plantilles Estàtiques defineixen com han d'organitzar-se i estilitzar-se les dades retornades i són una manera simple de mostrar les teves dades usant plantilles preestilitzades.

![DataSet Templates](img/v4_media_module_dataset_templates.png)

Les Plantilles es poden configurar per afectar el comportament dels resultats retornats, així com fer canvis en l'aparença del disseny usant una gamma d'opcions en el Panell de Propietats. S'ha de seleccionar un Conjunt de Dades per usar com a font de dades des de la pestanya **Configurar** per a cada Plantilla afegida al Disseny/Llista de Reproducció.

## Descripció General

- Actualitza Elements i Plantilles amb noves dades editant les dades subjacents del [Conjunt de Dades](media_datasets.html#content-adding-data-to-columns).
- Actualitza el contingut del Widget de Conjunt de Dades sense accedir a Dissenys o Llistes de Reproducció.
- Ordena i Filtra resultats per qualsevol columna.
- Barreja elements per reproduir en una seqüència aleatòria.
- El contingut per a aquest mitjà és emmagatzemat en memòria cau pels Reproductors per reproducció fora de línia.
- Estableix una 'comprovació de frescor' per determinar quan canviar al missatge 'Sense dades' quan un Reproductor està fora de línia.

---
toc: "widgets"
maxHeadingLevel: 2
excerpt: "Usa el Widget Ticker RSS per mostrar contingut de feed dinàmic"
keywords: "feeds dinàmics"
---

# Ticker RSS

Mostra contingut de feed dinàmic en qualsevol lloc d'un Disseny usant Elements o inclou Plantilles Estàtiques amb dissenys preestilitzats en Dissenys/Llistes de Reproducció.

{feat}Ticker|v4{/feat}

El Widget Ticker consisteix principalment en una ubicació de font de dades que alimenta els Elements configurats i les Plantillas Estàtiques.

## Elements de Ticker

Els Elements estan disponibles per selecció al afegir un Widget Ticker RSS a un [Disseny](layouts_editor.html) per donar als Usuaris més control sobre quins components del Widget Ticker usar i on es poden col·locar.

![Ticker Elements](img/v4_media_module_ticker_elements.png)

Cada Element té un conjunt d'opcions de configuració en el Panell de Propietats. S'ha de proporcionar una URL per ser usada com la font de dades des de la pestanya **Configurar** per a cada Element usat en el Disseny. Controla com els articles han de ciclar-se especificant una Ranura de Dades per usar per a cadascun dels Elements afegits. Els Elements de Dades poden complementar-se encara més afegint Elements Globals per afegir formes i text que es poden posar en un Grup d'Elements per a una configuració i posicionament més fàcils.

## Plantilles Estàtiques de DataSet

Les Plantilles Estàtiques defineixen com han d'organitzar-se i estilitzar-se els elements retornats i són una manera simple de mostrar elements usant plantilles preestilitzades.

![Ticker Templates](img/v4_media_module_ticker_templates.png)

Les Plantilles es poden configurar per afectar el comportament dels resultats retornats, així com fer canvis en l'aparença del disseny usant una gamma d'opcions en el Panell de Propietats. S'ha de proporcionar una URL per ser usada com la font de dades des de la pestanya **Configurar** per a cada Plantilla afegida al Disseny/Llista de Reproducció.

## Descripció General

- Defineix quants elements han de mostrar-se d'un feed.
- La durada es pot establir per element.

{tip}
Usa aquesta opció amb precaució ja que això pot crear elements de mitjans de llarga durada. ¡Assegura't d'usar en conjunt amb **Nombre d'elements** per limitar!
{/tip}

- Selecciona començar amb elements des de l'Inici o Fi de la llista.

- Es pot seleccionar ordre Invers i Aleatori dels elements del feed.

- Inclou un avís de Copyright per mostrar al final del feed.

- Retorna resultats costat a costat.

- Proporciona una llista d'atributs que no han d'eliminar-se del feed entrant.

- Inclou una llista d'etiquetes HTML per ser eliminades del feed.

- Estableix un Agent d'Usuari específic.

- Descodifica entitats HTML en el feed abans d'analitzar-lo.

- Deshabilita l'ordre per data.

- Emmagatzemat en memòria cau per reproducció fora de línia.

- Anul·la l'Interval d'Actualització per Imatges.

{tip}
¡Crea el teu propi [Feed RSS](media_datasets.html#content-view-rss) per usar amb aquest Widget usant [Conjunts de Dades](media_datasets.html)!
{/tip}

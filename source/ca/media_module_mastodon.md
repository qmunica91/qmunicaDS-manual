---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
aliases:
  - "media_module_twitter"
  - "media_module_twitter_metro"
  - "media_module_mastadon"
excerpt: "Mostra contingut de feed social de Mastodon en Pantalles"
keywords: "contingut social, publicacions socials, feeds socials, hashtags, menciones"
---

# Mastodon

Mostra contingut de feed social de Mastodon en qualsevol lloc d'un Disseny usant Elements o inclou Plantilles Estàtiques amb dissenys preestilitzats en Dissenys/Llistes de Reproducció.

{feat}Mastodon|v4{/feat}

El Widget de Mastodon retorna contingut de la URL ingressada per al [Mòdul](media_modules.html) que alimenta els Elements configurats i les Plantillas Estàtiques.

## Elements de Mastodon

Els Elements estan disponibles per selecció al afegir un Widget de Mastodon a un [Disseny](layouts_editor.html) per donar als Usuaris més control sobre quins components del Widget de Mastodon usar i on es poden col·locar.

![Mastodon Elements](img/v4_media_modules_mastadon_elements.png)

Cada Element té un conjunt d'opcions de configuració en el Panell de Propietats. S'ha de proporcionar un **Hashtag** per retornar resultats des de la pestanya **Configurar** per a cada Element usat en el Disseny. Controla com els articles han de ciclar-se especificant una [Ranura de Dades](layouts_editor.html#content-data-slots) per usar per a cadascun dels Elements afegits. Els Elements de Dades poden complementar-se encara més afegint Elements Globals per afegir formes i text que es poden posar en un Grup d'Elements per a una configuració i posicionament més fàcils.

Aprofita les Plantilles (Stencils) per afegir un grup predissenyat d'Elements al teu Disseny.

{tip}
¡Tots els Elements en la Plantilla es tracten com 'un' quan es configuren i es poden duplicar fàcilment amb un clic dret!
{/tip}

## Plantilles Estàtiques de Mastodon

Les Plantilles Estàtiques defineixen com han d'organitzar-se i estilitzar-se els elements retornats i són una manera simple de mostrar elements usant plantilles preestilitzades.

![Mastadon Templates](img/v4_media_modules_mastadon_templates.png)

Les Plantilles es poden configurar per afectar el comportament dels resultats retornats, així com fer canvis en l'aparença del disseny usant una gamma d'opcions en el Panell de Propietats. S'ha de proporcionar un **Hashtag** per retornar resultats des de la pestanya **Configurar** per a cada Plantilla afegida al Disseny/Llista de Reproducció.

## Descripció General

- Mostra publicacions només amb mitjans adjunts.
- Elimina Mencions, Hashtags i URLs de les publicacions.
- Mostra publicacions només de servidors locals o remots.
- Inclou un Nom d'Usuari de Mastodon per retornar estats públics.
- Estableix la durada per element.

{tip}
La majoria d'URLs no complementen la Senyalització Digital.
{/tip}

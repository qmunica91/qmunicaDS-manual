---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Mostra tipus de canvi per a parells de divises"
keywords: "api alpha vantage, connector alpha vantage, conversió inversa, moneda base"
---

# Monedes

Mostra tipus de canvi per a parells de divises en qualsevol lloc d'un Disseny usant **Elements** o selecciona una **Plantilla Estàtica** per mostrar resultats en Dissenys/Llistes de Reproducció.

{feat}Currencies|v4{/feat}

El Widget de Monedes depèn en part de l'[API d'Alpha Vantage](https://www.alphavantage.co/) per recuperar dades de tipus de canvi que alimenten els Elements configurats i les Plantillas Estàtiques.

{tip}
Si us plau visita [Alpha Vantage](https://www.alphavantage.co/support/#api-key) per crear una compte i obtenir una clau API per ingressar en el [Connector d'Alpha Vantage.](media_modules.html#content-connectors)
{/tip}

{nonwhite}
{cloud}
El Mòdul de Monedes està configurat per clients allotjats en **Xibo Cloud** amb una clau API proporcionada com part del servei.
{/cloud}
{/nonwhite}

## Elements de Monedes

Els Elements estan disponibles per selecció al afegir el Widget de Monedes a un [Disseny](layouts_editor.html) per donar als Usuaris més control sobre quins components del Widget de Monedes usar i on es poden col·locar.

![Currencies Elements](img/v4_media_modules_currencies_elements.png)

Cada Element té un conjunt d'opcions de configuració en el Panell de Propietats. Ingressa **Monedas** usant les seves sigles/abreviatures que desitges mostrar així com una moneda **Base** des de la pestanya **Configurar**.

Controla com els articles han de ciclar-se especificant una [Ranura de Dades](layouts_editor.html#content-data-slots) per usar per a cadascun dels Elements afegits. Els Elements de Dades poden complementar-se encara més afegint Elements Globals per afegir formes i text que es poden posar en un Grup d'Elements per a una configuració i posicionament més fàcils.

## Plantilles Estàtiques de Monedes

Les Plantilles Estàtiques defineixen com han d'organitzar-se i estilitzar-se les dades retornades i són una manera simple de mostrar les teves dades usant plantilles preestilitzades.

![Currencies Templates](img/v4_media_modules_currencies_templates.png)

Les Plantilles es poden configurar per fer canvis en l'aparença del disseny usant una gamma d'opcions en el Panell de Propietats. Ingressa **Monedas** usant les seves sigles/abreviatures que desitges mostrar així com una moneda **Base** des de la pestanya **Configurar** per a cada Plantilla afegida al Disseny/Llista de Reproducció.

## Descripció General

- Conversió inversa per usar la moneda base com comparació.
- El contingut per a aquest mitjà és emmagatzemat en memòria cau pels Reproductors per reproducció fora de línia.
- La durada es pot aplicar per element o per pàgina.

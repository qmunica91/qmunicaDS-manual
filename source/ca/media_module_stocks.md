---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Mostra informació de preus de comerç per a llistats d'accions"
keywords: "api alpha vantage, connector alpha vantage"
---

# Accions (Stocks)

Mostra informació de preus de comerç per a llistats d'accions en qualsevol lloc d'un Disseny usant **Elements** o selecciona una **Plantilla Estàtica** per mostrar resultats en Dissenys/Llistes de Reproducció.

{feat}Stocks|v4{/feat}

El Widget d'Accions depèn en part de l'[API d'Alpha Vantage](https://www.alphavantage.co/) per recuperar dades del mercat de valors que alimenten els Elements configurats i les Plantillas Estàtiques. Els preus retornats per Alpha Vantage segueixen l'[estàndard del mercat de valors](https://medium.com/@patrick.collins_58673/stock-api-landscape-5c6e054ee631) d'ajust per esdeveniments corporatius com divisions i pagament de dividends.

{tip}
Si us plau visita [Alpha Vantage](https://www.alphavantage.co/support/#api-key) per crear una compte i obtenir una clau API per ingressar en el [Connector d'Alpha Vantage.](media_modules.html#content-connectors)
{/tip}

{nonwhite}
{cloud}
El Mòdul de Monedes està configurat per clients allotjats en **Xibo Cloud** amb una clau API proporcionada com part del servei.
{/cloud}
{/nonwhite}

## Elements d'Accions

Els Elements estan disponibles per selecció al afegir el Widget d'Accions a un [Disseny](layouts_editor.html) per donar als Usuaris més control sobre quins components del Widget d'Accions usar i on es poden col·locar.

![Stocks Elements](img/v4_media_module_stocks_elements.png)

Cada Element té un conjunt d'opcions de configuració en el Panell de Propietats. Ingressa **Símbols d'Accions** per retornar resultats des de la pestanya **Configurar**.

{tip}
Si necessites un símbol d'acció que només es cotitza en un intercanvi específic, llavors pots usar el format `SÍMBOL:INTERCANVI` per retornar resultats.
¡Els símbols d'accions es poden trobar en diversos llocs de cerca com [Yahoo Finance](https://finance.yahoo.com/)!
{/tip}

Controla com els articles han de ciclar-se especificant una Ranura de Dades per usar per a cadascun dels Elements afegits. Els Elements de Dades poden complementar-se encara més afegint Elements Globals per afegir formes i text que es poden posar en un Grup d'Elements per a una configuració i posicionament més fàcils.

## Plantilles Estàtiques d'Accions

Les Plantilles Estàtiques defineixen com han d'organitzar-se i estilitzar-se els resultats retornats i són una manera simple de mostrar les teves dades usant plantilles preestilitzades.

![Stocks Templates](img/v4_media_modules_stocks_templates.png)

Les Plantilles es poden configurar per fer canvis en l'aparença del disseny usant una gamma d'opcions en el Panell de Propietats. Ingressa **Símbols d'Accions** per retornar resultats des de la pestanya **Configurar** per a cada Plantilla afegida al Disseny/Llista de Reproducció.

## Descripció General

- El contingut per a aquest mitjà és emmagatzemat en memòria cau pels Reproductors per reproducció fora de línia.
- La durada es pot aplicar per element o per pàgina.

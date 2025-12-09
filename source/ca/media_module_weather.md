---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Mostra pronòstics del temps diaris en Dissenys i Llistes de Reproducció"
keywords: "open weather map"
---

# Temps

Mostra dades de pronòstic del temps diaris en qualsevol lloc d'un Disseny usant **Elements** o selecciona una **Plantilla Estàtica** per mostrar resultats en Dissenys/Llistes de Reproducció.

{feat}Weather|v4{/feat}

Les dades del temps són proporcionades per [OpenWeather](https://openweathermap.org/) que es proporciona sota [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) i [ODbL](https://opendatacommons.org/licenses/odbl/) el que proporciona pronòstics del temps diaris mundials actuals que alimenten els Elements configurats i les Plantilles Estàtiques.

{tip}

Si us plau assegura't d'estar usant un CMS v3.2.1 o posterior per tenir en compte els canvis d'API.

Visita [Open Weather Map](https://openweathermap.org/api) per crear una compte i obtenir una clau API per ingressar en el [Connector d'Open Weather.](media_modules.html#content-connectors)

**NOTA:** Des del llançament de One Call 3.0 d'Open Weather, els nous usuaris han d'ingressar detalls de targeta de crèdit per usar la clau gratuïta de x nombre de trucades o optar per una subscripció de pagament.

Open Weather Map permet 1000 sol·licituds de pronòstic, per dia abans de cobrar una petita tarifa per cada sol·licitud posterior.

**Plans de pagament** desbloquegen un pronòstic de 16 dies així com altres optimitzacions en la forma en què s'extreuen les dades.

{/tip}

{noncloud}
{version}
Els usuaris existents que actualment usen l'API One Call 2.5 han de transferir-se a l'API One Call 3.0 per continuar usant aquest servei. L'accés a One Call 2.5 ja no serà possible després de juny de 2024. Es poden trobar més detalls sobre com transferir [aquí.](https://openweathermap.org/one-call-transfer)

Després de transferir-se a una nova clau, assegura't de netejar la memòria cau per Clima usant el menú de fila des de la pàgina **Mòduls**.
{/version}
{/noncloud}

{nonwhite}
{cloud}
El Mòdul de Clima està configurat per clients allotjats en **Xibo Cloud** amb una clau API proporcionada com part del servei.
{/cloud}
{/nonwhite}

Els Termes de Servei d'Open Weather Map https://openweathermap.org/terms han de llegir-se i entendre's abans d'usar aquest Widget.

## Elements de Clima

Els Elements estan disponibles per selecció al afegir el Widget de Clima a un [Disseny](layouts_editor.html) per donar als Usuaris més control sobre quins components del Widget de Clima usar i on es poden col·locar.

![Weather Elements](img/v4_media_module_weather_elements.png)

Cada Element té un conjunt d'opcions de configuració en el Panell de Propietats. Ingressa la ubicació geogràfica i unitats per retornar resultats des de la pestanya **Configurar**.

Controla com els articles han de ciclar-se especificant una Ranura de Dades per usar per a cadascun dels Elements afegits. Els Elements de Dades poden complementar-se encara més afegint Elements Globals per afegir formes i text que es poden posar en un Grup d'Elements per a una configuració i posicionament més fàcils.

{tip}
Tots els Dissenys que usen el Widget de Clima necessiten incloure atribució, disponible usant l'Element d'Atribució. Les Plantilles Estàtiques contenen aquesta etiqueta per defecte.
{/tip}

## Plantilles Estàtiques de Clima

Les Plantilles Estàtiques defineixen com han d'organitzar-se i estilitzar-se els resultats retornats i són una manera simple de mostrar les teves dades usant plantilles preestilitzades.

![Weather Templates](img/v4_media_modules_weather_templates.png)

Les Plantilles es poden configurar per fer canvis en l'aparença del disseny usant una gamma d'opcions en el Panell de Propietats. Ingressa ubicacions geogràfiques i unitats per retornar resultats des de la pestanya **Configurar** per a cada Plantilla afegida al Disseny/Llista de Reproducció.

## Descripció General

- Retorna resultats basats en la Ubicació de Pantalla.
- Estableix automàticament la unitat de mesura a usar per basar-se en la ubicació geogràfica.
- Selecciona automàticament pronòstics del temps basats en la Ubicació de Pantalla.
- Especifica quin Idioma usar.
- Opta per mostrar només condicions climàtiques diürnes.
- Reemplaça Imatges de Fons amb imatges de la [Biblioteca](media_library.html)
- Les dades per a aquest mitjà són emmagatzemades en memòria cau pels Reproductors per reproducció fora de línia.

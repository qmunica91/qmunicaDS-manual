---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Mostra alertes meteorològiques en temps real"
keywords: "alertes meteorològiques d'emergència, format de feed atom, url de feed atom personalitzada, connector nws"
---

# Servei Nacional de Meteorologia

Ajuda als ciutadans dels EUA a preparar-se per esdeveniments climàtics extrems mostrant pronòstics del temps amb dades en temps real sobre clima sever, aigua i esdeveniments climàtics. Augmenta la consciència sobre perills potencials a través de la teva xarxa de Pantalles [[PRODUCTNAME]] usant dades del [Servei Nacional de Meteorologia (NWS)](https://www.weather.gov/).

![National_Weather_Alerts](img/media_module_national_weather_alerts_elements.png)

{version}
**NOTA:** Els pronòstics i advertències meteorològiques són per als Estats Units, els seus territoris i aigües adjacents i àrees oceàniques. Si desitges utilitzar aquest Widget, demana al teu Administrador que habiliti el **Servei Nacional de Meteorologia** des de la secció **Mòduls**.
{/version}

## Descripció General de Característiques

- El **Connector del Servei Nacional de Meteorologia** utilitza dades de la URL de feed Atom de NWS proporcionada.
- Es pot usar amb la **URL predeterminada per al Feed Atom de NWS** o es pot proporcionar una URL de format de Feed Atom personalitzada.
- Afegeix d'una varietat d'**Elements** per adaptar representacions visuals en l'Editor de Dissenys per al màxim impacte.
- Usa filtres estàndard de la indústria per adaptar la missatgeria de les dades retornades.
- Mostra múltiples missatges d'alerta meteorològica amb ciclatge de dades del Feed Atom de NWS.
- Estableix **Criteris** al **Programar** per determinar si l'alerta meteorològica ha d'incloure's en el Bucle de Programació per Reproductors suportats.

{tip}
{nonwhite}
¡A l'establir el **Tipus de Criteri** en "Alerta d'Emergència" i la **Categoria** en "Met", t'asseguraràs que els Dissenys amb Elements NWS s'afegeixin automàticament al Bucle de Programació cada vegada que passi una **Alerta d'Emergència** activa!
{/nonwhite}
{/tip}

## Suport de Característiques del Reproductor

{feat}National Weather Service|v4{/feat}

## Lectura Addicional

[Gestió de Connectors](/media_modules_connectors)

[Widgets de Dades](/layouts_editor_data_widgets)

[Editor de Dissenys](/layouts_editor)

{nonwhite}
[Criteris de Programació](/developer/player-control/schedule-criteria)
{/nonwhite}

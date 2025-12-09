---
toc: "widgets"
minHeadingLevel: 2
excerpt: "Mostra Panells que han estat configurats per usar el Servei de Panells de Xibo"
keywords: "servei de panells de xibo, power bi, grafana, matomo"
---

# Panells (Dashboards)

{white}
**Tingues en compte:** Si desitges aprofitar aquest Widget, per favor contacta al teu Administrador.
{/white}

{nonwhite}
El Widget de Panells s'utilitza per mostrar [Panells](media_dashboard_service.html) que s'han configurat per usar el [Servei de Panells de Xibo](/docs/setup/xibo-dashboard-service)

**Tingues en compte:** Aquest Widget comercial és part del **Servei de Panells de Xibo** i requereix una API per configuració com s'explica més endavant [aquí](/pricing#dashboards)

{feat}Dashboards|v4{/feat}

## Configuració

- Selecciona el servei de panell perquè coincideixi amb els panells que s'han configurat en el connector.
- Ingressa la URL per incrustar.

{tip}
Si us plau mira la següent pàgina per més informació sobre com obtenir una URL per usar amb aquest servei, mecanismes d'autenticació i possibles limitacions [Servei de Panells de Xibo](/docs/setup/xibo-dashboard-service)
{/tip}

- Proporciona un interval d'actualització en minuts.

{version}
**NOTA:** L'interval d'actualització mínim que es pot ingressar per panell és de 5 minuts ja que no admetem actualitzacions del servei de panell amb més freqüència que 5 minuts.
{/version}

A l'ingressar per primera vegada una URL en el Widget de Panell, pot trigar uns moments en carregar-se ja que depèn de quant temps trigui en renderitzar-se el contingut del teu panell, i que tan ocupat estigui el servei actualment.

Un cop que estiguis mostrant els teus panells en pantalles, el servei mantindrà els teus panells actualitzats en l'interval que specifiquis perquè sempre estiguin llestos per mostrar-se i apareguin instantàniament a les Pantalles.

Si deixes de mostrar un panell a les teves pantalles per un temps, llavors el servei deixarà d'actualitzar-lo, però començarà de nou automàticament la propera vegada que es mostri aquest panell.

{tip}

Per defecte, els informes en **Power BI** es renderitzen amb un format de Data d'EUA. Per usar un format de data alternatiu, afegeix els següents paràmetres a la URL que passes en el Widget de Panells com es mostra amb l'exemple a continuació per `en-GB`:

`&language=en&formatLocale=en-GB`

{/tip}

**Tingues en compte:** Si Xibo detecta un error amb una sol·licitud de serveis de panell, veuràs un missatge de banner vermell sobre la part superior d'una captura de pantalla per donar una indicació a l'usuari d'on ha ocorregut el problema. Això es mostrarà en el previsualitzador del Dissenyador de Dissenys només per a l'usuari connectat. La Previsualització del Disseny i les Pantalles que mostren el Disseny programat continuaran mostrant l'última captura bona o una icona de carregant fins que s'hagi resolt el problema.

Missatge d'Error d'Exemple amb captura de pantalla mostrada a continuació:

![Example Error Message](img/v4_media_modules_dashboard_error.png)

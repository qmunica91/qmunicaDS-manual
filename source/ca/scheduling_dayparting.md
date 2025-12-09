---
toc: "scheduling"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Crea les teves pròpies Particions del Dia per simplificar la programació"
keywords: "excepcions, hores d'operació de pantalla, predefinit"
---

# Partició del Dia (Dayparting)

{tip}
En la programació de transmissió, dayparting és la pràctica de dividir el dia de transmissió en diverses parts, en les quals es transmet un tipus diferent de programa de ràdio o televisió apropiat per a aquest període de temps.
-- Wikipedia
{/tip}

[[PRODUCTNAME]] admet la creació de múltiples Particions del Dia, que poden incloure excepcions per dia de la setmana. Això significa que un sol dia es pot dividir en tantes parts **predefinides** com sigui necessari.

{tip}
Un cas d'ús típic seria un Usuari d'hostaleria que té contingut diferent per mostrar per a l'Esmorzar, el Dinar i el Sopar. La Partició del Dia permet a aquest Usuari crear una partició del dia per Esmorzar, Dinar i Sopar, cadascuna de les quals comença i acaba en un dia diferent per a la seva selecció per simplificar la programació diària.
{/tip}

{version}
Les **Particions del Dia** també es poden crear per establir les [Hores d'Operació de Pantalles](displays_settings.html#content-operating-hours).
{/version}

## Afegir Partició del Dia

Les Particions del Dia es creen i administren des de **Partició del Dia** en el menú principal del CMS.

- Selecciona el botó **Afegir Partició del Dia**.
- Completa els camps del formulari per configurar.

{tip}
¡Inclou **Excepcions** per definir diferents temps d'inici i fi per dies seleccionats!
{/tip}

Al Guardar, la Partició del Dia estarà disponible per a selecció en el menú desplegable **Partició del Dia** del formulari de programació a l'afegir un Esdeveniment.

{tip}
El següent formulari de Partició del Dia mostra un exemple de Partició del Dia d'Esmorzar:

![Exanple Breakfast Daypart](img/v4_scheduling_daypart_form.png)

Dissabte i Diumenge s'han configurat com excepcions perquè l'esmorzar comenci i acabi en diferents moments en aquests dies:

![Daypart form exceptions tab](img/v4_scheduling_daypart_form_exceptions.png)

Al Programar, la Partició del Dia **Esmorzar** apareixerà en el menú desplegable per a selecció. Al seleccionar, els selectors de data/hora des de/fins a canviaran a selectors de només data i l'hora es prendrà de la configuració de Partició del Dia - d'acord amb el dia de la setmana en què té lloc l'Esdeveniment.
{/tip}

## Editar Particions del Dia

Fes edicions a les Particions del Dia existents usant el menú de fila.

{tip}
¡Afegeix opcions de Compartir per Particions del Dia per Compartir amb altres Usuaris/Grups d'Usuaris!

Actualitzar els temps d'inici/fi o excepcions per una Partició del Dia farà que els esdeveniments futurs existents s'actualitzin amb els temps recentment definits.

Les Programacions recurrents existents, configurades per recórrer més enllà del temps actual, tindran noves Programacions creades per reflectir la informació actualitzada.
{/tip}
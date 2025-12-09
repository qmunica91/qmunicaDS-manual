---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 1
alias: "media_module_chart"
excerpt: "Gestió de Mòduls per a Administradors"
keywords: "fitxer genèric, emmagatzematge en memòria cau, accés extern, habilitar mòduls, deshabilitar mòduls"
---

# Gestió de Mòduls

Tot el contingut mostrat en [[PRODUCTNAME]] és servit per un **Mòdul de Mitjans** gestionat des de la pàgina **Mòduls** sota la secció **Administració** del menú principal del CMS:

![Modules Grid](img/v4_media_modules_grid.png)

- Usa el menú de fila i fes clic a **Configurar** per controlar si ha de ser accessible perquè els Usuaris l'usin.

{tip}
De vegades pot ser necessari afegir o eliminar les extensions permeses en un Mòdul basat en fitxer de Biblioteca particular (Imatge, Vídeo, Flash, etc.). Un cas d'ús típic seria si s'està utilitzant un Reproductor que no admet aquest tipus particular de fitxer.

Les fonts es poden afegir i gestionar des de la pàgina [Fonts](tour_cms_settings.html#content-fonts) sota la secció **Administració** del menú principal del CMS.
{/tip}

## Emmagatzematge en memòria cau i accés extern

Els Mòduls principals estan dissenyats per tenir les seves dades emmagatzemades en memòria cau i servides des del CMS perquè puguin reproduir-se sense una connexió activa i/o sense accés directe a recursos externs que puguin ser necessaris. El CMS també utilitza aquest mecanisme per ser un _bon ciutadà_ en sol·licitar dades de tercers.

{tip}
Per exemple, un Widget Ticker amb l'adreça `http://anexternal.com/feed` només seria accedit pel CMS i només una vegada per `updateInterval`. Els Reproductors que mostren el Disseny no necessitarien accedir a aquesta adreça directament.
{/tip}

Tots els Mòduls principals adopten aquest enfocament, excepcions assenyalades a continuació:

- El **Mòdul de Pàgina Web** no emmagatzema en memòria cau des del CMS i sempre intentarà obrir l'adreça de pàgina web especificada usant el navegador en el Reproductor. Això significa que el Reproductor ha de tenir accés a la xarxa a l'adreça web en tot moment.
- El **Mòdul Incrustat** es pot emmagatzemar en memòria cau usant referències de biblioteca, no obstant això, l'Usuari que crea el Mòdul és lliure d'especificar recursos externs si els requereix.
- El **Mòdul de Vídeo Local** és renderitzat pel descodificador de vídeo en el Reproductor i pot fer referència a una transmissió externa.
- Els Fitxers **Flash** tenen la capacitat de fer referència a un fitxer extern i s'executaran en el Reproductor.

## Fitxer Genèric

El Mòdul de Fitxer Genèric s'utilitza per enviar **fitxers addicionals** al Reproductor que després es poden utilitzar per a altres fins.

{tip}
Això podria ser útil per proporcionar fitxers suplementaris per ser utilitzats com rutes relatives (per exemple, una fletxa cap amunt i cap avall que es mostra dinàmicament en l'HTML incrustat basat en els resultats de les dades d'accions) com exemple.
{/tip}

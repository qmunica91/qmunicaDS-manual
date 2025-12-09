---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Mostra dades amb una clau API de Google Maps"
---

# Trànsit de Google

Mostra dades de trànsit configurades amb una clau API de Google Maps en Dissenys i Llistes de Reproducció.

{version}
**IMPORTANT:** Aquest Mòdul requereix una clau API de Google que té càrrecs d'ús associats. Si us plau assegura't d'estar al corrent dels càrrecs d'ús abans d'ingressar la teva clau en la configuració d'aquest Mòdul.
{/version}

{feat}Google Traffic Maps|v4{/feat}

## Instal·lació

El Mòdul de Trànsit de Google ha de configurar-se amb una clau API de Google Maps abans d'usar. La documentació "[get a key](https://developers.google.com/maps/documentation/javascript/get-api-key)" descriu el procés i les diferències entre les claus.

El Mòdul de Trànsit de Google s'instal·la des de la pàgina **Mòduls** sota la secció **Administració** del menú principal del CMS.

- Fes clic al botó **Instal·lar Mòdul** i selecciona el Mòdul per instal·lar.
- Després de la instal·lació, selecciona el Mòdul de la quadrícula i usa el menú de fila per seleccionar **Editar**.

- Completa els camps del formulari i inclou la **clau API**.

Aquest formulari també conté configuracions per proporcionar una **durada per defecte** i una **durada mínima**. Si us plau assegura't d'entendre aquestes dues configuracions i configurar-les d'una manera adequada per al teu entorn.

{version}
**IMPORTANT:** L'API de Google es cobra per càrrega de mapa i, per tant, quant temps roman el Widget en pantalla té una relació directa amb els càrrecs que acumularàs.
{/version}

{tip}
Fins que s'ingressi una clau API, el Widget no es renderitzarà en l'Editor de Dissenys o el Reproductor, encara que encara pots afegir el Widget als teus Dissenys.

Aquest Mòdul requereix una **connexió a internet vàlida** en el Reproductor per funcionar.
{/tip}

Els termes d'ús de l'API de Google Maps han de llegir-se i entendre's abans d'usar aquest Mòdul. En el moment d'escriure això, aquests termes es poden trobar [aquí](https://developers.google.com/maps/terms).

## Descripció General

- Ingressa la Latitud i Longitud a usar.

- Usa la Ubicació de Pantalla per usar la Latitud i Longitud registrades per a una Pantalla.

- Reutilitza fàcilment 1 Disseny en múltiples Pantalles per mostrar el trànsit en la ubicació correcta per a cada Pantalla usant la configuració d'Ubicació de Pantalla.

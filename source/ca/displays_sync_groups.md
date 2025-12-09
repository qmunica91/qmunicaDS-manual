---
toc: "displays"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Els Grups de Sincronització contenen Pantalles per mostrar contingut sincronitzat"
keywords: "contingut sincronitzat, port de publicació, pantalla líder"
persona: "schedule manager, display manager, administrator"
---

# Grups de Sincronització

Els Grups de Sincronització contenen les Pantalles que mostraran contingut sincronitzat. El contingut pot sincronitzar-se per reproduir-se en 2 o més Pantalles en una configuració reflectida o de videowall al programar un [Esdeveniment Sincronitzat](scheduling_events.html#content-synchronised-events).

{feat}Sync Groups|v4{/feat}

{tip}
Sincronitza Llistes de Reproducció en diferents Dissenys usant la **Clau de Sincronització de Contingut**.
{/tip}

Les [Pantalles](displays.html) primer han d'assignar-se a un **Grup de Sincronització**:

- Fes clic en **Grups de Sincronització** sota la secció **Pantalles** del menú principal del CMS.
- Selecciona el botó **Afegir Grup de Sincronització**.

![Add Sync Group](img/v4_displays_add_sync_groups.png)

Els Grups de Sincronització poden guardar-se en Carpetas per controlar fàcilment els nivells d'interacció d'Usuari/Grup d'Usuaris per a les Pantalles, a més de proporcionar una forma addicional d'organització.

{tip}
Totes les Pantalles en un Grup de Sincronització necessiten comunicar-se usant la seva adreça IP LAN sobre TCP en el port de publicació specificat. Aquest valor predeterminat és 9590 però pot canviar-se si aquest port està reservat.

Recomanem usar una xarxa cablejada i dispositius d'alta potència similars per a la millor Sincronització.
{/tip}

- Al guardar, usa el formulari **Gestionar Membresía** per seleccionar quines Pantalles incloure en aquest Grup.

{version}
**NOTA:** Una Pantalla només pot pertànyer a un Grup de Sincronització al mateix temps.
{/version}

- Al guardar, usa el formulari Editar i utilitza el menú desplegable per seleccionar quina Pantalla ha de ser la **Pantalla Líder** per al Grup de Sincronització.

- Fes clic en **Guardar**

{tip}
El contingut ara pot programar-se al Grup de Sincronització fent clic en **Programar** des del menú principal del CMS i seleccionant el botó [Afegir Esdeveniment Sincronitzat](scheduling_events.html#content-synchronised-events).
{/tip}

## Editar / Gestionar Membresía

Gestiona un Grup de Sincronització utilitzant el menú de fila:

- Selecciona **Editar** per establir una Pantalla Líder alternativa
- Selecciona **Membres** per gestionar quines Pantalles són membres del grup.

#### Següent...

[Programant Esdeveniments Sincronitzats](scheduling_events.html#content-synchronised-events)

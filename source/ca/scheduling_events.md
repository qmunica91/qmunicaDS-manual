---
toc: "scheduling"
maxHeadingLevel: 3
minHeadingLevel: 2
aliases:
  - "layouts_interrupt"
  - "scheduling"
  - "schedule_now"
excerpt: "Crea Programacions per mostrar el teu contingut en el moment i lloc adequats"
keywords: "sincronitzat, mirall, videowall, accions programades, programació de mitjans, disseny d'interrupció"
---

# Programació 

Les Programacions es creen des de la pàgina **Programació** del menú principal del CMS i inclouen els següents Tipus d'Esdeveniments:

### Comandament

Selecciona un [Comandament](displays_command_functionality.html) per ser executat pel Reproductor en un punt específic en el temps.

{tip}
Els Esdeveniments de Comandament no requereixen un `toDt`.

L'Ordre de Visualització i la Prioritat són irrellevants quan es tracta d'executar Comandaments, però poden establir-se en el CMS per a finalitats organitzatives.
{/tip}

### Disseny de Superposició

Els Dissenys que han estat dissenyats com un [Disseny de Superposició](layouts_overlay.html) es programaran al mateix temps que els Dissenys existents per crear una superposició de contingut quan es mostrin.

### Disseny d'Interrupció

Un Disseny d'Interrupció programarà un Disseny seleccionat per reproduir-se **entre** altres Dissenys en la 'programació habitual'.

[[PRODUCTNAME]] calcularà quan es reproduirà utilitzant quants **segons per hora** o com un **Percentatge** ingressat en la programació.

{feat}Interrupt Layouts|v4{/feat}

{tip}
¡Això pot ser útil si tens Anuncis que necessiten mostrar-se durant una quantitat particular de temps dins de la programació habitual!
{/tip}

- Selecciona **Disseny d'Interrupció** com el Tipus d'Esdeveniment des del menú desplegable a l'afegir un Esdeveniment.
- Completa els camps del formulari per crear la programació.

#### Quota de Veu (Share of Voice)

Ingressa la quantitat de temps que el Disseny ha de mostrar-se en segons per hora o com un percentatge (0 - 100%) de la durada dels esdeveniments (la diferència entre la data d'inici i la data de finalització) que el **Disseny d'Interrupció** ha d'ocupar en la programació habitual.

{tip}
**Tingues en compte:** Si el teu Disseny 'principal' té una llarga durada, el Disseny d'Interrupció pot mostrar-se en un bloc per satisfer els criteris SoV ingressats.
{/tip}

### Acció

Les **Accions Programades** escolten un Codi d'Activador que arriba en un webhook per Navegar a un Disseny o executar un Comandament.

{feat}Scheduled Action Events|v4{/feat}

- **Navegar a Disseny** - ingressa el codi identificador per al Disseny al qual el Reproductor ha de navegar quan s'activa. Aquest codi es crea a l'afegir un nou Disseny o a l'editar un existent des de la quadrícula de Dissenys.
- **Comandament** - selecciona el Comandament a executar.

## Esdeveniments Sincronitzats

{feat}Sync Events|v4{/feat}

{tip}
Els Esdeveniments Sincronitzats s'utilitzen juntament amb [Grups de Sincronització](displays_sync_groups.html) per mostrar configuracions en mirall o de videowall a través de 2 o més Pantalles.

¡Assegura't d'haver creat i configurat un **Grup de Sincronització** abans de programar!
{/tip}

Fes clic al botó **Afegir Esdeveniment Sincronitzat** a la part superior de la quadrícula de programació per obrir el formulari **Afegir Esdeveniment Sincronitzat**.

Selecciona un [Grup de Sincronització](displays_sync_groups.html) des del menú desplegable.

- Usa el menú desplegable **Disseny** per seleccionar quin contingut ha de mostrar-se en cada Pantalla dins del grup.

{tip}
Al seleccionar diferent contingut per mostrar en una configuració de paret en Pantalles, la durada total serà imposada pel contingut en la Pantalla Líder.

La Pantalla Líder emetrà instruccions per canviar la seqüència segons el seu contingut assignat. Tingues en compte que altres Pantalles dins del grup podrien dessincronitzar-se si el seu contingut no és similar en disseny (mateix nombre d'elements, durades, etc.).
{/tip}

- Selecciona **Mirall** per establir automàticament el mateix element en cada Pantalla dins del grup automàticament.

{tip}
Sincronitza [Llistes de Reproducció](media_module_playlists.html) en diferents Dissenys usant una **Clau de Sincronització de Contingut**.
{/tip}

### Particions del Dia (Dayparts)

- Els Esdeveniments es programen usant informació de **Partició del Dia**:
  - Selecciona **Personalitzat** per ingressar les teves pròpies hores d'inici i fi. Usa la casella de verificació **Temps Relatiu** per ingressar les Hores i Minuts al crear un Esdeveniment Programat (no disponible per Esdeveniments Sincronitzats).
  - Selecciona **Sempre** per tenir el contingut sempre programat en la Pantalla seleccionada.

{tip}
¡Crea les teves pròpies [Particions del Dia](scheduling_dayparting.html) definides per seleccionar per a una programació encara més fàcil!
{/tip}

- Usa el menú desplegable per seleccionar el que necessita ser programat de la llista.

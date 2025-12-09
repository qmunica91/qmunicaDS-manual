---
toc: "scheduling"
maxHeadingLevel: 3
minHeadingLevel: 2
aliases:
  - "layouts_interrupt"
  - "scheduling"
  - "schedule_now"
excerpt: "Crea Programaciones para mostrar tu contenido en el momento y lugar adecuados"
keywords: "sincronizado, espejo, videowall, acciones programadas, programación de medios, diseño de interrupción"
---

# Programación 

Las Programaciones se crean desde la página **Programación** del menú principal del CMS e incluyen los siguientes Tipos de Eventos:

### Comando

Selecciona un [Comando](displays_command_functionality.html) para ser ejecutado por el Reproductor en un punto específico en el tiempo.

{tip}
Los Eventos de Comando no requieren un `toDt`.

El Orden de Visualización y la Prioridad son irrelevantes cuando se trata de ejecutar Comandos, pero pueden establecerse en el CMS para fines organizativos.
{/tip}

### Diseño de Superposición

Los Diseños que han sido diseñados como un [Diseño de Superposición](layouts_overlay.html) se programarán al mismo tiempo que los Diseños existentes para crear una superposición de contenido cuando se muestren.

### Diseño de Interrupción

Un Diseño de Interrupción programará un Diseño seleccionado para reproducirse **entre** otros Diseños en la 'programación habitual'.

[[PRODUCTNAME]] calculará cuándo se reproducirá utilizando cuántos **segundos por hora** o como un **Porcentaje** ingresado en la programación.

{feat}Interrupt Layouts|v4{/feat}

{tip}
¡Esto puede ser útil si tienes Anuncios que necesitan mostrarse durante una cantidad particular de tiempo dentro de la programación habitual!
{/tip}

- Selecciona **Diseño de Interrupción** como el Tipo de Evento desde el menú desplegable al añadir un Evento.
- Completa los campos del formulario para crear la programación.

#### Cuota de Voz (Share of Voice)

Ingresa la cantidad de tiempo que el Diseño debe mostrarse en segundos por hora o como un porcentaje (0 - 100%) de la duración de los eventos (la diferencia entre la fecha de inicio y la fecha de finalización) que el **Diseño de Interrupción** debe ocupar en la programación habitual.

{tip}
**Ten en cuenta:** Si tu Diseño 'principal' tiene una larga duración, el Diseño de Interrupción puede mostrarse en un bloque para satisfacer los criterios SoV ingresados.
{/tip}

### Acción

Las **Acciones Programadas** escuchan un Código de Activador que llega en un webhook para Navegar a un Diseño o ejecutar un Comando.

{feat}Scheduled Action Events|v4{/feat}

- **Navegar a Diseño** - ingresa el código identificador para el Diseño al que el Reproductor debe navegar cuando se activa. Este código se crea al añadir un nuevo Diseño o al editar uno existente desde la cuadrícula de Diseños.
- **Comando** - selecciona el Comando a ejecutar.

## Eventos Sincronizados

{feat}Sync Events|v4{/feat}

{tip}
Los Eventos Sincronizados se utilizan junto con [Grupos de Sincronización](displays_sync_groups.html) para mostrar configuraciones en espejo o de videowall a través de 2 o más Pantallas.

¡Asegúrate de haber creado y configurado un **Grupo de Sincronización** antes de programar!
{/tip}

Haz clic en el botón **Añadir Evento Sincronizado** en la parte superior de la cuadrícula de programación para abrir el formulario **Añadir Evento Sincronizado**.

Selecciona un [Grupo de Sincronización](displays_sync_groups.html) desde el menú desplegable.

- Usa el menú desplegable **Diseño** para seleccionar qué contenido debe mostrarse en cada Pantalla dentro del grupo.

{tip}
Al seleccionar diferente contenido para mostrar en una configuración de pared en Pantallas, la duración total será impuesta por el contenido en la Pantalla Líder.

La Pantalla Líder emitirá instrucciones para cambiar la secuencia según su contenido asignado. Ten en cuenta que otras Pantallas dentro del grupo podrían desincronizarse si su contenido no es similar en diseño (mismo número de elementos, duraciones, etc.).
{/tip}

- Selecciona **Espejo** para establecer automáticamente el mismo elemento en cada Pantalla dentro del grupo automáticamente.

{tip}
Sincroniza [Listas de Reproducción](media_module_playlists.html) en diferentes Diseños usando una **Clave de Sincronización de Contenido**.
{/tip}

### Particiones del Día (Dayparts)

- Los Eventos se programan usando información de **Partición del Día**:
  - Selecciona **Personalizado** para ingresar tus propias horas de inicio y fin. Usa la casilla de verificación **Tiempo Relativo** para ingresar las Horas y Minutos al crear un Evento Programado (no disponible para Eventos Sincronizados).
  - Selecciona **Siempre** para tener el contenido siempre programado en la Pantalla seleccionada.

{tip}
¡Crea tus propias [Particiones del Día](scheduling_dayparting.html) definidas para seleccionar para una programación aún más fácil!
{/tip}

- Usa el menú desplegable para seleccionar lo que necesita ser programado de la lista.

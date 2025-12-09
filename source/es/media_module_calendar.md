---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
alias: "media_module_agenda"
excerpt: "Muestra eventos de Calendario extraídos de un feed iCal"
keywords: "feed ical"
---

# Calendario

Muestra eventos de Calendario extraídos de un feed iCal en cualquier lugar de un Diseño usando **Elementos** o selecciona una **Plantilla Estática** para mostrar resultados en Diseños/Listas de Reproducción.

{feat}Calendar View|v4{/feat}

Los datos del Calendario son proporcionados por un feed iCal que alimentará los Elementos configurados y las Plantillas Estáticas.

{tip}
Asegúrate de que la URL del feed ICS esté disponible para el CMS. Si el feed se carga en un navegador sin autenticación, entonces el feed debería mostrarse en el CMS sin problemas.

Para más información sobre cómo ver tu Google Calendar en aplicaciones, usa el siguiente enlace seleccionando la opción **Obtener tu calendario (solo vista)**: https://support.google.com/calendar/answer/37648?hl=es
{/tip}

## Elementos de Calendario

Los Elementos están disponibles para selección al añadir el Widget de Calendario a un [Diseño](layouts_editor.html) para dar a los Usuarios más control sobre qué componentes del Widget de Calendario usar y dónde se pueden colocar.

![Calendar Elements](img/v4_media_modules_calendar_elements.png)

Cada Elemento tiene un conjunto de opciones de configuración en el Panel de Propiedades. Ingresa el feed iCal para usar para devolver resultados desde la pestaña **Configurar**.

Controla cómo los artículos deben ciclarse especificando una [Ranura de Datos](https://test.xibo.org.uk/manual/en/layouts_editor.html#content-data-slots) para usar para cada uno de los Elementos añadidos. Los Elementos de Datos pueden complementarse aún más añadiendo Elementos Globales para añadir formas y texto que se pueden poner en un Grupo de Elementos para una configuración y posicionamiento más fáciles.

Aprovecha las Plantillas (Stencils) para añadir un grupo prediseñado de Elementos a tu Diseño.

{tip}
¡Todos los Elementos en la Plantilla se tratan como 'uno' cuando se configuran y se pueden duplicar fácilmente con un clic derecho!
{/tip}

## Plantillas Estáticas de Calendario

Las Plantillas Estáticas definen cómo deben organizarse y estilizarse los resultados devueltos y son una manera simple de mostrar tus datos usando plantillas preestilizadas.

![Calendar Elements](img/v4_media_modules_calendar_templates.png)

Las Plantillas se pueden configurar para hacer cambios en la apariencia del diseño usando una gama de opciones en el Panel de Propiedades. Ingresa un iCal para devolver resultados desde la pestaña **Configurar** para cada Plantilla añadida al Diseño/Lista de Reproducción.

## Descripción General

- Devuelve eventos dentro de un rango de fechas especificado.
- Opciones para excluir eventos de todo el día y actuales del feed para que no se muestren.
- Usar zonas horarias de eventos y calendario.
- Establecer duración por elemento.
- Especificar cuántos eventos mostrar.
- Ejecutar un disparador de Web Hook cuando se detecten ciertas condiciones.
- Los datos para este medio son almacenados en caché por los Reproductores para reproducción fuera de línea.

### Disparadores de Web Hook

Dispara una [Acción](layouts_interactive_actions.html) de Web Hook cuando hay un **Evento Actual** o **Sin Evento** desde la pestaña Disparador.

{tip}
**Escenario de Ejemplo**:

Un usuario tiene un calendario de sala de reuniones configurado usando el Widget de Calendario en un Diseño que muestra la ocupación actual para una sala y le gustaría cambiar las luces LED para mostrar cuando está vacante o en uso.

- El usuario primero necesitaría crear [Comandos de Shell](displays_command_functionality.html#content-shell-commands) que emitieran comandos a un dispositivo LED IoT o a los LED integrados en algunas de las Pantallas Comerciales de Philips.
- A continuación, una [Acción Interactiva](layouts_interactive_actions.html) necesitaría definirse en el **Diseño**, que **Navegaría a Widget** y **Apuntaría a la Pantalla**, con el [Widget de Comando de Shell.](media_module_shellcommand.html)
- Desde la pestaña **Disparador**, asigna los códigos para disparar los **Web Hooks** para **Evento Actual** y **Sin Evento**.

{/tip}

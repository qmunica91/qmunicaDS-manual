---
toc: "configure"
maxHeadingLevel: 3
minHeadingLevel: 2
alias: "tour_transitions"
excerpt: "Opciones de Gestión de Transiciones para Usuarios"
keywords: "predeterminados de transición, fundido de entrada, fundido de salida, volar, transiciones de lista de reproducción, transiciones de salida"
---

# Gestión de Transiciones

{feat}Transitions|v4{/feat}

{version}

**Nota:** Las transiciones no son compatibles con Reproductores Tizen para los siguientes Widgets:

- [Vídeo](media_module_video.html)
- [Entrada de Vídeo](media_module_video_in.html)
- [Vídeo Local](media_module_localvideo.html)

{/version}

Las transiciones se gestionan desde la página **Transiciones** bajo la sección **Administración** del menú principal del CMS. Configura qué Transiciones deben estar disponibles para los Usuarios para asignación a elementos de Medios:

![Transitions Grid](img/v4_tour_transitions_grid.png)

- **Fundido de Entrada (Fade In)** - Aumenta Opacidad de 0 a 100.
- **Fundido de Salida (Fade Out)** - Disminuye Opacidad de 100 a 0.
- **Volar (Fly)** - Volar hacia adentro o afuera en un punto cardinal.

## Predeterminados de Transición

{version}
Los valores predeterminados globales se pueden establecer para Transiciones por Administradores desde la página de [Ajustes del CMS](tour_cms_settings.html#content-defaults).
{/version}

Las Transiciones Predeterminadas se pueden habilitar fácilmente para todos los Widgets añadidos a un Diseño marcando la casilla **¿Aplicar Transiciones automáticamente?** desde el panel de propiedades del Diseño:

![Transitions Layout](img/v4_tour_transitions_layout.png)

{version}

**NOTA:** Cuando se han aplicado Predeterminados de Transición, los campos de Transición del Widget se mostrarán como entradas en blanco:

![Transitions Widget](img/v4_tour_transitions_widget.png)

Esto es porque solo las Transiciones ingresadas **manualmente** para un Widget se mostrarán en los campos del formulario.
{/version}

## Transiciones de Lista de Reproducción

Estas son las Transiciones entre **elementos de Medios** en una [Lista de Reproducción](media_playlists.html) y se establecen como transiciones de **Entrada** y **Salida**.

{tip}
El formulario de Transición se adapta dependiendo de la Transición seleccionada y las opciones disponibles para esa transición. En la mayoría de los casos es necesario seleccionar una duración para la Transición en Milisegundos y en el caso de Volar, también se debe seleccionar una dirección.
{/tip}

## Transición de Salida de Lista de Reproducción

Una Transición de Salida de Lista de Reproducción ocurre cuando el último Elemento de Medios que se muestra en una [Lista de Reproducción](media_playlists.html) se muestra y permite establecer una Transición de Salida diferente.
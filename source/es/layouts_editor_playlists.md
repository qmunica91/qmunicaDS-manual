---
toc: "layouts"
maxHeadingLevel: 3
minHeadingLevel: 2
aliases: 
   - "media_module_subplaylist"   
excerpt: "Crea o Añade Listas de Reproducción directamente a un Diseño desde el Editor de Diseños"
keywords: "línea de tiempo de contenido, pase de diapositivas, clave de sincronización de contenido, añadiendo listas de reproducción a un diseño, convertir lista de reproducción, lista de reproducción guardada, reproducción basada en ciclos, widget aleatorio"
persona: "content creator, super administrator, user"
---

# Listas de Reproducción

Las Listas de Reproducción se usan para mostrar una secuencia de elementos multimedia (como una presentación de imágenes). Hay dos formas de crear una Lista de Reproducción:

- Añadir Listas de Reproducción directamente a un Diseño desde el Editor de Diseños. Las Listas de Reproducción locales se pueden convertir para guardarlas para su reutilización como una Lista de Reproducción global. Las Listas de Reproducción guardadas se mostrarán en el Editor de Diseños para añadirlas a los Diseños.
- Crear [Listas de Reproducción](media_playlists.html#content-creating-a-playlist) independientemente de un Diseño. Las Listas de Reproducción globales pueden programarse en Pantallas sin la creación de un Diseño. Las Listas de Reproducción creadas fuera del Editor de Diseños todavía se muestran para selección desde la función Añadir Lista de Reproducción del Editor de Diseños.

## Añadir Listas de Reproducción

Crea nuevas o selecciona Listas de Reproducción existentes para usar desde el **Editor de Diseños** para crear una línea de tiempo de contenido para mostrar en un Diseño.

## Resumen de Características:

- Crea y configura directamente en un Diseño.
- Convierte una Lista de Reproducción creada en un Diseño a una Lista de Reproducción Global para guardarla para uso futuro.
- Muestra fácilmente un 'pase de diapositivas' de contenido contenido en una o más Listas de Reproducción.
- Sincroniza con Listas de Reproducción en otros Diseños que son parte de un Evento Sincronizado.
- Combina contenido de una variedad de Listas de Reproducción para mostrar.
- Establece el número máximo de elementos a mostrar de una Lista de Reproducción.
- Controla cuánto tiempo debe mostrarse cada elemento en una Lista de Reproducción antes de pasar al siguiente elemento.
- Establece Fechas de Caducidad para elementos multimedia añadidos a una Lista de Reproducción.
- Reproduce un elemento por ciclo para un recuento de reproducción especificado.
- Selecciona un Widget Aleatorio para reproducir en cada ciclo.
- Cicla a través de los elementos contenidos en una Lista de Reproducción en el visor para ver fácilmente la secuencia.

## Añadiendo Listas de Reproducción a un Diseño

- Desde el [Editor de Diseños](layouts_editor), haz clic en **Añadir Listas de Reproducción** desde la **Caja de Herramientas**:

![Add Playlists](img/v4.1_layouts_editor_add_playlists.png)

- Haz clic para Añadir o arrastra una **Nueva Lista de Reproducción** o una Lista de Reproducción con nombre que ya haya sido creada.
- Redimensiona y posiciona:

![Content Synchronisation Key](img/v4.1_layouts_editor_synchronisation_key.png)

Desde el **Panel de Propiedades**, usa la **Clave de Sincronización de Contenido** para sincronizar con Listas de Reproducción en otros Diseños. Las Listas de Reproducción con la misma clave se sincronizarán cuando el Diseño se programe como un [Evento Sincronizado.](scheduling_events.html#content-synchronised-events)

{tip}
**Escenario:**

Tienes un Evento Sincronizado con 3 Pantallas y 3 Diseños diferentes. Cada Diseño tiene un Texto en la parte superior y una Lista de Reproducción en el medio que las 3 necesitan reproducir en sincronía. 

También podrías establecer dos Listas de Reproducción diferentes para sincronizar de manera diferente, lo que podrías establecer en `sync_1` y `sync-2` por ejemplo.
{/tip}

- Opcionalmente, establece **Transiciones** para elementos en una Lista de Reproducción desde el Panel de Propiedades.

{tip}
Cuando se han aplicado Transiciones por defecto, el panel de propiedades estará en blanco. Solo las Transiciones ingresadas manualmente se mostrarán en los formularios.
Los valores predeterminados pueden anularse desmarcando la casilla de verificación **Aplicar Transiciones automáticamente** desde el Panel de Propiedades para el Diseño.
{/tip}

- Haz clic en el icono en la esquina derecha de la Lista de Reproducción para abrir el [Editor de Listas de Reproducción](media_playlists.html#content-playlist-editor) para añadir y configurar contenido.

{tip}
El [Editor de Listas de Reproducción](media_playlists.html#content-playlist-editor) incluye Widgets de **Espaciador** y **Texto Enriquecido** que solo están disponibles para su uso con Listas de Reproducción.

Los medios añadidos a una Lista de Reproducción también pueden tener horas de Inicio y Fin usando [Fechas de Caducidad](media_playlists.html#content-widget-expiry-dates).
{/tip}

{version}
**Nota:** Si añades una Lista de Reproducción con nombre que ya ha sido creada, cualquier edición realizada en la Lista de Reproducción se aplicará en todas partes donde se esté utilizando la Lista de Reproducción actualmente.
{/version}

- Haz clic en el botón **Atrás** en la parte superior para salir del Editor de Listas de Reproducción y volver al Editor de Diseños.

Mira todo el contenido que se ha añadido a la Línea de Tiempo de la Lista de Reproducción utilizando las flechas en la parte inferior derecha de la Lista de Reproducción en el Diseño.

- Cicla a través del orden del contenido:

![Preview Timeline Content](img/v4.1_layouts_editor_playlists_preview_content.png)

## Convertir Lista de Reproducción

Si añades una **Nueva Lista de Reproducción** al Diseño, puedes optar por convertirla en una Lista de Reproducción guardada. Las Listas de Reproducción convertidas se mostrarán para la selección de Listas de Reproducción en el Editor de Diseños y desde la cuadrícula de [Listas de Reproducción](media_playlists.html#content-playlists-grid).

- Haz clic en la Lista de Reproducción en el Diseño para seleccionarla y dale un **Nombre** desde la pestaña **General** del **Panel de Propiedades**.
- Haz clic derecho y selecciona **Convertir Lista de Reproducción** desde el menú.

![Convert Playlist](img/v4.1_layouts_editor_convert_playlist.png)

Verás un mensaje emergente en la parte inferior del Editor de Diseños para decir que la Lista de Reproducción se ha guardado como una Lista de Reproducción Global.

{tip}
¡Haz clic en el botón **Mostrar más** para ver tu Lista de Reproducción añadida a la lista de Listas de Reproducción disponibles!
{/tip}

Las Listas de Reproducción convertidas se guardarán en la [Cuadrícula de Listas de Reproducción](media_playlists.html#content-playlist-grid).

## Añadir a la Lista de Reproducción

Si tienes una **Nueva Lista de Reproducción** en un Diseño, puedes añadir una nueva o global Lista de Reproducción a la Línea de Tiempo para abrir más opciones en el Panel de Propiedades para configuración:

![Playlist Spots](img/v4.1_layouts_editor_playlist_spots.png)

- Selecciona Listas de Reproducción, Opciones de Lugar y Ordenación de Lista de Reproducción, al seleccionar más de una Lista de Reproducción para [Incrustar](media_playlists.html#content-embedding-playlists) desde el Panel de Propiedades.

Añadir una **Lista de Reproducción** a una **Nueva Lista de Reproducción** en un Diseño tiene opciones adicionales de [Reproducción Basada en Ciclos](layouts_editor_playlists.html#content-cycle-based-playback) que incluye una característica de Widget Aleatorio.

{tip}
Si deseas añadir más de una Lista de Reproducción para combinar el orden de reproducción, recomendamos que solo añadas una Lista de Reproducción a la Línea de Tiempo y luego uses las opciones en el Panel de Propiedades para seleccionar las Listas de Reproducción adicionales y configurar.
{/tip}

- ### Reproducción Basada en Ciclos

Una vez habilitada, todas las Listas de Reproducción seleccionadas se tratarán como una "lista" y solo mostrarán un Widget cada vez que se reproduzca el Diseño, ciclando a través del contenido de todas las Listas de Reproducción añadidas:

- Marca Habilitar reproducción basada en ciclos desde el Panel de Propiedades.
- Proporciona un **Recuento de Reproducción** para determinar cuántas reproducciones debe tener cada Widget en la Lista de Reproducción antes de pasar al siguiente Widget en la línea de tiempo.

![Cycle Playback](img/v4.1_layouts_editor_playlist_cycle_playback.png)

Usar la opción **Widget aleatorio en cada ciclo** reproducirá un Widget de la línea de tiempo al azar para cada ciclo.

{version}
**Nota:** ¡Estas opciones adicionales **no** están disponibles al añadir una o más Listas de Reproducción a una línea de tiempo de [Lista de Reproducción Global](media_playlists.html#content-feature-overview), que se ha añadido directamente al Diseño!
{/version}

{tip}
¿Sabías que las [Listas de Reproducción](media_playlists.html) creadas y gestionadas independientemente de los Diseños no requieren más derechos de acceso de usuario a los Diseños o al Editor de Diseños para añadir y gestionar contenido?
{/tip}

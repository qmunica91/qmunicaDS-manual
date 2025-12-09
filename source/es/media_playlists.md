---
toc: "media"
maxHeadingLevel: 3
minHeadingLevel: 2
aliases:
  - "layouts_timeline"
  - "media_module_spacer"
  - "media_module_text"
excerpt: "Las Listas de Reproducción contienen una línea de tiempo de contenido ordenado que puede reutilizarse en múltiples Diseños"
keywords: "reutilizable, presentación de diapositivas, añadir múltiples elementos, mostrar una secuencia de contenido, programar listas de reproducción, lista de reproducción dinámica, editor de lista de reproducción, widget espaciador, widget de texto, fechas de vencimiento de widget, spots, orden de reproducción, incrustar listas de reproducción"
---

# Listas de Reproducción

Las Listas de Reproducción se utilizan para mostrar una secuencia de elementos multimedia (como una presentación de imágenes). Hay dos formas de crear una Lista de Reproducción:

- Crear [Listas de Reproducción](media_playlists) de forma independiente a un Diseño. Las Listas de Reproducción Globales pueden programarse en Pantallas sin la creación de un Diseño. Las Listas de Reproducción creadas fuera del Editor de Diseños aún se muestran para su selección desde la función Añadir Lista de Reproducción desde el Editor de Diseños.
- Añadir Listas de Reproducción directamente a un Diseño desde el Editor de Diseños. Las Listas de Reproducción Locales pueden convertirse para guardarse para su reutilización como una Lista de Reproducción global. Las Listas de Reproducción guardadas se mostrarán en el Editor de Diseños para añadir a los Diseños.

## Resumen de Características:

- Crear y configurar independientemente de los Diseños.
- Añadir y mantener contenido [dinámicamente](media_playlists.html#content-dynamically-adding-media).
- Actualizar contenido de Lista de Reproducción sin acceder a los Diseños.
- Programar directamente desde la cuadrícula de Listas de Reproducción sin necesidad de añadir a un Diseño.
- Combinar contenido de una variedad de Listas de Reproducción para mostrar.
- Establecer el número máximo de elementos a mostrar de una Lista de Reproducción.
- Controlar cuánto tiempo debe mostrarse cada elemento en una Lista de Reproducción antes de pasar al siguiente elemento.
- Establecer Fechas de Vencimiento para elementos multimedia añadidos a una Lista de Reproducción.

## Creando una Lista de Reproducción

Optimiza recursos y ahorra tiempo creando Listas de Reproducción para mantener múltiples elementos de contenido para mostrar en Pantallas. Crea Listas de Reproducción para dirigir y recopilar contenido para requisitos específicos, ubicaciones, categorías de temas, etc.

Las Listas de Reproducción que se crean independientemente de los Diseños y no requieren acceso adicional de Usuario a Diseños o al Editor de Diseños para añadir o gestionar contenido en Listas de Reproducción. Cualquier cambio realizado en una Lista de Reproducción se actualizará en todos los Diseños/Programaciones que ya contienen esa Lista de Reproducción.

- Selecciona **Listas de Reproducción** bajo la sección **Biblioteca** del menú principal del CMS.

- Haz clic en el botón **Añadir Lista de Reproducción** y completa los campos del formulario:

![Add Playlist](img/v4_media_playlists_add.png)

- Dale a tu Lista de Reproducción un **Nombre** para una identificación fácil en el CMS.

Hay dos opciones para añadir contenido de [Medios](media_library) a Listas de Reproducción:

- Asignar automáticamente medios basados en Biblioteca según criterios usando la opción [Dinámica](media_playlists.html#content-dynamically-adding-media).
- Asignar manualmente medios usando el [Editor de Listas de Reproducción](media_playlists.html#content-media-playlists), que se abrirá al guardar el formulario.

## Añadiendo Medios Dinámicamente

- Una vez marcado, haz clic en la pestaña **Filtro** y establece los criterios requeridos para poblar Medios de Biblioteca coincidentes.
- Proporciona un **número máximo** de archivos de Medios de Biblioteca para limitar el número que puede asignarse automáticamente.

Se mostrarán los Medios ya en la Biblioteca del CMS que coinciden con los criterios establecidos:

![Dynamic Assignment](img/v4_media_playlists_dynamic.png)

Cualquier archivo de medios futuro que se añada a la Biblioteca que cumpla con los criterios establecidos para esta Lista de Reproducción se añadirá automáticamente a esta lista.

{tip}
¡Los Medios de Biblioteca también pueden prepoblarse como una asignación única a una Lista de Reproducción estableciendo criterios pero dejando la opción Dinámica desmarcada!
{/tip}

- Haz clic en **Guardar**.

{tip}
¿Sabías que una Lista de Reproducción Dinámica puede programarse para mostrarse en Pantallas a pantalla completa sin añadirla primero a un Diseño? ¡Usa el menú de fila para la Lista de Reproducción y selecciona Programar!
{/tip}

## Editor de Listas de Reproducción

- Desde la Caja de Herramientas, selecciona contenido para añadir a la Lista de Reproducción.
- Las opciones de configuración se cargarán en el panel de propiedades.

![Playlist Timeline](img/v4_media_playlists_timeline.png)

{tip}
El **Editor de Listas de Reproducción** contiene dos Widgets adicionales, un **Editor de Texto Enriquecido** para proporcionar texto, Html o JavaScript y un **Espaciador** para crear un 'espacio' vacío dentro de una Lista de Reproducción.
{/tip}

Las duraciones se actualizarán para mostrar los minutos/segundos a medida que se añaden elementos a la línea de tiempo de la Lista de Reproducción.

- Reordena la secuencia arrastrando y soltando.

- Haz clic en el icono de regla para **Cambiar modo de Escala**:

![Scale Mode](img/v4_media_playlists_scale_mode.png)

Usa las opciones de escala para acercar y alejar para disminuir/aumentar el lapso de tiempo visible.

Los elementos pueden añadirse a un punto específico en la lista, arrastra o haz clic para añadir contenido a un marcador de posición dentro de la Lista de Reproducción.

![Add to Timeline](img/v4_media_playlists_add_timeline.png)

{tip}
Usa el botón Deshacer en la parte inferior de la barra de herramientas para revertir un cambio.
{/tip}

Se puede acceder a un Menú Contextual adicional de opciones haciendo clic derecho en un elemento que incluye establecer [Fechas de Vencimiento de Widget](media_playlists.html#content-widget-expiry-dates) y Transiciones de Lista de Reproducción.

{tip}
Cuando las Transiciones se aplican a un Widget por defecto, el panel de propiedades estará en blanco. ¡Solo las Transiciones ingresadas manualmente se mostrarán en los formularios!
{/tip}

Usa el botón **Seleccionar Múltiples Widgets** en la parte inferior del Editor de Listas de Reproducción para eliminar múltiples selecciones con un solo clic:

![Mutli Select](img/v4_media_playlists_multi_select.png)

{tip}
¿Sabías que una Lista de Reproducción 'global' puede programarse para mostrarse en Pantallas a pantalla completa sin añadirla primero a un Diseño? ¡Usa el menú de fila para la Lista de Reproducción y selecciona Programar!
{/tip}

## Fechas de Vencimiento de Widget

Los elementos añadidos a una Lista de Reproducción tienen una opción adicional de establecer tiempos de Inicio y Fin.

{feat}Widget Expiry Dates|v4{/feat}

- Haz clic derecho en un elemento en una Lista de Reproducción para **Editar Fechas de Vencimiento** o establecer al subir medios directamente a una Lista de Reproducción.

Subir desde una [Búsqueda en la Biblioteca](layouts_editor_using_library_search.html) tendrá una opción adicional **Establecer Fecha de Vencimiento**:

![Expiry Dates](img/v4_media_playlists_upload_expiry.png)

Al subir múltiples archivos de medios, hacer clic en el botón **Iniciar carga** subirá todos los archivos con la misma fecha/hora y ubicación de Carpeta establecidas.

{tip}
Los elementos también pueden subirse individualmente usando el botón **carga azul** al final de la fila para que un archivo tenga diferentes Fechas de Vencimiento y ubicaciones de Carpeta establecidas para cada archivo subido.
{/tip}

Cualquier elemento en una Lista de Reproducción que tenga **Fechas de Vencimiento** establecidas muestra un icono, que al pasar el ratón mostrará más información:

![Expiry Dates](img/v4_media_playlists_expiry_dates.png)

{tip}
Una vez que la fecha de Finalización ha pasado, el elemento se eliminará de la Lista de Reproducción. Los elementos vencidos que no se hayan configurado para Eliminar al Vencer permanecerán visibles en el Editor de Listas de Reproducción solo para que los tiempos de Inicio y Fin puedan reajustarse si es necesario.
{/tip}

- Haz clic en un icono para abrir y realizar cualquier cambio/eliminar del elemento.

## Incrustando Listas de Reproducción

Las Listas de Reproducción se pueden añadir a otras líneas de tiempo de Listas de Reproducción para definir qué tanto contenido debe mostrarse, por cuánto tiempo, así como determinar un orden de reproducción.

- Desde el Editor de Listas de Reproducción selecciona añadir una Nueva o selecciona de la lista de Listas de Reproducción 'globales' disponibles desde la Caja de Herramientas.
- Las opciones de configuración se muestran en el Panel de Propiedades:

![Embedding Playlists](img/v4.1_media_playlists_embedding.png)

- Usa el menú desplegable para seleccionar **Listas de Reproducción** usando el botón `+` para añadir y configurar múltiples Listas de Reproducción si es necesario.

- Las opciones de **Spot** se utilizan para definir qué tanto contenido de las Listas de Reproducción debe mostrarse y por cuánto tiempo.

Los Spots también tienen una opción para usar el contenido de una Lista de Reproducción como relleno solamente y añadir contenido de esta Lista de Reproducción para **Llenar** o **Rellenar** otras Listas de Reproducción seleccionadas:

- Esta Lista de Reproducción debe ser la **primera** Lista de Reproducción añadida en la lista.
- Ingresa un **0** en el campo **Spots** para que toda la Lista de Reproducción sea ignorada y omitida del orden de reproducción. Selecciona cómo debe distribuirse el contenido de esta Lista de Reproducción con las otras Listas de Reproducción usando las opciones **Relleno de Spot**.

{version}
**Nota:** Ten en cuenta que al establecer **Fechas de Inicio** a los Widgets puede causar que se muestren menos Spots que la cantidad total especificada.
{/version}

Usa el menú desplegable para el campo **Relleno de Spot** para seleccionar cómo deben llenarse los Spots restantes en el caso de que no haya suficientes Widgets en la Lista de Reproducción seleccionada para cumplir con los spots de reproducción especificados.

{tip}
¡**Spots**, **Duración de Spot** y **Relleno de Spot** son todos opcionales y pueden dejarse en blanco si esta funcionalidad no es requerida!
{/tip}

Usa el desplegable para **Orden de Lista de Reproducción** para seleccionar cómo deben ordenarse todas las Listas de Reproducción para reproducirse.

{tip}
**Auto** usa el recuento total de elementos en cada lista y lo divide por la lista más pequeña para determinar con qué frecuencia tomar elementos de cada lista para asegurar una reproducción uniforme de cada Lista de Reproducción.
{/tip}

Selecciona de las opciones **Widgets Restantes** para manejar cualquier contenido que quede sin ordenar al final de una Lista de Reproducción.

{tip}
Añadir Listas de Reproducción a una **Nueva Lista de Reproducción** en un Diseño tiene una opción adicional de Reproducción Basada en Ciclos que incluye una función de **Widget Aleatorio**.
¡La reproducción basada en ciclos no es compatible al añadir Listas de Reproducción a una Lista de Reproducción global!
{/tip}

## Cuadrícula de Lista de Reproducción

Las Listas de Reproducción guardadas se pueden ver desde **Listas de Reproducción** bajo la sección **Biblioteca** del menú principal del CMS:

![Playlist Grid](img/v4.1_media_playlists_grid.png)

Cada Lista de Reproducción tiene un menú de fila que se utiliza para acceder a un menú de acciones/atajos, las configuraciones notables se enumeran a continuación:

- **Línea de Tiempo** - abre el Editor de Listas de Reproducción para hacer cambios en el contenido en la línea de tiempo.
- **Editar** - usa la pestaña Filtro para Listas de Reproducción Dinámicas para ver la lista de medios asignados dinámicamente y hacer cambios en los criterios.
- **Informe de Uso** - ve dónde se muestran las Listas de Reproducción y en qué Diseños se han incluido.
- **Programar** - Programa directamente una Lista de Reproducción para que se muestre a pantalla completa en Pantallas.

{tip}
Cualquier cambio realizado en una Lista de Reproducción Programada se enviará automáticamente a los Reproductores a medida que se realicen.
{/tip}

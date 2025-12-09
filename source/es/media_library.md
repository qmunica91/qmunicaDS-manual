---
toc: "media"
maxHeadingLevel: 3
minHeadingLevel: 2
aliases:
  - "media"
  - "media_tidylibrary"
  - "media_resizing_images"
excerpt: "Gestiona medios basados en archivos desde la Biblioteca del CMS"
keywords: "subir medios a biblioteca, añadir medios vía url, fechas de vencimiento de biblioteca de medios, retirar medios, habilitar recolección de estadísticas de medios, actualizar medios, reemplazar medios, informe de uso, limpiar biblioteca, lista de purga, programación"
---

# Biblioteca de Medios

[[PRODUCTNAME]] admite una amplia variedad de tipos de medios, desde Widgets que se crean y almacenan directamente en Diseños y Listas de Reproducción hasta medios basados en archivos que se suben y almacenan en la Biblioteca del CMS que luego se pueden reutilizar a través de múltiples Diseños y Listas de Reproducción.

{version}
**NOTA:** [[PRODUCTNAME]] no toma medidas para controlar qué contenido se coloca en tus Pantallas. Es tu responsabilidad asegurar que tu contenido sea material apropiado para tu audiencia deseada. El contenido debe atribuirse adecuadamente si no posees los derechos sobre él.
{/version}

Gestiona todos los medios basados en archivos seleccionando **Medios** bajo la sección **Biblioteca** del menú principal del CMS:

![Media Library](img/v4_media_library_grid.png)

Usa los múltiples campos de filtro en la parte superior de la cuadrícula para restringir los criterios para los resultados devueltos.

{tip}
Usa la opción **O/Y** para **Nombres** y para filtrar elementos que se han asignado a múltiples **Etiquetas**.

Las Imágenes y Vídeos que tienen una miniatura configurada también se pueden filtrar por **Orientación** una vez configurada:

- Usa el menú de fila para el elemento y selecciona **Editar** para un archivo de Imagen/Vídeo.

- Desplázate hasta la parte inferior del formulario y establece la **Orientación** prevista.
{/tip}

## Añadiendo Medios a la Biblioteca

Los medios de la biblioteca se pueden subir directamente usando el botón **Añadir Medios** o proporcionando una URL usando el botón **Añadir Medios (URL)**.

{tip}
¡Añade Medios a la Biblioteca del CMS y guarda en Carpetas para tener medios listos para usar para los Usuarios/Grupos de Usuarios apropiados!

Los archivos añadidos a la Biblioteca del CMS se pueden añadir fácilmente a Diseños y Listas de Reproducción usando una [Búsqueda en la Biblioteca](layouts_editor_library_search)
{/tip}

### Añadir Medios (Subir)

- Selecciona el botón **Añadir Medios**

  ![Upload Media](img/v4_media_library_upload.png)

- Haz clic en **Añadir archivos** y selecciona el(los) archivo(s) que deseas subir.

{tip}
Se pueden especificar umbrales y límites predeterminados que luego se consideran en el caso de que una [Imagen](media_module_image.html) deba redimensionarse al subir una imagen, por ejemplo. Se puede encontrar más información en **Configuración del CMS**.
{/tip}

- Dale a tu archivo un **Nombre** para una identificación más fácil en el CMS.

{tip}
¡Si el campo Nombre se deja en blanco, el archivo se nombrará según el nombre del archivo original al subir!
{/tip}

Sube archivos a una ubicación de Carpeta especificada para heredar las opciones de Ver, Editar, Eliminar Compartir que se han aplicado a la Carpeta de destino para un fácil acceso de Usuario/Grupo de Usuarios:

- Haz clic en el botón **Seleccionar Carpeta** y expande para seleccionar la Carpeta en la que guardar.

- Haz clic en la Carpeta a la que deseas subir el archivo y haz clic en **Listo**.
- La **Carpeta Actual** ahora mostrará la ruta del archivo seleccionado.

- Haz clic en el botón **Iniciar carga** para comenzar la carga de todos los archivos. Si se ha seleccionado una Carpeta y has añadido múltiples archivos, todos los archivos se subirán a esa ubicación.

Los archivos también se pueden subir individualmente y tener diferentes ubicaciones de Carpeta especificadas:

- En lugar de hacer clic en el botón Iniciar carga, haz clic en el botón **carga azul** que se muestra al final de la fila para un archivo añadido.

- Cambia la ubicación de la Carpeta usando el botón **Seleccionar Carpeta** como antes y luego haz clic en el botón azul al final de la fila para subir solo ese archivo singular.

![Single Upload](img/v4_media_library_single_upload.png)

- Una vez que todos los archivos se hayan subido con éxito, haz clic en **Listo**.

{tip}
Los archivos de medios también se pueden subir directamente a Diseños/Listas de Reproducción usando la herramienta de carga desde una Búsqueda en la Biblioteca. Los medios subidos a una Lista de Reproducción tienen una opción adicional para establecer [Fechas de Vencimiento de Widget](media_playlists.html#content-widget-expiry-dates).

Los archivos de medios que se suben y añaden directamente a Diseños/Listas de Reproducción también se guardan por defecto en la Biblioteca de Medios del CMS.
{/tip}

### Añadir Medios vía URL

- Selecciona el botón **Añadir Medios (URL)**:

![Upload via URL](img/v4_media_library_upload_url.png)

- Guarda en una Carpeta para heredar las opciones de Ver, Editar, Eliminar Compartir que se han aplicado a la Carpeta de destino para un fácil acceso de Usuario/Grupo de Usuarios.
- Proporciona la URL remota para el archivo.
- Dale a tu archivo un **Nombre** para una identificación más fácil en el CMS.

{tip}
¡Si el campo Nombre se deja en blanco, el archivo se nombrará según el nombre del archivo original!
{/tip}

- Haz clic en **Guardar**.

## Menú de Fila

Cada elemento en la **Biblioteca** tiene un menú de fila donde los Usuarios pueden acceder a una lista de acciones/atajos

## Editar

Selecciona **Editar** para hacer cambios en las ubicaciones de **Carpeta**, **Duraciones** y **Etiquetas** y otras configuraciones.

- Las configuraciones notables se enumeran a continuación:

### Fechas de Vencimiento

Establece una Fecha de Vencimiento para los Medios de la Biblioteca para eliminar el archivo de cualquier Diseño/Lista de Reproducción en el que se haya utilizado.

### Retirar Medios

Marcar **Retirar este Medio** mantendrá el archivo de medios asignado a cualquier Diseño/Lista de Reproducción existente pero no estará disponible para una selección adicional para añadir a Diseños/Listas de Reproducción.

### Habilitar Recolección de Estadísticas de Medios

- Establece la recolección de estadísticas de [Prueba de Reproducción](displays_metrics.html#proof_of_play) en Encendido / Apagado / Heredar para el archivo de medios seleccionado.

{tip}
¡Asegúrate de que **Habilitar Informes de Estadísticas** se haya marcado en Configuración de Pantalla para recopilar estadísticas de Prueba de Reproducción!
{/tip}

### Actualizar Medios

Usa la casilla de verificación **Actualizar este Medio en todos los Diseños a los que está asignado** para que cualquier edición se refleje en los Diseños/Listas de Reproducción a los que este archivo de medios está asignado actualmente.

{tip}
¡Las ediciones solo se actualizarán en Diseños/Listas de Reproducción que tengas acceso para editar!
{/tip}

### Reemplazar Medios

Puede ser necesario subir una nueva revisión de un archivo existente usando el botón **Reemplazar** en la parte inferior del formulario.

- Sube un archivo de reemplazo usando los mismos pasos que antes para [Añadir Medios (Subir).](media_library.html#content-add-media-upload)
- Marca para **Actualizar** el archivo de reemplazo a todos los Diseños/Listas de Reproducción a los que está asignado actualmente.
- Marca para **Eliminar** la versión anterior del archivo completamente del CMS.

## Eliminar

Los archivos de medios solo se pueden eliminar del CMS si **no** se están utilizando en ningún **Diseño/Lista de Reproducción** existente.

{version}
La opción para forzar una eliminación debe usarse con precaución ya que eliminar un archivo no se puede revertir.
{/version}

{tip}
[Retirar Contenido](media_library.html#content-retire-media) en lugar de eliminarlo mantendrá el archivo de medios en cualquier Diseño/Lista de Reproducción existente al que se haya asignado, con cualquier contenido programado no afectado. Los medios no estarán disponibles para añadir a nuevos Diseños/Listas de Reproducción.
{/tip}

{feat}Purge List|v4{/feat}

- Marca en la casilla para habilitar un empuje fuerte usando XMDS para eliminar completamente el archivo del almacenamiento local de un Reproductor.

### Informe de Uso

{tip}
¡Este informe es excelente para usar para hacer comprobaciones finales antes de limpiar archivos de medios!
{/tip}

Esto mostrará si el **archivo de medios** seleccionado está asignado/programado directamente a **Pantallas**.

![Library Usage Report](img/v4_media_library_usage_report.png)

- Usa la pestaña Diseño para ver en qué **Diseños** está incluido actualmente el archivo de medios.

### Programación

Los archivos de medios de Imagen y Vídeo de la Biblioteca se pueden Programar directamente a una Pantalla como contenido de pantalla completa desde el menú de fila.

- Haz clic en **Programación**

![Schedule Library Media](img/v4_media_library_schedule_fullscreen.png)

- Establece la **Duración** del elemento para determinar cuánto tiempo debe mostrarse este archivo de medios cada vez que aparece en la programación. Usa la duración, tal como se establece en la Biblioteca de Medios dejando este campo en blanco.
- Opcionalmente selecciona una **Resolución** para usar. Si se deja en blanco, se usará una resolución que coincida más en tamaño con el archivo de medios seleccionado.
- Se puede establecer un **Color de Fondo** opcional para llenar cualquier vacío si el medio no llena toda la pantalla.
- **Guardar**
- Completa el resto de los campos del formulario para completar la nueva Programación.

## Limpiar Biblioteca

A medida que se usa el CMS y se añaden Diseños/Listas de Reproducción y Medios, con el tiempo la Biblioteca puede llenarse de contenido antiguo que ya no está en uso.

La Biblioteca puede ser *limpiada* por un Usuario o Super Administrador para que se mantenga limpia y pequeña.
**Las acciones no se pueden revertir, por lo que esto debe usarse con precaución.**

{tip}
¡Esto podría ser particularmente útil si el CMS está instalado en un servidor web que tiene cuotas o si a los Usuarios se les han asignado sus propias cuotas!
{/tip}

Hay dos lugares donde se puede limpiar la Biblioteca:

1. Desde **Configuración del CMS** - disponible solo para todos los Super Administradores.
2. Desde la **Biblioteca** - para todos los Usuarios cuando **Habilitar Limpieza de Biblioteca** está marcado.

{nonwhite}
{cloud}
La función Limpiar Biblioteca está desactivada por defecto para clientes de **Xibo Cloud Hosting** ya que puede ser potencialmente destructiva si las opciones no se entienden completamente. Usa la casilla de verificación para habilitar si es necesario.
{/cloud}
{/nonwhite}

Una vez habilitado, los Usuarios pueden hacer clic en un botón **Limpiar Biblioteca** ubicado en la parte superior de la página de la Biblioteca:

![Tidy from Library](img/v4_media_library_tidylibrary.png)

El formulario mostrará el número de archivos que se eliminarán y cuánto espacio ocupan esos archivos.

{tip}
Esto solo eliminará archivos que son propiedad del Usuario conectado que ya no están en uso en un Diseño o Asignados a un Grupo de Pantallas/Pantalla.
{/tip}

#### Siguiente...

[Módulos y Conectores](media_modules.html)
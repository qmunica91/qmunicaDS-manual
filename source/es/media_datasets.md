---
toc: "media"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Diseña y almacena datos tabulares y úsalos con Widgets de datos para añadir a Diseños"
keywords: "conjunto de datos remoto, fuente json, fuente csv, columnas de conjunto de datos, filas de conjunto de datos, datos de conjunto de datos, ver rss"
---

# Conjuntos de Datos (DataSets)

Los Conjuntos de Datos se utilizan para diseñar y almacenar datos tabulares que se crean y gestionan independientemente de los [Diseños](layouts.html) y [Listas de Reproducción](media_playlists.html). Una vez creados, los Conjuntos de Datos se añaden a Diseños y Listas de Reproducción utilizando el Widget de [Conjunto de Datos](media_module_dataset.html).

Los Conjuntos de Datos también se pueden utilizar para crear tus propios [Feeds RSS](media_datasets.html#content-view-rss) para añadir al Widget [Ticker](media_module_ticker.html).

## Resumen de Características:

- Definir la estructura de datos.
- Los datos se pueden añadir manualmente.
- Importar datos desde un archivo CSV.
- Usar una fuente de datos formateada en JSON a través de la API.
- Sincronizar desde una fuente de datos de terceros de forma remota en un horario.
- Mantener contenido sin acceder a Diseños/Listas de Reproducción.
- Reutilizar a través de múltiples Widgets/Diseños/Listas de Reproducción.
- Crear un feed RSS desde un Conjunto de Datos.

Los Conjuntos de Datos han sido diseñados para ser versátiles de modo que puedan configurarse de varias maneras con el Widget de Conjunto de Datos así como una fuente de datos para un Módulo personalizado. Un Conjunto de Datos proporciona una forma conveniente de importar y mostrar datos de otros sistemas en [[PRODUCTNAME]].

Ejemplos de dónde podrían utilizarse los Conjuntos de Datos:

- Un menú de bebidas en un bar
- Horarios de salida en un club de golf
- Reservas de salas de reuniones
- Horarios de autobuses

Los Conjuntos de Datos se crean y gestionan independientemente de los Diseños y Listas de Reproducción y, por lo tanto, no requieren acceso de usuario a los Diseños, el Editor de Diseños o Listas de Reproducción para añadir o gestionar los datos contenidos dentro de un Conjunto de Datos.

![DataSet Flow](img/v4_media_dataset_flow.png)

## Creando un Conjunto de Datos

Los Conjuntos de Datos se crean y gestionan seleccionando **Conjuntos de Datos** bajo la sección **Biblioteca** del menú principal del CMS:

![DataSet Grid](img/v4_media_dataset_grid.png)

- Selecciona el botón **Añadir Conjunto de Datos** y completa los campos del formulario para crear un nuevo registro:

![DataSet Add](img/v4_media_dataset_add.png)

- Dale a tu Conjunto de Datos un **Nombre** para una identificación fácil en el CMS. Proporciona una **Descripción** interna opcional e ingresa un **Código** si haces referencia a este Conjunto de Datos a través de la API.

Si el Conjunto de Datos se va a conectar para sincronizar con una fuente de datos **Remota**, marca para habilitar y continuar con la configuración de [Creando Conjuntos de Datos Remotos](media_datasets.html#content-creating-remote-datasets).

Si el Conjunto de Datos **no es Remoto**, haz clic para Guardar el registro del Conjunto de Datos y continúa desde la sección [Crear y Configurar Columnas](media_datasets.html#content-create-and-configure-columns).

### Creando Conjuntos de Datos Remotos

Los Conjuntos de Datos Remotos son un tipo especial de Conjunto de Datos que se sincronizará periódicamente desde una fuente de datos de terceros. [[PRODUCTNAME]] llamará a la URL en un período de tiempo elegido y analizará los datos de acuerdo con las instrucciones establecidas en el registro del Conjunto de Datos y cualquier Columna que se haya definido como **Remota**.

Al seleccionar Remoto, se ponen a disposición campos con pestañas adicionales para que el registro del Conjunto de Datos Remoto se pueda completar completamente:

![Remote DataSet Options](img/v4_media_dataset_remote.png)

- #### Remoto

  Establece el tipo de método de solicitud e ingresa la URL para la fuente de datos remota.

- #### Autenticación

  Proporciona información de autenticación. Los Encabezados Personalizados están disponibles para proporcionar una cadena opcional de encabezados HTTP personalizados.

- #### Datos

  Establece la fuente de datos remota:

### Fuente JSON

Los datos JSON se pueblan de acuerdo con las Columnas definidas como tipos Remotos. Al especificar una **Columna Remota** se necesita ingresar una 'ruta de datos' que es la ruta de sintaxis JSON a los datos para esa columna, con respecto a la **Raíz de Datos** especificada.

{tip}
Considera una fuente de datos JSON de ejemplo:

```json
{
    "base": "EUR",
    "date": "2017-12-22",
    "rates": {
        "GBP": 0.88568,
        "THB": 38.83,
        "USD": 1.1853
    }
}
```

Si quisiéramos dos columnas para capturar el **Símbolo** y el **Valor** de la moneda, necesitaríamos establecer la **Raíz de Datos** en `rates` y tener Columnas para:

- **Símbolo** - ruta de datos = 0
- **Valor** - ruta de datos = 1

{/tip}

Usa la **URL de datos de prueba** para asegurar que se devuelva la estructura deseada.

### Fuente CSV

La fuente de datos remota se puede seleccionar como un CSV.

Si la fuente CSV contiene encabezados, marca para ignorar la primera fila.

Usa la **URL de datos de prueba** para asegurar que se devuelva la estructura deseada.

#### Avanzado

- Establece con qué frecuencia se deben obtener e importar los datos remotos.

{tip}
La tarea de obtener conjunto de datos remoto se ejecuta cada hora por defecto. Los Conjuntos de Datos Remotos están destinados a datos que se actualizan con poca frecuencia y no en tiempo real.
{/tip}

- Establece una escala de tiempo para Truncar datos.

- Usa el menú desplegable para seleccionar un Conjunto de Datos si usas dependientes.

- Opcionalmente establece un límite de filas y qué debe suceder si se excede este límite.

{nonwhite}

{noncloud}
Si no se establece un **Límite de Filas** aquí, se utilizará el Límite de Filas aplicado en la [Configuración del CMS](tour_cms_settings.html#content-defaults) para clientes no Cloud.
{/noncloud}

{cloud}
Si no se establece un **Límite de Filas** aquí, se aplicará el predeterminado que es 10,000 filas por Conjunto de Datos para clientes Cloud.
{/cloud}
{/nonwhite}

- Haz clic en **Guardar**.

## Crear y Configurar Columnas

Las Columnas definen la estructura de tus datos:

- Usa el menú de fila para un registro de Conjunto de Datos y selecciona **Ver Columnas**:

![DataSets Add columns](img/v4_media_datasets_add_columns.png)

{tip}
Por defecto, todos los nuevos Conjuntos de Datos tendrán una **Col1** añadida. ¡Esto debe editarse o eliminarse usando el menú de fila para Col1!
{/tip}

- Elimina Col1 desde el menú de fila y haz clic en el botón **Añadir Columna** para crear una nueva columna

o

- Usa el menú de fila para Col1 y selecciona **Editar**.

![DataSet Columns Form](img/v4_media_columns_form.png)

- Incluye un **Encabezado** para identificar esta Columna.
- Usa el menú desplegable para seleccionar un **Tipo** de Columna a usar.

### Tipos de Columna:

#### Valor

Ingresa una lista de elementos para presentar en un cuadro combinado.

- Usa el menú desplegable para seleccionar el **Tipo de Datos**.
- Proporciona una lista separada por comas de valores que se pueden seleccionar para esta columna.
- Establece la posición en que esta Columna debe aparecer al ver/editar Datos.
- Proporciona un mensaje de información sobre herramientas opcional para mostrar al ingresar datos para esta columna.

Usa las opciones adicionales para habilitar **Filtros**, **Ordenación** y **Valores Requeridos** para esta columna.

#### Fórmula

Ingresa una declaración MySQL.

- Usa el menú desplegable para seleccionar el Tipo de Datos.
- Establece la posición en que esta Columna debe aparecer al ver/editar Datos.
- Proporciona una declaración MySQL adecuada para usar en una declaración 'SELECT' o una cadena para formatear un campo de fecha.

{tip}
`	$dateFormat(<col>,<format>,<idioma>)`
	Asegúrate de que `<col>` tenga una fecha y hora especificadas para que funcione el formato de fecha. Si no se ha configurado el idioma, por defecto será Inglés.

Dos sustituciones están disponibles para columnas de Fórmula: `[DisplayId]` y `[DisplayGeoLocation]` que se sustituirán en tiempo de ejecución con el ID de Pantalla / Ubicación Geo de Pantalla (MySQL GEOMETRY).
{/tip}

Usa las opciones adicionales para habilitar **Filtros** y **Ordenación** para esta columna.

#### Remoto

Proporciona una cadena de sintaxis JSON.

- Usa el menú desplegable para seleccionar el Tipo de Datos.
- Ingresa una cadena de sintaxis JSON que muestre cómo acceder a los datos de una fuente de datos de terceros.
- Establece la posición en que esta Columna debe aparecer al ver/editar Datos.

Usa las opciones adicionales para habilitar **Filtros** y **Ordenación** para esta columna.

Continúa añadiendo y configurando Columnas según sea necesario. No hay límite teórico para el número de Columnas que [[PRODUCTNAME]] puede soportar, aunque un Conjunto de Datos más pequeño es a menudo más fácil de gestionar y mostrar.

{tip}
Las Columnas se pueden ver/añadir y editar usando el menú de fila para un registro de Conjunto de Datos desde la página de Conjuntos de Datos.

El orden y el contenido de la lista de Columnas se pueden cambiar después de que se hayan recopilado los Datos.
{/tip}

## Añadiendo Datos a las Columnas

Una vez que se han definido las Columnas, se deben añadir datos. Esto se puede lograr de varias maneras:

- Manualmente a través de la interfaz de usuario del CMS
- Importado a través de un archivo CSV
- Usando la API
- Sincronización Remota

### Manualmente

Los datos se añaden usando el botón **Ver Datos** en la página de Columnas.

{tip}
¡Los datos se pueden ver/añadir y editar usando el menú de fila para un registro de Conjunto de Datos desde la página de Conjuntos de Datos!
{/tip}

La tabla de datos mostrará cada una de las Columnas añadidas al Conjunto de Datos tal como se han configurado.

![Dataset Row](img/v4_media_dataset_row.png)

- Añade una nueva fila de datos haciendo clic en el botón **Añadir Fila** y completa para cada tipo de Columna no fórmula.
- Haz clic en **Siguiente** para continuar añadiendo datos para añadir más filas.
- Cuando se hayan completado todos los datos, haz clic en **Guardar**

{tip}
Haz clic en cualquier fila para Editar Datos. Haz clic en la cruz al final de una fila seleccionada para Eliminar.

Los Usuarios pueden cambiar a un **Modo de Selección Múltiple** usando el botón en la parte superior de la cuadrícula. En este modo, los Usuarios pueden seleccionar múltiples filas y hacer clic en **Eliminar Filas** para eliminar en bloque.

Una vez completo, haz clic en el botón **Modo de Edición** para salir del modo de selección múltiple.
{/tip}

### Importando un CSV

El CMS tiene un importador CSV de Conjunto de Datos que se puede usar para extraer datos de un **archivo CSV** y ponerlos en un Conjunto de Datos. La función **Importar CSV** se puede acceder a través del menú de fila de cualquier registro de Conjunto de Datos (con la excepción de Conjuntos de Datos configurados para fuentes de datos Remotas).

![Dataset Import CSV](img/v4_media_dataset_importcsv_form.png)

El importador tiene opciones para sobrescribir los datos existentes contenidos en el archivo de importación, así como una opción para ignorar la primera fila del CSV al importar si tu archivo tiene encabezados.

Las Columnas Remotas en el Conjunto de Datos se enumerarán con un campo junto a ellas para indicar el número de columna en el archivo CSV que corresponde con el Encabezado de Columna listado.

{tip}
Es importante asegurar que tu archivo CSV tenga la codificación de archivo correcta si estás usando caracteres no ASCII. Los caracteres no ASCII son muy comunes para idiomas fuera del inglés. La codificación de archivo más comúnmente utilizada es UTF-8.

Si has editado tu archivo CSV usando Excel, necesitarás asegurarte de seleccionar "Unicode (UTF-8)" desde Herramientas -> Opciones Web -> pestaña Codificación en el diálogo 'Guardar como'.
{/tip}

### A través de la API

Puedes escribir tu propia aplicación que sincronice datos en un Conjunto de Datos usando la API de [[PRODUCTNAME]]. Los datos se pueden añadir fila por fila o importando estructuras JSON completas.

{nonwhite}
Se puede ver más discusión sobre la API en la [documentación para Desarrolladores](/docs/developer).
{/nonwhite}

### Remotamente

Los Conjuntos de Datos Remotos se mantienen sincronizados con una Tarea llamada **Obtener Conjuntos de Datos Remotos**. Esta tarea está configurada por defecto y se ejecuta una vez por minuto.

- #### Dependientes

  Un Conjunto de Datos remoto puede depender de otro Conjunto de Datos para formular su solicitud. Cada fila en el Conjunto de Datos dependiente se utilizará para crear una solicitud utilizando los parámetros de solicitud del Conjunto de Datos principal.

## Menú de Fila

Cada Conjunto de Datos tiene un menú de fila donde los Usuarios pueden acceder a una lista de acciones/atajos.

- Las configuraciones notables se enumeran a continuación:

### Ver RSS

Crea tu propio feed RSS usando los datos contenidos en un Conjunto de Datos.

- Selecciona **Ver RSS** desde el menú de fila de un Conjunto de Datos.
- Haz clic en el botón **Añadir RSS**.

![Add RSS](img/v4_media_datasets_add_rss.png)

- Completa los campos del formulario, seleccionando las Columnas a usar.
- Al Guardar se generará una URL que se puede copiar y añadir al Widget [Ticker](media_module_ticker.html).

### Eliminar

Los Conjuntos de Datos solo se pueden eliminar si no están en uso.

Múltiples Conjuntos de Datos se pueden seleccionar y eliminar en bloque usando la opción Con Seleccionados en la parte inferior de la cuadrícula de Conjuntos de Datos.

### Compartir

Establece opciones de Compartir para acceso de Usuario/Grupo de Usuarios a Conjuntos de Datos individuales.

{nonwhite}
Echa un vistazo a nuestra guía para ver un ejemplo de cómo utilizar Conjuntos de Datos para tus Pantallas: [Usando Conjuntos de Datos para mostrar próximos cumpleaños](https://community.xibo.org.uk/t/using-datasets-to-show-upcoming-birthdays/31617)
{/nonwhite}

#### Siguiente...

[Widget de Conjunto de Datos](media_module_dataset.html)

---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
aliases:
  - "media_module_dataset_ticker"
  - "media_module_dataset_view"
excerpt: "Muestra información contenida en Conjuntos de Datos como Tickers o Tablas"
keywords: "ticker de conjunto de datos, vista de conjunto de datos, tablas de conjunto de datos, elementos de conjunto de datos, plantillas de conjunto de datos"
---

# Conjunto de Datos (DataSet)

Muestra datos contenidos en un Conjunto de Datos en cualquier lugar de un Diseño usando **Elementos** o incluye **Plantillas Estáticas** para mostrar Tickers y Tablas de datos en Diseños/Listas de Reproducción.

{feat}DataSets|v4{/feat}

El Widget de Conjunto de Datos consiste principalmente en una fuente de Conjunto de Datos que alimenta los Elementos configurados y las Plantillas Estáticas.

{tip}
Los [Conjuntos de Datos](media_datasets.html) deben crearse y definirse antes de añadir el Widget de Conjunto de Datos a Diseños/Listas de Reproducción.
{/tip}

## Elementos de Conjunto de Datos

Los [Elementos](layouts_editor#content-data-widgets-and-elements) están disponibles para selección al añadir un Widget de Conjunto de Datos a un [Diseño](layouts_editor.html) para dar a los Usuarios más control sobre qué componentes del Widget de Conjunto de Datos usar y dónde se pueden colocar.

![DataSet Elements](img/v4_media_module_dataset_elements.png)

{tip}
¡Verás un mensaje en el panel de propiedades si intentas usar un Elemento que no tiene un tipo de campo coincidente en tu Conjunto de Datos!
{/tip}

Cada Elemento tiene un conjunto de opciones de configuración en el Panel de Propiedades. Se debe seleccionar un Conjunto de Datos para usar como fuente de datos desde la pestaña **Configurar** para cada Elemento usado en el Diseño. Controla cómo los artículos deben ciclarse especificando una [Ranura de Datos](layouts_editor.html#content-data-slots) para usar para cada uno de los Elementos añadidos. Los Elementos de Datos pueden complementarse aún más añadiendo Elementos Globales para añadir formas y texto que se pueden poner en un Grupo de Elementos para una configuración y posicionamiento más fáciles.

## Plantillas Estáticas de Conjunto de Datos

Las Plantillas Estáticas definen cómo deben organizarse y estilizarse los datos devueltos y son una manera simple de mostrar tus datos usando plantillas preestilizadas.

![DataSet Templates](img/v4_media_module_dataset_templates.png)

Las Plantillas se pueden configurar para afectar el comportamiento de los resultados devueltos, así como hacer cambios en la apariencia del diseño usando una gama de opciones en el Panel de Propiedades. Se debe seleccionar un Conjunto de Datos para usar como fuente de datos desde la pestaña **Configurar** para cada Plantilla añadida al Diseño/Lista de Reproducción.

## Descripción General

- Actualiza Elementos y Plantillas con nuevos datos editando los datos subyacentes del [Conjunto de Datos](media_datasets.html#content-adding-data-to-columns).
- Actualiza el contenido del Widget de Conjunto de Datos sin acceder a Diseños o Listas de Reproducción.
- Ordena y Filtra resultados por cualquier columna.
- Mezcla elementos para reproducir en una secuencia aleatoria.
- El contenido para este medio es almacenado en caché por los Reproductores para reproducción fuera de línea.
- Establece una 'comprobación de frescura' para determinar cuándo cambiar al mensaje 'Sin datos' cuando un Reproductor está fuera de línea.

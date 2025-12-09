---
toc: "widgets"
maxHeadingLevel: 2
excerpt: "Usa el Widget Ticker RSS para mostrar contenido de feed dinámico"
keywords: "feeds dinámicos"
---

# Ticker RSS

Muestra contenido de feed dinámico en cualquier lugar de un Diseño usando Elementos o incluye Plantillas Estáticas con diseños preestilizados en Diseños/Listas de Reproducción.

{feat}Ticker|v4{/feat}

El Widget Ticker consiste principalmente en una ubicación de fuente de datos que alimenta los Elementos configurados y las Plantillas Estáticas.

## Elementos de Ticker

Los Elementos están disponibles para selección al añadir un Widget Ticker RSS a un [Diseño](layouts_editor.html) para dar a los Usuarios más control sobre qué componentes del Widget Ticker usar y dónde se pueden colocar.

![Ticker Elements](img/v4_media_module_ticker_elements.png)

Cada Elemento tiene un conjunto de opciones de configuración en el Panel de Propiedades. Se debe proporcionar una URL para ser usada como la fuente de datos desde la pestaña **Configurar** para cada Elemento usado en el Diseño. Controla cómo los artículos deben ciclarse especificando una Ranura de Datos para usar para cada uno de los Elementos añadidos. Los Elementos de Datos pueden complementarse aún más añadiendo Elementos Globales para añadir formas y texto que se pueden poner en un Grupo de Elementos para una configuración y posicionamiento más fáciles.

## Plantillas Estáticas de DataSet

Las Plantillas Estáticas definen cómo deben organizarse y estilizarse los elementos devueltos y son una manera simple de mostrar elementos usando plantillas preestilizadas.

![Ticker Templates](img/v4_media_module_ticker_templates.png)

Las Plantillas se pueden configurar para afectar el comportamiento de los resultados devueltos, así como hacer cambios en la apariencia del diseño usando una gama de opciones en el Panel de Propiedades. Se debe proporcionar una URL para ser usada como la fuente de datos desde la pestaña **Configurar** para cada Plantilla añadida al Diseño/Lista de Reproducción.

## Descripción General

- Define cuántos elementos deben mostrarse de un feed.
- La duración se puede establecer por elemento.

{tip}
Usa esta opción con precaución ya que esto puede crear elementos de medios de larga duración. ¡Asegúrate de usar en conjunto con **Número de elementos** para limitar!
{/tip}

- Selecciona comenzar con elementos desde el Inicio o Fin de la lista.

- Se puede seleccionar orden Inverso y Aleatorio de los elementos del feed.

- Incluye un aviso de Copyright para mostrar al final del feed.

- Devuelve resultados lado a lado.

- Proporciona una lista de atributos que no deben eliminarse del feed entrante.

- Incluye una lista de etiquetas HTML para ser eliminadas del feed.

- Establece un Agente de Usuario específico.

- Decodifica entidades HTML en el feed antes de analizarlo.

- Deshabilita el orden por fecha.

- Almacenado en caché para reproducción fuera de línea.

- Anula el Intervalo de Actualización para Imágenes.

{tip}
¡Crea tu propio [Feed RSS](media_datasets.html#content-view-rss) para usar con este Widget usando [Conjuntos de Datos](media_datasets.html)!
{/tip}

---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Muestra tipos de cambio para pares de divisas"
keywords: "api alpha vantage, conector alpha vantage, conversión inversa, moneda base"
---

# Monedas

Muestra tipos de cambio para pares de divisas en cualquier lugar de un Diseño usando **Elementos** o selecciona una **Plantilla Estática** para mostrar resultados en Diseños/Listas de Reproducción.

{feat}Currencies|v4{/feat}

El Widget de Monedas depende en parte de la [API de Alpha Vantage](https://www.alphavantage.co/) para recuperar datos de tipos de cambio que alimentan los Elementos configurados y las Plantillas Estáticas.

{tip}
Por favor visita [Alpha Vantage](https://www.alphavantage.co/support/#api-key) para crear una cuenta y obtener una clave API para ingresar en el [Conector de Alpha Vantage.](media_modules.html#content-connectors)
{/tip}

{nonwhite}
{cloud}
El Módulo de Monedas está configurado para clientes alojados en **Xibo Cloud** con una clave API proporcionada como parte del servicio.
{/cloud}
{/nonwhite}

## Elementos de Monedas

Los Elementos están disponibles para selección al añadir el Widget de Monedas a un [Diseño](layouts_editor.html) para dar a los Usuarios más control sobre qué componentes del Widget de Monedas usar y dónde se pueden colocar.

![Currencies Elements](img/v4_media_modules_currencies_elements.png)

Cada Elemento tiene un conjunto de opciones de configuración en el Panel de Propiedades. Ingresa **Monedas** usando sus siglas/abreviaturas que deseas mostrar así como una moneda **Base** desde la pestaña **Configurar**.

Controla cómo los artículos deben ciclarse especificando una [Ranura de Datos](layouts_editor.html#content-data-slots) para usar para cada uno de los Elementos añadidos. Los Elementos de Datos pueden complementarse aún más añadiendo Elementos Globales para añadir formas y texto que se pueden poner en un Grupo de Elementos para una configuración y posicionamiento más fáciles.

## Plantillas Estáticas de Monedas

Las Plantillas Estáticas definen cómo deben organizarse y estilizarse los datos devueltos y son una manera simple de mostrar tus datos usando plantillas preestilizadas.

![Currencies Templates](img/v4_media_modules_currencies_templates.png)

Las Plantillas se pueden configurar para hacer cambios en la apariencia del diseño usando una gama de opciones en el Panel de Propiedades. Ingresa **Monedas** usando sus siglas/abreviaturas que deseas mostrar así como una moneda **Base** desde la pestaña **Configurar** para cada Plantilla añadida al Diseño/Lista de Reproducción.

## Descripción General

- Conversión inversa para usar la moneda base como comparación.
- El contenido para este medio es almacenado en caché por los Reproductores para reproducción fuera de línea.
- La duración se puede aplicar por elemento o por página.

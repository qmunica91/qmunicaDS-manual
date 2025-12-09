---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Muestra información de precios de comercio para listados de acciones"
keywords: "api alpha vantage, conector alpha vantage"
---

# Acciones (Stocks)

Muestra información de precios de comercio para listados de acciones en cualquier lugar de un Diseño usando **Elementos** o selecciona una **Plantilla Estática** para mostrar resultados en Diseños/Listas de Reproducción.

{feat}Stocks|v4{/feat}

El Widget de Acciones depende en parte de la [API de Alpha Vantage](https://www.alphavantage.co/) para recuperar datos del mercado de valores que alimentan los Elementos configurados y las Plantillas Estáticas. Los precios devueltos por Alpha Vantage siguen el [estándar del mercado de valores](https://medium.com/@patrick.collins_58673/stock-api-landscape-5c6e054ee631) de ajuste por eventos corporativos como divisiones y pago de dividendos.

{tip}
Por favor visita [Alpha Vantage](https://www.alphavantage.co/support/#api-key) para crear una cuenta y obtener una clave API para ingresar en el [Conector de Alpha Vantage.](media_modules.html#content-connectors)
{/tip}

{nonwhite}
{cloud}
El Módulo de Monedas está configurado para clientes alojados en **Xibo Cloud** con una clave API proporcionada como parte del servicio.
{/cloud}
{/nonwhite}

## Elementos de Acciones

Los Elementos están disponibles para selección al añadir el Widget de Acciones a un [Diseño](layouts_editor.html) para dar a los Usuarios más control sobre qué componentes del Widget de Acciones usar y dónde se pueden colocar.

![Stocks Elements](img/v4_media_module_stocks_elements.png)

Cada Elemento tiene un conjunto de opciones de configuración en el Panel de Propiedades. Ingresa **Símbolos de Acciones** para devolver resultados desde la pestaña **Configurar**.

{tip}
Si necesitas un símbolo de acción que solo se cotiza en un intercambio específico, entonces puedes usar el formato `SÍMBOLO:INTERCAMBIO` para devolver resultados.
¡Los símbolos de acciones se pueden encontrar en varios sitios de búsqueda como [Yahoo Finance](https://finance.yahoo.com/)!
{/tip}

Controla cómo los artículos deben ciclarse especificando una Ranura de Datos para usar para cada uno de los Elementos añadidos. Los Elementos de Datos pueden complementarse aún más añadiendo Elementos Globales para añadir formas y texto que se pueden poner en un Grupo de Elementos para una configuración y posicionamiento más fáciles.

## Plantillas Estáticas de Acciones

Las Plantillas Estáticas definen cómo deben organizarse y estilizarse los resultados devueltos y son una manera simple de mostrar tus datos usando plantillas preestilizadas.

![Stocks Templates](img/v4_media_modules_stocks_templates.png)

Las Plantillas se pueden configurar para hacer cambios en la apariencia del diseño usando una gama de opciones en el Panel de Propiedades. Ingresa **Símbolos de Acciones** para devolver resultados desde la pestaña **Configurar** para cada Plantilla añadida al Diseño/Lista de Reproducción.

## Descripción General

- El contenido para este medio es almacenado en caché por los Reproductores para reproducción fuera de línea.
- La duración se puede aplicar por elemento o por página.

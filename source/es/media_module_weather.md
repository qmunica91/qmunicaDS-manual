---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Muestra pronósticos del tiempo diarios en Diseños y Listas de Reproducción"
keywords: "open weather map"
---

# Clima

Muestra datos de pronóstico del tiempo diarios en cualquier lugar de un Diseño usando **Elementos** o selecciona una **Plantilla Estática** para mostrar resultados en Diseños/Listas de Reproducción.

{feat}Weather|v4{/feat}

Los datos del tiempo son proporcionados por [OpenWeather](https://openweathermap.org/) que se proporciona bajo [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) y [ODbL](https://opendatacommons.org/licenses/odbl/) lo que proporciona pronósticos del tiempo diarios mundiales actuales que alimentan los Elementos configurados y las Plantillas Estáticas.

{tip}

Por favor asegúrate de estar usando un CMS v3.2.1 o posterior para tener en cuenta los cambios de API.

Visita [Open Weather Map](https://openweathermap.org/api) para crear una cuenta y obtener una clave API para ingresar en el [Conector de Open Weather.](media_modules.html#content-connectors)

**NOTA:** Desde el lanzamiento de One Call 3.0 de Open Weather, los nuevos usuarios deben ingresar detalles de tarjeta de crédito para usar la clave gratuita de x número de llamadas u optar por una suscripción paga.

Open Weather Map permite 1000 solicitudes de pronóstico, por día antes de cobrar una pequeña tarifa por cada solicitud posterior.

**Planes pagos** desbloquean un pronóstico de 16 días así como otras optimizaciones en la forma en que se extraen los datos.

{/tip}

{noncloud}
{version}
Los usuarios existentes que actualmente usan la API One Call 2.5 deben transferirse a la API One Call 3.0 para continuar usando este servicio. El acceso a One Call 2.5 ya no será posible después de junio de 2024. Se pueden encontrar más detalles sobre cómo transferir [aquí.](https://openweathermap.org/one-call-transfer)

Después de transferirse a una nueva clave, asegúrate de limpiar la caché para Clima usando el menú de fila desde la página **Módulos**.
{/version}
{/noncloud}

{nonwhite}
{cloud}
El Módulo de Clima está configurado para clientes alojados en **Xibo Cloud** con una clave API proporcionada como parte del servicio.
{/cloud}
{/nonwhite}

Los Términos de Servicio de Open Weather Map https://openweathermap.org/terms deben leerse y entenderse antes de usar este Widget.

## Elementos de Clima

Los Elementos están disponibles para selección al añadir el Widget de Clima a un [Diseño](layouts_editor.html) para dar a los Usuarios más control sobre qué componentes del Widget de Clima usar y dónde se pueden colocar.

![Weather Elements](img/v4_media_module_weather_elements.png)

Cada Elemento tiene un conjunto de opciones de configuración en el Panel de Propiedades. Ingresa la ubicación geográfica y unidades para devolver resultados desde la pestaña **Configurar**.

Controla cómo los artículos deben ciclarse especificando una Ranura de Datos para usar para cada uno de los Elementos añadidos. Los Elementos de Datos pueden complementarse aún más añadiendo Elementos Globales para añadir formas y texto que se pueden poner en un Grupo de Elementos para una configuración y posicionamiento más fáciles.

{tip}
Todos los Diseños que usan el Widget de Clima necesitan incluir atribución, disponible usando el Elemento de Atribución. Las Plantillas Estáticas contienen esta etiqueta por defecto.
{/tip}

## Plantillas Estáticas de Clima

Las Plantillas Estáticas definen cómo deben organizarse y estilizarse los resultados devueltos y son una manera simple de mostrar tus datos usando plantillas preestilizadas.

![Weather Templates](img/v4_media_modules_weather_templates.png)

Las Plantillas se pueden configurar para hacer cambios en la apariencia del diseño usando una gama de opciones en el Panel de Propiedades. Ingresa ubicaciones geográficas y unidades para devolver resultados desde la pestaña **Configurar** para cada Plantilla añadida al Diseño/Lista de Reproducción.

## Descripción General

- Devuelve resultados basados en la Ubicación de Pantalla.
- Establece automáticamente la unidad de medida a usar para basarse en la ubicación geográfica.
- Selecciona automáticamente pronósticos del tiempo basados en la Ubicación de Pantalla.
- Especifica qué Idioma usar.
- Opta por mostrar solo condiciones climáticas diurnas.
- Reemplaza Imágenes de Fondo con imágenes de la [Biblioteca](media_library.html)
- Los datos para este medio son almacenados en caché por los Reproductores para reproducción fuera de línea.

---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Muestra alertas meteorológicas en tiempo real"
keywords: "alertas meteorológicas de emergencia, formato de feed atom, url de feed atom personalizada, conector nws"
---

# Servicio Nacional de Meteorología

Ayuda a los ciudadanos de EE. UU. a prepararse para eventos climáticos extremos mostrando pronósticos del tiempo con datos en tiempo real sobre clima severo, agua y eventos climáticos. Aumenta la conciencia sobre peligros potenciales a través de tu red de Pantallas [[PRODUCTNAME]] usando datos del [Servicio Nacional de Meteorología (NWS)](https://www.weather.gov/).

![National_Weather_Alerts](img/media_module_national_weather_alerts_elements.png)

{version}
**NOTA:** Los pronósticos y advertencias meteorológicas son para los Estados Unidos, sus territorios y aguas adyacentes y áreas oceánicas. Si deseas utilizar este Widget, pide a tu Administrador que habilite el **Servicio Nacional de Meteorología** desde la sección **Módulos**.
{/version}

## Descripción General de Características

- El **Conector del Servicio Nacional de Meteorología** utiliza datos de la URL de feed Atom de NWS proporcionada.
- Se puede usar con la **URL predeterminada para el Feed Atom de NWS** o se puede proporcionar una URL de formato de Feed Atom personalizada.
- Añade de una variedad de **Elementos** para adaptar representaciones visuales en el Editor de Diseños para el máximo impacto.
- Usa filtros estándar de la industria para adaptar la mensajería de los datos devueltos.
- Muestra múltiples mensajes de alerta meteorológica con ciclado de datos del Feed Atom de NWS.
- Establece **Criterios** al **Programar** para determinar si la alerta meteorológica debe incluirse en el Bucle de Programación para Reproductores soportados.

{tip}
{nonwhite}
¡Al establecer el **Tipo de Criterio** en "Alerta de Emergencia" y la **Categoría** en "Met", te asegurarás de que los Diseños con Elementos NWS se añadan automáticamente al Bucle de Programación cada vez que ocurra una **Alerta de Emergencia** activa!
{/nonwhite}
{/tip}

## Soporte de Características del Reproductor

{feat}National Weather Service|v4{/feat}

## Lectura Adicional

[Gestión de Conectores](/media_modules_connectors)

[Widgets de Datos](/layouts_editor_data_widgets)

[Editor de Diseños](/layouts_editor)

{nonwhite}
[Criterios de Programación](/developer/player-control/schedule-criteria)
{/nonwhite}

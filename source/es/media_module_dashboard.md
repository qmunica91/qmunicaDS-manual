---
toc: "widgets"
minHeadingLevel: 2
excerpt: "Muestra Paneles que han sido configurados para usar el Servicio de Paneles de Xibo"
keywords: "servicio de paneles de xibo, power bi, grafana, matomo"
---

# Paneles (Dashboards)

{white}
**Ten en cuenta:** Si deseas aprovechar este Widget, por favor contacta a tu Administrador.
{/white}

{nonwhite}
El Widget de Paneles se utiliza para mostrar [Paneles](media_dashboard_service.html) que se han configurado para usar el [Servicio de Paneles de Xibo](/docs/setup/xibo-dashboard-service)

**Ten en cuenta:** Este Widget comercial es parte del **Servicio de Paneles de Xibo** y requiere una API para configuración como se explica más adelante [aquí](/pricing#dashboards)

{feat}Dashboards|v4{/feat}

## Configuración

- Selecciona el servicio de panel para que coincida con los paneles que se han configurado en el conector.
- Ingresa la URL para incrustar.

{tip}
Por favor mira la siguiente página para más información sobre cómo obtener una URL para usar con este servicio, mecanismos de autenticación y posibles limitaciones [Servicio de Paneles de Xibo](/docs/setup/xibo-dashboard-service)
{/tip}

- Proporciona un intervalo de actualización en minutos.

{version}
**NOTA:** El intervalo de actualización mínimo que se puede ingresar por panel es de 5 minutos ya que no admitimos actualizaciones del servicio de panel con más frecuencia que 5 minutos.
{/version}

Al ingresar por primera vez una URL en el Widget de Panel, puede tardar unos momentos en cargarse ya que depende de cuánto tiempo tarde en renderizarse el contenido de tu panel, y qué tan ocupado esté el servicio actualmente.

Una vez que estés mostrando tus paneles en pantallas, el servicio mantendrá tus paneles actualizados en el intervalo que especifiques para que siempre estén listos para mostrarse y aparezcan instantáneamente en las Pantallas.

Si dejas de mostrar un panel en tus pantallas por un tiempo, entonces el servicio dejará de actualizarlo, pero comenzará de nuevo automáticamente la próxima vez que se muestre ese panel.

{tip}

Por defecto, los informes en **Power BI** se renderizan con un formato de Fecha de EE. UU. Para usar un formato de fecha alternativo, añade los siguientes parámetros a la URL que pasas en el Widget de Paneles como se muestra con el ejemplo a continuación para `en-GB`:

`&language=en&formatLocale=en-GB`

{/tip}

**Ten en cuenta:** Si Xibo detecta un error con una solicitud de servicios de panel, verás un mensaje de banner rojo sobre la parte superior de una captura de pantalla para dar una indicación al usuario de dónde ha ocurrido el problema. Esto se mostrará en el previsualizador del Diseñador de Diseños solo para el usuario conectado. La Previsualización del Diseño y las Pantallas que muestran el Diseño programado continuarán mostrando la última captura buena o un icono de cargando hasta que se haya resuelto el problema.

Mensaje de Error de Ejemplo con captura de pantalla mostrada a continuación:

![Example Error Message](img/v4_media_modules_dashboard_error.png)

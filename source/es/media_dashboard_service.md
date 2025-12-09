---
toc: "media"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Característica comercial para mostrar de forma segura servicios de panel de control"
keywords: "conector, microsoft power bi, grafana, matomo"
---

# Servicio de Panel (Dashboard Service)

{white}
Si deseas aprovechar esta función, por favor contacta a tu Administrador.
{/white}

{nonwhite}
El Servicio de Paneles de Xibo es una característica comercial que permite a los Usuarios mostrar de forma segura servicios de panel; Microsoft Power BI, Grafana y Matomo, en Diseños con automatización y autenticación manejadas por Xibo.

**Ten en cuenta:** Esta característica comercial requiere una API para configuración como se explica más adelante [aquí](/pricing#dashboards).

Una vez que el Conector ha sido configurado, añade paneles para mostrar en Diseños usando el [Widget de Paneles](/manual/en/media_module_dashboard.html)

## Configurar Conector

Desde el CMS:

- Haz clic en **Aplicaciones** bajo la sección **Administración** del menú principal.
- Desplázate hacia abajo hasta la sección **Conectores** de la página.
- Haz clic en el botón **Configurar** para el conector **Xibo** **Dashboard Service**:

![Dashboard Connector](img/v4_media_dashboard_connector.png)

- Ingresa la clave API que se te ha dado (disponible en [Mi Cuenta](/login)).

{tip}
¡Los clientes en un Plan de Negocios o Empresarial tendrán su clave API prellenada!
{/tip}

- Marca para **Habilitar** para comenzar a proporcionar los servicios de panel

![Configure Connector](img/v4_media_dashboard_configure_connector.png)

- Haz clic en **Guardar.**

- Haz clic en el botón **Configurar** nuevamente para el conector de servicio de Panel de Xibo.
- Usando la sección **Credenciales** del formulario, selecciona el(los) servicio(s) de panel que deseas usar:

![Dashboard Credentials](img/v4_media_dashboard_credentials.png)

Ingresa las siguientes credenciales:

- Nombre de usuario
- Contraseña
- Secreto de Dos Factores (si es necesario)
- URL (si es necesario)

{tip}
Grafana no admite autenticación de múltiples factores, así que por favor deja el campo **Secreto de Dos Factores** **vacío** al configurar esta integración.

Por favor mira la siguiente página para más información sobre cómo obtener una URL para usar con este servicio, mecanismos de autenticación soportados y posibles limitaciones [Xibo Dashboard Service](/docs/setup/xibo-dashboard-service)
{/tip}

- Haz clic en **Guardar** y espera unos momentos mientras esas credenciales se registran exitosamente.

Tu Panel está listo para ser añadido a Diseños usando el [Widget de Panel](/manual/en/media_module_dashboard.html)
{/nonwhite}
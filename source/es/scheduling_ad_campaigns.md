---
toc: "scheduling"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Crea una Campaña Publicitaria con programación automática basada en criterios establecidos"
keywords: "costo por reproducción, impresiones por reproducción, prueba de reproducción"
---

# Campañas Publicitarias

Crea Campañas Publicitarias donde [[PRODUCTNAME]] calculará cuántas reproducciones se necesitan para satisfacer los criterios ingresados y gestionará la programación automáticamente por ti.

{tip}
¡Habilita la función **Acceso a Campañas Publicitarias** para cada Usuario/Grupo de Usuarios que deba tener acceso completo a esta función!
{/tip}

## Crear una Campaña Publicitaria

Haz clic en **Campañas** bajo la sección **Diseño** del menú principal del CMS:

- Haz clic en el botón **Añadir Campaña** en la parte superior de la cuadrícula.

- Selecciona **Campaña Publicitaria** desde el menú desplegable y completa los campos del formulario:

![Add Ad Campaign](img/v4_layouts_campaign_add_ad_campaign.png)

Las Carpetas se usan para organizar, buscar y Compartir objetos de Usuario fácilmente con otros Usuarios/Grupos de Usuarios. Las Campañas Publicitarias guardadas en una Carpeta heredarán las opciones de acceso aplicadas a esa Carpeta.

{tip}
¡Si los usuarios también deben tener acceso a los Diseños/Contenido de Diseño, asegúrate de que esto también se guarde en la misma Carpeta!
{/tip}

- Dale a tu Campaña Publicitaria un **Nombre** para una identificación fácil en el CMS incluyendo Etiquetas opcionales.

{tip}
¡Etiquetas y Carpetas también se pueden asignar a múltiples Campañas usando la opción **Con Seleccionados** en la parte inferior de la cuadrícula de Campañas!
{/tip}

- Usa el menú desplegable para establecer el **Tipo de Objetivo** para esta Campaña Publicitaria como **Reproducciones**, **Presupuesto** o **Impresiones**.
- Incluye el número **Objetivo** total para esta Campaña Publicitaria en relación con su Tipo de Objetivo seleccionado.

- Haz clic en **Guardar**.

A continuación, se deben establecer los criterios para permitir a [[PRODUCTNAME]] calcular la frecuencia de reproducción.

- Desde la cuadrícula, usa el menú de fila para la **Campaña Publicitaria** y selecciona **Editar**:

![Edit Ad Campaign](img/v4_campaigns_edit_ad_campaign.png)

- Proporciona Fechas y Horas de **Inicio** y **Fin** para la Campaña Publicitaria. (Esta información es requerida y **no puede** dejarse en blanco)
- Selecciona de las **Pantallas** y **Grupos de Pantallas** disponibles para reproducir esta Campaña Publicitaria. (Esta información es requerida y **no puede** dejarse en blanco)

{tip}
¡Asegúrate de que las Pantallas tengan los **Detalles de Pantalla** ingresados correctamente para las Pantallas seleccionadas que reproducen esta Campaña Publicitaria, asegurando que los campos **Costo por reproducción** e **Impresiones por reproducción** se hayan completado!
{/tip}

- Haz clic en **Guardar**.

{tip}
¡La **Prueba de Reproducción** necesita configurarse en **ON** para todas las Pantallas/Grupos de Pantallas seleccionados aquí, para asegurar informes precisos y reproducciones!
{/tip}

- Asigna un Diseño usando el menú desplegable **Añadir Diseño**.

Una vez que se selecciona un Diseño, hay más opciones de programación disponibles:

![Assign Layouts Ad Campaign](img/v4_campaigns_assign_layouts_ad_campaign.png)

- Selecciona qué **Días de la Semana** debe estar activo este Diseño en esta Campaña Publicitaria.

- Elige de [Particiones del Día](scheduling_dayparting.html) existentes si este Diseño solo debe mostrarse en momentos predefinidos seleccionados.

{tip}
Las Campañas Publicitarias pueden incluir múltiples instancias del mismo Diseño con diferentes Particiones del Día asignadas si es necesario.

Por ejemplo, si necesitas mostrar el mismo Diseño para una partición del día 'Mañana' definida así como una partición del día 'Noche' definida, ¡añade el Diseño dos veces y define las particiones del día requeridas individualmente para cada uno!
{/tip}

- Dibuja áreas en el mapa para proporcionar reproducciones basadas en **geo cercas** para cualquier pantalla móvil, con contenido para mostrar al entrar en un área definida.

{tip}
¡Puedes tener múltiples áreas definidas en el mismo mapa!
{/tip}

- Haz clic en **Guardar**.

El Diseño se añadirá a la Campaña que se puede editar/eliminar si es necesario usando el menú de fila:

![View Ad Campaigns](img/v4_campaigns_view_added_ad_campaigns.png)

Continúa construyendo tu Campaña Publicitaria seleccionando Diseños y definiendo opciones de programación.

{tip}
¡La **Prueba de Reproducción** necesita configurarse en **ON** para todos los Diseños añadidos a la Campaña Publicitaria para asegurar informes precisos y reproducciones!
{/tip}

[[PRODUCTNAME]] programará automáticamente para cumplir con los criterios de reproducción requeridos para alcanzar los Objetivos ingresados.

Las Campañas Publicitarias se pueden ver en la **Programación** como entradas bloqueadas que no se pueden editar desde el propio programador.

**Agenda** se puede usar para ver una vista de reproducción más detallada de la Campaña Publicitaria y previsualizar los Diseños incluidos.

El progreso de la Campaña Publicitaria se mostrará en la cuadrícula de Campañas y al abrir la Campaña Publicitaria, siempre que la Prueba de Reproducción se haya configurado en ON para todas las Pantallas y Diseños seleccionados para la Campaña. Así como los campos Costo por reproducción e Impresiones por reproducción completados para todas las Pantallas seleccionadas.

{version}
**NOTA**: Si se omite la información anterior, los informes no pueden actualizarse para reflejar Reproducciones, Gasto, Impresiones y Objetivo, los cuales mostrarán un valor de 0. La Campaña Publicitaria en sí también intentará ponerse al día para aumentar el Objetivo, lo que resultará en que los Diseños se reproduzcan cada vez con más frecuencia hasta que sea el único contenido mostrado para cumplir con el objetivo.
{/version}

![Ad Campaign Grid](img/v4_campaigns_ad_campaign_grid.png)

{tip}
La pestaña Referencia se puede usar para proporcionar información de referencia para la Campaña seleccionada. Una vez añadida, esta información se puede ver en la cuadrícula de Campañas y a través de la API.
{/tip}

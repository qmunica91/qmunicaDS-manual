---
toc: "layouts"
maxHeadingLevel: 3
minHeadingLevel: 2    
excerpt: "Usa Widgets de Datos para crear Diseños atractivos"
keywords: "widgets, widgets de datos, elementos, elementos de datos, elementos globales, grupos de elementos, plantillas, datos de respaldo, plantillas html, plantillas css, plantillas javascript, plantillas personalizadas"
---

# Widgets de Datos

Los Widgets de Datos dependen de una fuente de datos externa para mostrar información en los Diseños utilizando **Elementos**.

## Resumen de Características

- Contenido impulsado por fuente de datos.
- Elementos separados permiten flexibilidad.
- Proporcionar datos de respaldo para mostrar.
- Controlar la paginación de datos con Espacios de Datos.
- Crear Grupos para fácil duplicación.
- Extraer datos de una fuente alternativa en el mismo Diseño.
- Utilizar diseños prefabricados.

Cada Widget de Datos tiene un conjunto de **Elementos** que se alimentan de una fuente de datos que permite al Usuario flexibilidad en la colocación de los datos devueltos en lugar de estar obligados a un diseño rígido de **Plantilla Estática**:

- Haz clic en un **Widget de Datos** para mostrar todos los **Elementos** disponibles.

![Data Elements](img/v4_layouts_data_elements.png)

{version}
**NOTA:** Los Elementos de Datos solo están disponibles desde el Editor de Diseños y no están disponibles en el [Editor de Listas de Reproducción.](media_playlists.html#content-playlist-editor) Sin embargo, los Usuarios pueden añadir Widgets de Datos utilizando Plantillas Estáticas.
{/version}

### Configurar

Cada Elemento tiene un conjunto de opciones configurables disponibles desde el **Panel de Propiedades** una vez añadido:

![Element Properties](img/v4_layouts_element_properties.png)

{tip}
Se mostrará un icono de exclamación para avisar al Usuario sobre lo que necesita ser accionado. ¡El ejemplo anterior aún no tiene una URL ingresada para un feed ICS!
{/tip}

Las opciones establecidas desde la pestaña **Configurar** se aplicarán a todos los Elementos añadidos al Diseño del mismo tipo de Widget.

{tip}
¡Crea una [Nueva Configuración](layouts_data_widgets.html#content-new-configuration) para seleccionar datos de fuentes de datos alternativas asociadas con el Widget!
{/tip}

### Apariencia

La pestaña **Apariencia** incluye opciones para configurar cómo deben verse los datos devueltos por el Elemento e incluye efectos de transición y configuración de [Espacio de Datos](layouts_data_widgets.html#content-data-slots).

### Datos de Respaldo

Crea **Datos de Respaldo** para Widgets de Datos seleccionados y especifica bajo qué condiciones deben mostrarse:

![Fallback Data](img/v4_layouts_editor_data_widgets_fallback.png)

- Haz clic en **Añadir Nuevo**.
- Completa los campos del formulario con la información requerida.
- Guardar.

{tip}
¡Las opciones de Datos de Respaldo variarán dependiendo del Widget de Datos seleccionado!
{/tip}

### Avanzado

La pestaña Avanzado se usa para establecer Nombres, proporcionar duraciones específicas, establecer el nivel de colección de estadísticas de prueba de reproducción y habilitar elementos para repetirse para llenar todos los [Espacios de Datos](layouts_data_widgets.html#content-data-slots).

### Posicionamiento

Usa la pestaña **Posicionamiento** (icono de cuadrícula) para establecer un posicionamiento preciso y Capas.

{tip}
¡Los Elementos tienen su propia Capa de Lienzo, que se puede usar para determinar dónde aparecen en relación con otros Elementos renderizados nativamente como Listas de Reproducción y Vídeos!
{/tip}

## Espacios de Datos

Al añadir más de un mismo **Elemento**, maneja la paginación de los datos devueltos especificando un **Espacio de Datos** para usar por cada Elemento:

![Data Slots](img/v4_layouts_editor_data_slots.png)

{tip}
Por ejemplo, la imagen de arriba muestra que se han añadido 2 **Elementos de Descripción** del **Widget de Calendario**. Uno tiene un **Espacio de Datos de 1** y el otro un **Espacio de Datos de 2.** Si se devolvieran 10 elementos (Eventos de Calendario), el Espacio de Datos 1 mostraría los elementos 1,3,5,7,9 con el Espacio de Datos 2 mostrando los elementos 2,4,6,8,10.
{/tip}

Los Espacios de Datos se establecen desde la pestaña **Apariencia** del **Panel de Propiedades** para el Elemento seleccionado.

{tip}
¡Añadir más de un mismo Elemento aumentará automáticamente el número de **Espacio de Datos**!
{/tip}

Además, los Elementos tienen la opción de **Fijar este espacio** para que el primer elemento de datos que aparezca en ese espacio permanezca durante toda la duración del Widget y no cicle a través de los elementos de datos.

{tip}
¡Los Usuarios pueden establecer si **Repetir elementos** para llenar todos los espacios de datos para asegurar que no haya espacios vacíos usando la casilla de verificación en la pestaña **Avanzado** del Panel de Propiedades!
{/tip}

## Agrupando Elementos

Agrupa Elementos del mismo Widget de Datos juntos para facilitar la construcción de diseños:

- Añade Elementos al Diseño, posiciona y estiliza usando la pestaña **Apariencia**.
- Mantén presionada la tecla shift y haz clic en cada Elemento que desees agrupar.
- Una vez seleccionados, suelta la tecla shift y haz clic derecho.
- Selecciona **Agrupar elementos**.

![Grouping Elements](img/v4_layouts_grouping_elements.png)

{tip}
Los Grupos también pueden incluir **Elementos Globales**.
{/tip}

{version}
**NOTA:** ¡Todos los Elementos de Datos necesitan compartir el mismo **Espacio de Datos** y **Efecto** al agrupar!
{/version}

Los Grupos se pueden duplicar fácilmente:

- Haz clic derecho y selecciona **Duplicar**.

![Duplicated Elements](img/v4_layouts_duplicated_elements.png)

Edita **Espacios de Datos** para cada grupo para controlar la paginación de datos:

![Data Slots Groups](img/v4_layouts_data_slots_groups.png)

Haz ediciones a la **Apariencia** de cada Elemento en un grupo:

- Haz clic en el icono de lápiz en la esquina superior derecha.

- Haz clic en cada Elemento y usa la pestaña Apariencia para hacer cambios.
- Haz clic fuera del grupo o haz clic en la X para salir de la edición.

{tip}

Se pueden hacer ediciones a la **Configuración** pero se aplicará a todos los Elementos añadidos.

¡Desagrupa elementos desde el menú de clic derecho!
{/tip}

## Nuevas Configuraciones

Se pueden crear Nuevas Configuraciones para tener opciones de configuración alternativas/diferente fuente de datos asociada con el Widget:

- Haz clic derecho en un Elemento o Grupo de Elementos y selecciona **Nueva Configuración** desde el menú.
- Selecciona una fuente de datos alternativa / configuración alternativa desde la pestaña **Configurar**.

## Estarcidos (Stencils)

Los Widgets de Datos seleccionados incluyen diseños prefabricados de Grupos de Elementos llamados **Estarcidos** para ayudar a los Usuarios a crear contenido de manera simple y rápida:

- Los Estarcidos se añaden exactamente de la misma manera, posicionados y redimensionados.
- Completa los campos para **Configurar**.
- Edita la **Apariencia** haciendo clic en el icono de lápiz en la parte superior derecha del grupo.
- Selecciona un Elemento en el grupo para hacer ediciones.

{tip}
¡Haz clic derecho para desagrupar y personalizar aún más!
{/tip}

## Plantillas Estáticas

Las Plantillas Estáticas se incluyen para Widgets específicos. Las Plantillas pueden configurarse para afectar el comportamiento de los resultados devueltos, así como alterar las opciones de estilo.

{version}
Para uso avanzado, ¡se pueden crear **Plantillas de Módulo** para usar con Widgets de Datos usando HTML/CSS y JavaScript desde la sección **Desarrollador** del menú principal del CMS!
{/version}

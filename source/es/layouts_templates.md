---
toc: "layouts"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Acelera el proceso de diseño usando Plantillas"
keywords: "zonas, marcadores de posición, alterar plantilla, xibo exchange"
persona: "content creator, super administrator, user"
---

# Plantillas

Usa Plantillas para acelerar el proceso de diseño y asegurar que se mantenga un estándar corporativo.

## Resumen de Características:

- Usa diseños de Diseño publicados existentes para guardarlos fácilmente como Plantillas.
- Crea y gestiona Plantillas desde una página dedicada para una gestión más fácil.
- Añade Zonas a las Plantillas para que actúen como marcadores de posición de contenido en un Diseño.
- Establece opciones de Compartir para restringir el acceso del Usuario a zonas seleccionadas en una Plantilla.
- Muestra Plantillas Publicadas para selección en el Editor de Diseños.
- Acelera todo el proceso de diseño de Diseños para todos los Usuarios.
- Aplica una apariencia estandarizada a todos los Diseños.

Crea nuevas Plantillas o guarda tus diseños de Diseño existentes para usarlos como Plantillas para futuros Diseños.

{nonwhite}
Selecciona una de nuestras plantillas diseñadas desde el [Xibo Exchange.](layouts_editor_using_templates.html#content-xibo-exchange) haciendo clic en el botón debajo de Plantillas desde la Caja de Herramientas.
{/nonwhite}

{version}
Seleccionar una Plantilla reemplazará el diseño de Diseño actual con la Plantilla elegida. Esta acción es irreversible y debe usarse con precaución.
{/version}

## Crear Plantilla

Las Plantillas se crean seleccionando **Plantillas** bajo la sección **Diseño** del menú principal del CMS.

- Selecciona el botón **Añadir Plantilla** y completa los campos del formulario.

![Add Template Form](img/v4_layouts_add_template_form.png)

- Dale a tu Plantilla un **Nombre** para facilitar su identificación en el CMS.

- Selecciona la Resolución.

Al **Guardar**, el [Editor de Diseños](layouts_editor.html) se abrirá automáticamente con una **Zona** de tamaño completo.

Las Zonas se usan para definir áreas en un Diseño a las que se puede añadir contenido.

{tip}
Si no quieres incluir ninguna Zona y añadir contenido directamente a la Plantilla, elimina la Zona del lienzo haciendo clic derecho y seleccionando **Eliminar**. Añade contenido de la misma manera que creando un Diseño.
{/tip}

### Añadir Zonas

{tip}
¡Las Zonas solo están disponibles para su uso con Plantillas!
{/tip}

- Haz clic en cualquier lugar de la zona para redimensionar y posicionar:

![Template Layout Editor](img/v4_layouts_templates_editor.png)

{tip}
Usa los botones en la parte inferior derecha para seleccionar **Ajustar a la Cuadrícula**, **Ajustar a los Bordes** o **Ajustar a Elementos** para facilitar el posicionamiento al agregar elementos.
{/tip}

Las **Zonas** se pueden añadir desde la barra de herramientas:

- Haz clic en el botón superior **Widget**.

![Add Zone](img/v4_layouts_templates_add_zone.png)

- Selecciona la Zona y arrastra y suelta o haz clic para añadir.
- Redimensiona y Posiciona.

{tip}
Establece en **Bucle** solo si la Zona contiene un Widget que necesita actualizarse periódicamente (por ejemplo, RSS Ticker) y necesita actualizarse con más frecuencia que la duración del Diseño general.
{/tip}

### Capas

Desde el Panel de Propiedades, selecciona la pestaña Posicionamiento para establecer Capas para Zonas superpuestas / contenido añadido.

Añade tanto contenido desde la Caja de Herramientas como Zonas para construir tu diseño de Plantilla.

Una vez que tu Plantilla esté completa, usa el menú en la parte superior del editor para **Publicar**:

![Publish Template](img/v4_layouts_templates_publish.png)

Las **Plantillas** Publicadas se mostrarán para selección desde la Caja de Herramientas del Editor de Diseños.

## Guardar Diseño como Plantilla

Los Diseños Publicados se pueden guardar como una **Plantilla** desde dos ubicaciones:

- Desde el [Editor de Diseños](layouts_editor.html):
  - Después de **Publicar** vuelve al menú y selecciona **Guardar Plantilla**:

![Save Template Editor](img/v4_layouts_templates_save_as_template.png)

- Desde la cuadrícula de Diseños:
  - Usa el menú de fila para un Diseño **Publicado** y **selecciona Guardar Plantilla**.

Completa todos los campos relevantes del formulario para guardar el Diseño seleccionado como una Plantilla.

{tip}
¡Opcionalmente usa la casilla de verificación para incluir también todos los **Widgets** añadidos a la Plantilla!
{/tip}

- **Guardar**

{tip}
Los Diseños que se guardan como una Plantilla se pueden ver y editar desde la cuadrícula de **Plantillas** bajo la sección **Diseño** del menú principal del CMS.

¡**Etiquetar** un Diseño como una 'Plantilla' también añadirá tus diseños a tu lista de Plantillas!
{/tip}

## Menú de Fila

Todas las Plantillas tienen un menú de fila donde los Usuarios pueden acceder a una lista de acciones/atajos.

- Los ajustes notables se enumeran a continuación:

#### Alterar Plantilla

Selecciona para hacer cambios de diseño a la Plantilla en el Editor de Diseños.

#### Checkout

Para realizar ediciones en una Plantilla Publicada haz clic en **Checkout** y crea un borrador. Una vez editada la Plantilla se puede publicar para hacer permanentes los cambios sobrescribiendo la Plantilla existente. Descartar revertirá la Plantilla a su estado original publicado.

{tip}
Tómate tu tiempo con cualquier edición que necesites hacer, ya que usar **Checkout** asegura que no se realicen cambios en tu versión publicada ni se muestren en **Pantallas** programadas hasta que elijas hacerlo. **Publicar** confirma que se han realizado cambios y sobrescribirá tu versión publicada. **Descartar** eliminará el borrador permaneciendo la versión publicada intacta.
{/tip}

#### Publicar

Publicar asegurará que la Plantilla se muestre para selección desde la Caja de Herramientas.

#### Descartar

Descartar todos los cambios realizados en un borrador y revertir a la versión Publicada anterior.

#### Compartir

Establece opciones de Compartir para el acceso de Usuario/Grupo de Usuarios a Plantillas individuales.

#### Exportar

Exporta la Plantilla incluyendo todos los Widgets/Multimedia/Conjuntos de Datos asociados a un archivo ZIP, para que pueda compartirse fácilmente.

{tip}
Al exportar una Plantilla, se exportarán todas las **Etiquetas de Diseño**, **Lista de Reproducción** y **Etiquetas Multimedia** asignadas. Selecciona la opción **Importar Etiquetas** para añadir estas Etiquetas en la Importación de Diseño.

¡Usa la opción **Con Seleccionados** en la parte inferior de la cuadrícula de Plantillas para realizar acciones masivas para múltiples Plantillas!
{/tip}

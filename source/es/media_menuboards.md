---
toc: "media"
maxHeadingLevel: 3
minHeadingLevel: 2
alias: "media_module_menu_board"
excerpt: "Crea y Gestiona información de Tableros de Menú"
keywords: "categorías, productos, opciones de producto"
---

 # Tableros de Menú (Menu Boards)

La interfaz de Tableros de Menú proporciona una manera sencilla para que los usuarios creen y gestionen información de 'categorías' y 'productos' independientemente de los Diseños. Una vez creados, los datos del Tablero de Menú se pueden añadir en cualquier lugar de un Diseño usando Elementos de los Widgets [Tablero de Menú: Categoría](media_module_menuboards_category.html) y [Tablero de Menú: Productos](media_module_menuboards_products.html) disponibles en el [Editor de Diseños.](layouts_editor.html)

{version}
**Nota:** ¡Los Widgets de Tablero de Menú no están disponibles para añadir a una Lista de Reproducción!
{/version}

## Resumen de Características

- Crear y definir Categorías.
- Incluir información detallada del producto.
- Seleccionar Imágenes para usar desde tu Biblioteca.
- Mantener contenido sin acceder a Diseños.
- Reutilizar a través de múltiples Widgets/Diseños.

Los Tableros de Menú se crean y gestionan independientemente de los Diseños y, por lo tanto, no requieren acceso de usuario a Diseños o al Editor de Diseños para añadir o gestionar categorías/datos de productos contenidos en un Tablero de Menú.

## Creando un Tablero de Menú

Los Tableros de Menú se crean y gestionan seleccionando **Tableros de Menú** bajo la sección **Biblioteca** del menú principal del CMS:

![Menu Board](img/v4_media_menuboards_grid.png)

- Selecciona el botón **Añadir Tablero de Menú** y completa los campos del formulario para crear un nuevo registro:

![Menu Board Add](img/v4_media_menuboards_add.png)

- Dale a tu Tablero de Menú un **Nombre** para una identificación fácil en el CMS. Proporciona una **Descripción** interna opcional e ingresa un **Código** si haces referencia a este Tablero de Menú a través de la API.

- Haz clic en **Guardar**.

## Crear y Configurar Categorías

Las categorías definen la estructura de tus datos:

- Usa el menú de fila para un registro de Tablero de Menú y selecciona **Ver Categorías**.

![Menu Board row menu](img/v4_media_menuboards_row_menu.png)

Haz clic en el botón **Añadir Categoría** y completa los campos del formulario requeridos:

![Add Category](img/v4_media_menuboards_add_category.png)

{tip}
**Código** es para uso avanzado al hacer referencia a la API.
{/tip}

- Haz clic en **Siguiente** para repetir este proceso y añadir las **Categorías** requeridas para el Tablero de Menú.
- Selecciona **Guardar** al ingresar la última Categoría a usar.

## Añadir Productos

Los datos del producto se añaden a las Categorías para proporcionar toda la información clave que se puede seleccionar para mostrarse en Pantallas.

- Usa el menú de fila para una Categoría y selecciona **Ver Productos**:

![Products](img/v4_media_menuboards_products.png)

- Crea nuevos datos de Producto haciendo clic en el botón **Añadir Producto** y completa todos los campos del formulario relevantes:

![Add Products](img/v4_media_menuboards_add_product.png)

{tip}
¡El Widget [Tableros de Menú: Productos](media_module_menuboards_products.html) se puede configurar para atenuar productos que están marcados como no disponibles para mostrar en Pantallas!
{/tip}

### Opciones de Producto

Usa esta pestaña para proporcionar más opciones de producto:

![Product Options](img/v4_media_menuboards_product_options.png)

{tip}
Usa Opciones para proporcionar ofertas especiales, gangas limitadas, etc., para este producto en particular.
{/tip}

- Repite el proceso para añadir más Productos/Opciones de Producto a la Categoría.

{tip}
¡Cada Categoría se mostrará como una pestaña separada en la cuadrícula de Productos para que puedas cambiar fácilmente entre Categorías para añadir y editar información del producto!
{/tip}

![Product Tabs](img/v4_media_menuboards_product_tabs.png)

Haz clic en **Ver Categorías** para volver a la cuadrícula de Categorías para ver y editar las existentes usando el menú de fila o **Añadir Categoría**.

Los datos del Tablero de Menú se añaden a Diseños usando el Widget [Tablero de Menú: Categoría](media_module_menuboards_category.html) que tiene elementos de datos que se usan principalmente para añadir información de 'encabezado' y el Widget [Tablero de Menú: Productos](media_module_menuboards_products.html) que permite una colocación precisa de los detalles del Producto en Diseños.

{tip}
Los Tableros de Menú se editan independientemente de los Diseños, por lo que no hay necesidad de acceder o editar el(los) Diseño(s) a los que se ha añadido el Tablero de Menú. ¡Los cambios estarán disponibles en el sistema de inmediato listos para ser recogidos por los Reproductores en su próxima recolección, sin necesidad de hacer ninguna edición a los Diseños!
{/tip}

{nonwhite}
Echa un vistazo a nuestra guía para ver un ejemplo de cómo utilizar Tableros de Menú para tus Pantallas: [Usando Tableros de Menú](https://community.xibo.org.uk/t/utilising-menu-boards-in-v4/30749)
{/nonwhite}

#### Siguiente...

[Añadir Diseño](layouts_editor.html)

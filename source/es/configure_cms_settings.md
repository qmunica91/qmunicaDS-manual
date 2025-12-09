---
toc: "configure"
maxHeadingLevel: 3
minHeadingLevel: 2
alias: "tour_cms_settings"
excerpt: "Opciones configurables en los Ajustes del CMS para Administradores"
keywords: "redimensionar imágenes, predeterminados de transición, publicar diseño automáticamente, ajustes predeterminados de prueba de reproducción, biblioteca limpia, ajustes de mantenimiento, ajustes de red, ajustes regionales, establecer zona horaria, establecer idioma, política de contraseñas, recordatorio de contraseña, autenticación de dos factores, fuentes, aplicaciones, diseño predeterminado global"
---

# Ajustes de Administrador del CMS

{nonwhite}
Una vez que tu CMS esté instalado, se requiere alguna configuración adicional para habilitar toda la funcionalidad. Por favor consulta la siguiente guía: [Guía de Configuración Posterior a la Instalación del CMS](/docs/setup/xibo-cms-post-installation-setup-guide.html)
{/nonwhite}

Como cualquier aplicación compleja, el CMS de [[PRODUCTNAME]] viene con un número de opciones configurables. Estas se encuentran en la página **Ajustes** bajo la sección **Administración** del menú principal del CMS.

{nonwhite}
{cloud}
Los clientes alojados en **Xibo Cloud** tendrán algunos de estos campos pre-poblados como parte del servicio. Algunos pueden cambiarse y otros están bloqueados para deshabilitar la edición. Para más información, por favor consulta esta página: [Predeterminados y Restricciones del CMS de Xibo Cloud](/docs/setup/xibo-in-the-cloud.html#content-xibo-cloud-cms-defaults-and-restrictions).
{/cloud}
{/nonwhite}

Los ajustes se dividen en pestañas de categorías relacionadas:

![CMS Settings](img/v4_tour_cms_settings_admin.png)

## Configuración

Desde esta pestaña visualiza la **Clave Secreta del CMS** que se usa para autenticar Reproductores con el CMS y aplica un **Tema** a las páginas (si aplica) así como configurar el posicionamiento predeterminado para el [Menú de Navegación](tour_cms_navigation.html).

## Predeterminados

Usa esta pestaña para aplicar valores predeterminados a todos los archivos de [Medios](media_library.html) y establecer [Transiciones](configure_transitions.html) predeterminadas.

También puedes configurar Diseños para **Publicar automáticamente** 30 minutos después de la última edición registrada habilitando la casilla de verificación para este ajuste.

### Redimensionar Imágenes

Se pueden especificar umbrales y límites predeterminados que luego se consideran en el caso de que una imagen deba redimensionarse. Esto podría ser al subir una imagen o al descargar una imagen por un Widget - NASA RSS en un Widget Ticker por ejemplo.

- #### Umbral de Redimensionamiento

Establece un umbral máximo (basado en el lado más largo) que debe considerarse para redimensionar una imagen.

{tip}
Si estableces un Umbral de Redimensionamiento de 1920 y subes/descargas una imagen que es 800, esta imagen no necesitaría redimensionarse. Si subiste/descargaste una imagen que era 2400, esta se redimensionaría a 1920.
{/tip}

- #### Límite de Redimensionamiento

Establece un límite (basado en el lado más largo) para imágenes subidas/descargadas. Las imágenes que excedan este límite no se procesarán y deben reemplazarse con otra imagen que esté dentro del límite.

Este ajuste determinará si el archivo de imagen es demasiado grande para ser procesado.

- #### Número máximo de Filas de Conjunto de Datos

Establece el número máximo permitido de filas que un Usuario puede crear en un Conjunto de Datos.

{nonwhite}
{cloud}
El valor predeterminado para clientes de Cloud se establece en 10,000 filas por Conjunto de Datos.
{/cloud}
{/nonwhite}

## **Pantallas**

Establece valores predeterminados para **Latitud** y **Longitud** para todas las vistas previas conscientes de Geo en todo el CMS.

### Diseño Predeterminado

El Diseño Predeterminado establecido aquí se asignará automáticamente a todas las Pantallas para mostrarse cuando no haya otro contenido programado o si hay un problema que impida que se muestre un Evento programado.

{nonwhite}
{tip}
Puedes crear tu propio Diseño para reemplazar el predeterminado preestablecido, pero ten en cuenta que los diseños deben mantenerse simples sin contenido multimedia o web complejo.
{/tip}
{/nonwhite}

Este Diseño Predeterminado global puede anularse para Pantallas individuales seleccionando un [Diseño Predeterminado](displays.html#content-default-layout) alternativo para usar.

### Ajustes Predeterminados de Prueba de Reproducción

Establece el **Nivel de agregación** de la recopilación de estadísticas de [Prueba de Reproducción](displays_metrics.html) para aplicar a todos los **Diseños** / **Medios** y **elementos de Widget** por defecto.

- **Individual** - las estadísticas se registran al inicio y al final de cada elemento individualmente y se envían de vuelta al CMS en cada intervalo de recopilación.
- **Horario** - registra cada elemento una vez, e incluye el número total de veces reproducido y la duración del tiempo reproducido durante la hora y se envía de vuelta al CMS en el siguiente intervalo de recopilación después de que el período de hora haya expirado.
- **Diario** - registra cada elemento una vez, e incluye el número total de veces reproducido y la duración del tiempo reproducido durante el día y se envía de vuelta al CMS en el siguiente intervalo de recopilación después de que el día haya expirado.

{tip}
¡Los Reproductores agregan solo 'registros completados', con la recopilación hecha al final de la duración de los Widgets, así que si un Widget tiene una duración de 3 horas, la estadística se registrará una vez que el Widget haya expirado!
{/tip}

- Usa esta casilla para **habilitar la recopilación** de estadísticas de Prueba de Reproducción a todas las **Pantallas** por defecto.

{tip}
Esto se puede alternar encendido/apagado editando [Perfiles de Configuración de Pantalla](displays_settings.html#content-editing-profiles).
{/tip}

- Marca la casilla para establecer el valor predeterminado en encendido para la recopilación de estadísticas de Prueba de Reproducción para todos los **Diseños** recién agregados.

{tip}
La recopilación se puede deshabilitar desmarcando la casilla en el formulario **Añadir/Editar** Diseño.
{/tip}

Usa los ajustes para habilitar la recopilación de estadísticas de Prueba de Reproducción para aplicar a todos los **Medios**, **Listas de Reproducción** y **Widgets** (Apagado/Encendido/Heredar).

{tip}
¡Se pretende que **Widget** siempre esté establecido en Heredar para que las opciones de Diseño y Medios controlen la recopilación!
{/tip}

## General

Ve/establece la dirección para el **Manual de Usuario** y marca para enviar **estadísticas anónimas** para ayudar a mejorar el software.

### Limpieza de Biblioteca (Global)

La Biblioteca puede ser *limpiada* por un Super Administrador o Usuario para que se mantenga limpia y pequeña.
**Las acciones no pueden revertirse, por lo que esto debe usarse con precaución.**

{tip}
Esto podría ser de particular interés si el CMS está instalado en un servidor web que tiene cuotas o si a los Usuarios se les han asignado sus propias cuotas.
{/tip}

Los Administradores pueden iniciar una operación de limpieza de Biblioteca en todo el sistema haciendo clic en el botón **Limpiar Biblioteca** en la esquina derecha de la página de Ajustes:

![Settings Tidy Library](img/v4_tour_cms_settings_tidy_library.png)

Como esta funcionalidad es en todo el sistema y por lo tanto opera en **TODOS** los archivos de Usuario, se requiere confirmación para eliminar revisiones no utilizadas y antiguas.

Esta opción es más completa y elimina:

- Archivos temporales
- Archivos huérfanos
- Miniaturas
- Revisiones de medios que no se usan en ninguna parte
- Medios que no se usan en ninguna parte (en ningún Diseño / Grupo de Pantallas / Pantallas)
- Archivos genéricos subidos al CMS

#### Archivos huérfanos

Los archivos huérfanos son una ocurrencia rara donde un archivo almacenado en disco en la carpeta de la Biblioteca no se elimina cuando el elemento de Medios se elimina de la Biblioteca. Esto significa que el archivo existe pero el CMS no sabe nada al respecto.

### Limpieza desde Biblioteca de Usuario

{nonwhite}
{cloud}
La función de Limpiar Biblioteca está desactivada por defecto para clientes de **Xibo Cloud Hosting** ya que puede ser potencialmente destructiva si las opciones no se entienden completamente.
{/cloud}
{/nonwhite}

Permite a un Usuario limpiar archivos desde la página de [Biblioteca](media_library.html#content-tidy-library) usando la casilla de verificación para **Habilitar Limpieza de Biblioteca**.

## Mantenimiento

Desde aquí **Habilitar Mantenimiento** y **Alertas de Correo Electrónico** para ser enviadas y establecer las edades máximas de retención para **Registros** y **Estadísticas**.

## Red

Desde la pestaña Red completa una **dirección de correo electrónico de Admin** para el administrador general del CMS. Todas las notificaciones de correo electrónico generadas por el CMS se enviarán a esta dirección.

Asegúrate de que la **dirección de correo electrónico de envío** y el **nombre** estén completos antes de configurar cualquier notificación de correo electrónico adicional en todo el CMS.

{nonwhite}
{noncloud}
También puedes proporcionar información del Servidor Proxy (si tu CMS está detrás de un proxy) forzar **HTTPS** y establecer límites mensuales de **Ancho de Banda** y tamaño de **Biblioteca**.
{/noncloud}
{/nonwhite}

## Compartir

Usa el menú desplegable para cambiar cómo aparece el color del Widget en las Listas de Reproducción para los Usuarios.

- **Coloreado de Medios** usará los colores del **tema** para cada Widget.
- **Coloreado de Compartir** mostrará el color del Widget basado en el **acceso de Usuario** desde las opciones de **Compartir**. (Verde = editable)

Desde aquí puedes establecer si los Usuarios deben tener la capacidad de programar a Pantallas cuando las opciones de Compartir están establecidas en Ver para el Usuario, así como poder establecer si los Usuarios deben poder ver los nombres de los Diseños en programaciones que no se han compartido con ellos.

Marca para permitir a los Usuarios guardar su contenido en la [Carpeta Raíz](configure_folders.html) de nivel superior o deshabilita para forzar a los Usuarios a seleccionar una Carpeta para guardar.

## Regional

Desde esta pestaña establece el **Idioma** y la **Zona Horaria** predeterminada y el **Formato de Fecha** para usar en todo el CMS.

{tip}
¡Selecciona la ciudad principal más cercana en tu zona horaria!
{/tip}

Usa la casilla de verificación para detectar el **idioma del navegador** para usar en el CMS y selecciona qué tipo de **Calendario** debe usarse.

## Resolución de Problemas

Esta pestaña se usa para establecer Niveles de Registro que son útiles para capturar errores de php y problemas de entorno.

## Usuarios

Selecciona el Usuario del Sistema y establece el Grupo de Usuarios Predeterminado y el Tipo de Usuario al incorporar nuevos Usuarios.

{tip}
¡Recomendamos que el **Tipo de Usuario Predeterminado** se establezca en **Usuario**!
{/tip}

### Política de Contraseñas

Ingresa cualquier expresión regular válida en el campo **Expresión Regular de Política de Contraseñas** para que todas las solicitudes de cambio de contraseña y contraseñas recién creadas se prueben contra esto.

{tip}
¡Se mostrará una descripción de texto a los Usuarios cuando sus contraseñas no cumplan con la política requerida como aviso!
{/tip}

{nonwhite}
{cloud}
Los clientes con [Xibo Cloud Hosting](/hosting) tienen una **política predeterminada establecida** que requiere una contraseña de al menos 10 caracteres.
{/cloud}
{/nonwhite}

### Recordatorio de Contraseña

Habilita para proporcionar un enlace de restablecimiento de **¿Olvidaste tu Contraseña?** para **Usuarios** al iniciar sesión para que puedan recuperar fácilmente el acceso al CMS.

{tip}
¡Asegúrate de que se haya ingresado una **dirección de correo electrónico de envío** válida en la pestaña **Red** antes de habilitar esta funcionalidad!
{/tip}

Se mostrará al Usuario un enlace que, una vez clicado, enviará una **Notificación de Restablecimiento de Contraseña** a su dirección de correo electrónico según consta en su Perfil de Usuario.

{tip}
Los **Usuarios** también pueden cambiar sus propias contraseñas, una vez que hayan iniciado sesión en el CMS, desde su **Perfil de Usuario**.
{/tip}

## Autenticación de Dos Factores

[Autenticación de Dos Factores](index.html) puede ser configurada por un Usuario para mayor seguridad una vez que haya iniciado sesión.

Una vez configurada, un Usuario necesitaría ingresar el código enviado por correo electrónico o como se muestra en la aplicación Google Authenticator para completar el inicio de sesión para obtener acceso al CMS.

{tip}
¡Asegúrate de que el usuario haya proporcionado una dirección de correo electrónico para recibir el correo electrónico generado!
{/tip}

Establece una **dirección de correo electrónico de envío** válida en la pestaña **Red** y se ha ingresado un nombre en el campo **Emisor de Dos Factores** para que quede claro en la aplicación Google Authenticator y el correo electrónico cuando se generen códigos autenticados para iniciar sesión en el CMS.

Restablece la Autenticación de Dos Factores para Usuarios desde su Perfil de Usuario.

## Aplicaciones

[[PRODUCTNAME]] contiene una API que permite a aplicaciones de terceros conectarse y consumir sus datos.

Las aplicaciones se añaden y configuran desde **Aplicaciones** bajo la sección **Administración** del menú principal del CMS.

{tip}
Antes de usar una Aplicación, cada Usuario debe autorizar la aplicación para actuar en su nombre dentro del CMS.
Los Usuarios pueden ver Aplicaciones autorizadas desde la sección Mis Aplicaciones de su **Perfil de Usuario**.
{/tip}

En este momento, el CMS no proporciona a los Usuarios individuales un método para revocar el acceso a una aplicación. Solo un Administrador puede eliminar una aplicación completamente.

## Fuentes

[[PRODUCTNAME]] viene con un conjunto de fuentes estándar que se pueden configurar en muchos Widgets:

- Aileron Heavy Regular (Aileron-Heavy.otf)
- Aileron Regular (Aileron-Regular.otf)
- Dancing Script Regular (DancingScript-Regular.ttf)
- Railway Regular (Railway.ttf)
- Linear Regular (linear-by-braydon-fuller.otf)

{version}
**IMPORTANTE:** es posible establecer una fuente personalizada en muchos Widgets, ya sea a través de una propiedad llamada **Familia de Fuentes** o a través de la lista de selección de **Fuente** del editor visual. Si no se elige una fuente, el Reproductor mostrará su propia fuente predeterminada "sans-serif", referida como la fuente del sistema. Ej. en Android esto es usualmente Roboto.

Recomendamos siempre elegir una fuente donde esté disponible para evitar que los Reproductores muestren fuentes diferentes.{/version}

Gestiona desde la página **Fuentes** bajo la sección **Administración** del menú principal del CMS.

- Usa el menú de fila para ver los **Detalles** de una Fuente y ver un ejemplo del estilo de fuente:

![Font Details](img/v4_tour_settings_fonts.png)

Se pueden añadir fuentes adicionales haciendo clic en el botón **Subir Fuente** y usando la herramienta de carga de archivos.

{tip}
Si la nueva fuente no se muestra en el editor de texto después de subirla, ¡intenta limpiar la caché del navegador!
{/tip}

{version}
**NOTA:** Las fuentes tienen preferencias integradas en ellas conocidas como **etiquetas OS/2**. [[PRODUCTNAME]] busca preferencias OS/2 y puede usar **fuentes con etiquetas OS/2 0 o 8**.

Las fuentes con otras etiquetas OS/2 pueden producir un error al subir y pueden no mostrarse correctamente.
{/version}

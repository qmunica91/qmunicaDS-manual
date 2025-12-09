---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 1
alias: "media_module_chart"
excerpt: "Gestión de Módulos para Administradores"
keywords: "archivo genérico, almacenamiento en caché, acceso externo, habilitar módulos, deshabilitar módulos"
---

# Gestión de Módulos

Todo el contenido mostrado en [[PRODUCTNAME]] es servido por un **Módulo de Medios** gestionado desde la página **Módulos** bajo la sección **Administración** del menú principal del CMS:

![Modules Grid](img/v4_media_modules_grid.png)

- Usa el menú de fila y haz clic en **Configurar** para controlar si debe ser accesible para que los Usuarios lo usen.

{tip}
A veces puede ser necesario añadir o eliminar las extensiones permitidas en un Módulo basado en archivo de Biblioteca particular (Imagen, Vídeo, Flash, etc.). Un caso de uso típico sería si se está utilizando un Reproductor que no admite ese tipo particular de archivo.

Las fuentes se pueden añadir y gestionar desde la página [Fuentes](tour_cms_settings.html#content-fonts) bajo la sección **Administración** del menú principal del CMS.
{/tip}

## Almacenamiento en caché y acceso externo

Los Módulos principales están diseñados para tener sus datos almacenados en caché y servidos desde el CMS para que puedan reproducirse sin una conexión activa y/o sin acceso directo a recursos externos que puedan ser necesarios. El CMS también utiliza este mecanismo para ser un _buen ciudadano_ al solicitar datos de terceros.

{tip}
Por ejemplo, un Widget Ticker con la dirección `http://anexternal.com/feed` solo sería accedido por el CMS y solo una vez por `updateInterval`. Los Reproductores que muestran el Diseño no necesitarían acceder a esa dirección directamente.
{/tip}

Todos los Módulos principales adoptan este enfoque, excepciones señaladas a continuación:

- El **Módulo de Página Web** no almacena en caché desde el CMS y siempre intentará abrir la dirección de página web especificada usando el navegador en el Reproductor. Esto significa que el Reproductor debe tener acceso a la red a la dirección web en todo momento.
- El **Módulo Incrustado** se puede almacenar en caché usando referencias de biblioteca, sin embargo, el Usuario que crea el Módulo es libre de especificar recursos externos si los requiere.
- El **Módulo de Vídeo Local** es renderizado por el decodificador de vídeo en el Reproductor y puede hacer referencia a una transmisión externa.
- Los Archivos **Flash** tienen la capacidad de hacer referencia a un archivo externo y se ejecutarán en el Reproductor.

## Archivo Genérico

El Módulo de Archivo Genérico se utiliza para enviar **archivos adicionales** al Reproductor que luego se pueden utilizar para otros fines.

{tip}
Esto podría ser útil para proporcionar archivos suplementarios para ser utilizados como rutas relativas (por ejemplo, una flecha hacia arriba y hacia abajo que se muestra dinámicamente en el HTML incrustado basado en los resultados de los datos de acciones) como ejemplo.
{/tip}

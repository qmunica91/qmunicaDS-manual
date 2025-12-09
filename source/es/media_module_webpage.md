---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Muestra contenido de Página Web añadiendo el Widget de Página Web a los Diseños"
keywords: "abrir nativamente, posición manual, mejor ajuste, precarga, error de carga de página web"
---

# Página Web

Incluye contenido de una página web para ser mostrado en Diseños y Listas de Reproducción.

{feat}Webpage|v4{/feat}

{version}
**Nota:** El Widget de Página Web requiere una conexión a internet válida para funcionar ya que las páginas web no son almacenadas en caché por el Reproductor.
{/version}

## Descripción General

- Ve una página web completa sin alteraciones.
- Opciones de incrustación Abrir Nativamente, Posición Manual y Mejor Ajuste.
- Escala y desplaza la página web objetivo para mostrar una sección particular de la página web.
- Para contenido con un fondo transparente marca para mostrar el Widget con un fondo transparente.
- Precarga contenido fuera de pantalla.
- Dispara un web hook para navegar a una [acción](layouts_interactive_actions.html) activa en el caso de un error de carga de página web.

{version}

**NOTA:**

- Fondo transparente está disponible en Windows desde v2 R253. [[PRODUCTNAME]] hará su mejor esfuerzo para hacer esto cuando esté habilitado para páginas que tienen un fondo transparente, sin embargo, no puede ser soportado en algunas páginas web.
- Precarga fuera de pantalla está actualmente solo disponible desde Android v2 R207.

{/version}

### Abrir Nativamente

Cuando se selecciona, el Reproductor abrirá la página web sin ninguna alteración y abrirá y renderizará en el navegador como si la URL hubiera sido visitada en el dispositivo fuera de [[PRODUCTNAME]].

{tip}
**Por favor ten en cuenta:** ¡No hay previsualización disponible con esta opción!
{/tip}

### Disparar un web hook

Dispara un web hook para una acción activa (navegar a Widget, navegar a Diseño un Comando Programado, etc.) para ser mostrada en el caso de que la página web devuelva un error y falle al cargar.

{feat}Webpage - Page load error trigger|v4{/feat}

- Ingresa el **Código de Disparador** de una Acción configurada para coincidir con un parámetro `trigger` de web hook suministrado.

### Posición Manual

Esta opción incrustará la página web en un iframe donde los usuarios pueden especificar las dimensiones requeridas.

- Usa las configuraciones de Desplazamiento y Escala para forzar que la página/secciones de la página ajusten dentro de las dimensiones para mostrar solo una sección de la página web.

### Mejor Ajuste

Esta opción incrustará la página web en un iframe donde los usuarios pueden especificar las dimensiones requeridas.

{version}
**NOTA:** Las opciones **Posición Manual** y **Mejor Ajuste** no funcionarán con sitios web que establecen el **encabezado X-Frame-Options**. Si no puedes ver la página web usa la opción Abrir Nativamente cuando uses Windows / Linux o Android.

¡Si X-Frame-Options están establecidos entonces webOS y Tizen no funcionarán en ningún modo!

Si X-Frame-Options no están establecidos entonces el sitio web debería mostrarse en cualquiera de los Reproductores, usando cualquiera de las opciones anteriores.

Usa esta [Herramienta de Comprobación de Encabezado X-Frame-Options](https://geekflare.com/tools/x-frame-options-test) para ver si el encabezado ha sido establecido para la página web que deseas apuntar.
{/version}

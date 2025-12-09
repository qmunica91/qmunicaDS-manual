---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Incrusta HTML y Javascript para mostrar en Diseños y Listas de Reproducción"
keywords: "contenido de precarga, CSS, etiquetas de cabecera de script"
---

# Contenido Incrustado (Embedded Content)

Incrusta HTML y JavaScript para ser mostrado en Diseños y Listas de Reproducción.

{feat}Embedded HTML|v4{/feat}

## Descripción General

- Haz mejoras personalizadas sin modificar la aplicación principal.
- Para contenido con un fondo transparente marca para mostrar el Widget con un fondo transparente.
- Escala contenido con el Diseño.
- Precarga contenido fuera de pantalla.

- Ingresa texto o HTML para incrustar.
- Usa una hoja de estilo CSS para controlar el estilo visual.
- Incluye etiquetas `script` para incrustar contenido en el HEAD del documento. (Por favor mira la sección a continuación).

{version}
**NOTA:**

- Fondo transparente y Escala está disponible en Windows desde v2 R253.

- Precarga fuera de pantalla está actualmente solo disponible desde Android v2 R207.

{/version}

### Contenido HEAD para Incrustar

JavaScript debe estar envuelto en etiquetas `script`. [[PRODUCTNAME]] añadirá automáticamente jQuery.

El método `EmbedInit()` será llamado por el Reproductor y se puede usar para iniciar de forma segura cualquier JavaScript personalizado en el momento apropiado. El método está predeterminado en cualquier nuevo Elemento de medios Incrustado.

```html
<script type="text/javascript">
function EmbedInit()
{
    // Init se llamará cuando esta página se cargue en el cliente.

    return;
}
</script>
```

{tip}
Muestra HTML incrustado con contenido Active-X en un Reproductor Windows, con la configuración de seguridad de IE, para que los archivos locales puedan ejecutar contenido activo por defecto. Esto se puede hacer en Herramientas -> Opciones de Internet -> Avanzado -> Seguridad -> "Permitir que el contenido activo se ejecute en archivos en Mi PC".
{/tip}

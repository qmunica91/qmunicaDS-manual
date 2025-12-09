---
toc: "layouts"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Añade Acciones Interactivas a los Diseños para activar cambios de contenido en las Pantallas"
keywords: "webhook, touch, botón, enlace, zona interactiva, widgets interactivos, código de activación, código de diseño, identificador de código"
---

# Acciones Interactivas

Crea **Acciones** Interactivas en **Diseños** para activar cambios de contenido para mostrar en tus **Pantallas**.

Puedes tener una exhibición de producto que incluya un dispositivo 'internet de las cosas', como un sensor de luz, que podría usarse para activar un webhook para mostrar un Diseño con información específica del producto en una Pantalla para el producto con el que ha interactuado un cliente.

Podrías usar pantallas táctiles para mostrar información específica activada al presionar un botón en un Diseño, mostrado en la Pantalla.

Las Acciones pueden adjuntarse a un **Diseño** completo, **Widgets** individuales en un Diseño o en una **Imagen dentro de una Lista de Reproducción** en un Diseño, activadas por **Toque/Clic** o programáticamente por un **Webhook**.

Diseña tu Diseño, añadiendo **Widgets** para configurar como **Activadores** y **Objetivos** interactivos.

Más **Widgets Interactivos** están disponibles desde la **Caja de Herramientas**:

- **Botón** se puede usar como un Activador que se puede personalizar completamente para adaptarse a tus diseños.
- **Enlace** se puede añadir para proporcionar texto para ser usado como un Activador.
- **Zona Interactiva** para definir un área en el Diseño para ser usada como Objetivo o Activador.

Para usar una **Imagen** como activador, primero añade una **Lista de Reproducción** desde la **Caja de Herramientas** y añade una Imagen a la Línea de Tiempo de la Lista de Reproducción.

Una vez diseñado, cambia el **Modo Interactivo a ON**, ubicado en la parte superior del Editor de Diseños.

Los elementos de diseño se bloquearán para centrarse en añadir y editar **Acciones** solamente.

Las Acciones se crean haciendo clic en un elemento en el Diseño como un Activador para arrastrar una flecha a un elemento Objetivo, haciendo clic en **Guardar** desde el Panel de Propiedades.

También se pueden crear haciendo clic en **Añadir Acción** desde el **Panel de Propiedades**, y seleccionando el Tipo de Acción y Tipo de Activador.

- Seleccionar **Toque/Clic**, requiere que los dispositivos que se usarán como pantalla táctil tengan capacidades táctiles habilitadas.

- Para usar un **Webhook** se necesita ingresar un **Código de Activador** que debe estar presente en el parámetro URL `trigger=`.

Selecciona qué elemento en el Diseño debe ser el **Activador**.

- Haz clic en **Guardar**.

Se mostrarán flechas para ver fácilmente la relación entre Activadores y Objetivos.

### Tipos de Acción

- **Diseño Siguiente/Anterior** mostrará el Diseño siguiente o anterior en la programación para la(s) Pantalla(s) seleccionada(s).
- **Navegar a Diseño** usa un **Código** para identificar el Diseño al que cambiar. Usa el botón **Buscar Diseños** en la parte inferior del lienzo, para buscar Diseños por Código. Asegúrate de que los Diseños que se usarán como Objetivos Interactivos tengan un **Identificador de Código** asignado en el **formulario Editar Diseño**.
- **Widget Siguiente/Anterior** se usa con contenido desde dentro de una **Lista de Reproducción** y mostrará el elemento siguiente/anterior en esa Línea de Tiempo de la Lista de Reproducción.
- **Navegar a Widget** para especificar qué Widget cargar o haz clic en **Crear Widget** para que se pueda seleccionar un elemento de la Caja de Herramientas para añadir al Objetivo especificado.

## Lecturas Adicionales

{nonwhite}
[Control del Reproductor con Webhooks](/docs/developer/player-control/webhooks)
{/nonwhite}

[Usando el Editor de Diseños](layouts_editor)

[Usando Listas de Reproducción en Diseños](layouts_editor_playlists)

## Preguntas Frecuentes

***¿Dónde habilito las capacidades táctiles para mi dispositivo Android?***

Desde Configuración de Pantalla bajo la sección Pantallas del menú principal del CMS y usa el menú de fila para seleccionar Editar. Desde la pestaña Avanzado, marca la configuración Habilitar capacidades táctiles en el dispositivo en la parte inferior del formulario.

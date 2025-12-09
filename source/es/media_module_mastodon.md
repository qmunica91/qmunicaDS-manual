---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
aliases:
  - "media_module_twitter"
  - "media_module_twitter_metro"
  - "media_module_mastadon"
excerpt: "Muestra contenido de feed social de Mastodon en Pantallas"
keywords: "contenido social, publicaciones sociales, feeds sociales, hashtags, menciones"
---

# Mastodon

Muestra contenido de feed social de Mastodon en cualquier lugar de un Diseño usando Elementos o incluye Plantillas Estáticas con diseños preestilizados en Diseños/Listas de Reproducción.

{feat}Mastodon|v4{/feat}

El Widget de Mastodon devuelve contenido de la URL ingresada para el [Módulo](media_modules.html) que alimenta los Elementos configurados y las Plantillas Estáticas.

## Elementos de Mastodon

Los Elementos están disponibles para selección al añadir un Widget de Mastodon a un [Diseño](layouts_editor.html) para dar a los Usuarios más control sobre qué componentes del Widget de Mastodon usar y dónde se pueden colocar.

![Mastodon Elements](img/v4_media_modules_mastadon_elements.png)

Cada Elemento tiene un conjunto de opciones de configuración en el Panel de Propiedades. Se debe proporcionar un **Hashtag** para devolver resultados desde la pestaña **Configurar** para cada Elemento usado en el Diseño. Controla cómo los artículos deben ciclarse especificando una [Ranura de Datos](layouts_editor.html#content-data-slots) para usar para cada uno de los Elementos añadidos. Los Elementos de Datos pueden complementarse aún más añadiendo Elementos Globales para añadir formas y texto que se pueden poner en un Grupo de Elementos para una configuración y posicionamiento más fáciles.

Aprovecha las Plantillas (Stencils) para añadir un grupo prediseñado de Elementos a tu Diseño.

{tip}
¡Todos los Elementos en la Plantilla se tratan como 'uno' cuando se configuran y se pueden duplicar fácilmente con un clic derecho!
{/tip}

## Plantillas Estáticas de Mastodon

Las Plantillas Estáticas definen cómo deben organizarse y estilizarse los elementos devueltos y son una manera simple de mostrar elementos usando plantillas preestilizadas.

![Mastadon Templates](img/v4_media_modules_mastadon_templates.png)

Las Plantillas se pueden configurar para afectar el comportamiento de los resultados devueltos, así como hacer cambios en la apariencia del diseño usando una gama de opciones en el Panel de Propiedades. Se debe proporcionar un **Hashtag** para devolver resultados desde la pestaña **Configurar** para cada Plantilla añadida al Diseño/Lista de Reproducción.

## Descripción General

- Muestra publicaciones solo con medios adjuntos.
- Elimina Menciones, Hashtags y URLs de las publicaciones.
- Muestra publicaciones solo de servidores locales o remotos.
- Incluye un Nombre de Usuario de Mastodon para devolver estados públicos.
- Establece la duración por elemento.

{tip}
La mayoría de URLs no complementan la Señalización Digital.
{/tip}

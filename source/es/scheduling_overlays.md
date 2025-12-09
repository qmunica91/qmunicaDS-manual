---
toc: "scheduling"
maxHeadingLevel: 3
minHeadingLevel: 2
alias: "layouts_overlay"
excerpt: "Crea un Diseño de Superposición que una vez programado se sentará encima de otros Diseños en la programación"
keywords: "mostrar encima de contenido existente"
---

# Diseños de Superposición

Un Diseño de Superposición se mostrará encima de otros Diseños una vez Programado.

{tip}
Los Diseños de Superposición también pueden Programarse para usarse con Diseños dentro de una [Campaña de Lista de Diseños](scheduling_layout_list_campaign.html).
{/tip}

Los Diseños de Superposición permanecen arriba mientras tu contenido programado normal cambia debajo. Esto es particularmente útil para logotipos, información importante o avisos de emergencia, por ejemplo.

![Overlay Layout](img/v4_layouts_overlay.png)

## Crear un Diseño de Superposición

Los Diseños de Superposición se crean exactamente de la misma manera que todos los demás **Diseños**. Añade contenido para que se ajuste alrededor de tus diseños existentes para que tu Diseño de Superposición pueda "sentarse encima" de otros Diseños que están **Programados** al mismo tiempo que la Superposición. Tu Diseño de Superposición mostrará todo su contenido importante mientras los Diseños "debajo" se reproducen en rotación.

{tip}
[[PRODUCTNAME]] no renderizará el fondo en los Reproductores cuando un Diseño se programa como un Diseño de Superposición.
{/tip}

{version}
**NOTA:** Los Diseños que contienen Widgets / Multimedia que usan el navegador Edge no se pueden usar con un Diseño de Superposición ya que el contenido no puede sentarse encima de otro contenido bajo estas circunstancias. Esto incluiría HLS y YouTube Integrado. Si su contenido no es un vídeo entonces el navegador CEF se puede usar en su lugar.
{/version}

Los Diseños de Superposición se comportan de una manera diferente a los Diseños cuando se programan y solo renderizarán el contenido multimedia una vez, por lo que no mostrarán ningún contenido actualizado.

Si tu Diseño de Superposición incluye contenido que necesita ser actualizado, como Widgets de Calendario o Ticker por ejemplo, se debe añadir una Lista de Reproducción al Diseño e incluir los medios a la Lista de Reproducción. Entonces, cuando cargue el siguiente elemento en la Lista de Reproducción, recargará los otros elementos para mostrar contenido actualizado.

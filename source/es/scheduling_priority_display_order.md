---
toc: "scheduling"
maxHeadingLevel: 3
minHeadingLevel: 1
alias: "schedule_management"
excerpt: "Establece el orden de reproducción y la importancia de los eventos al programar contenido"
keywords: "tipo de evento, anular programaciones, limitar número de reproducciones, ejecutar a la hora del cms"
---

# Usando Prioridad y Orden de Visualización

[[PRODUCTNAME]] tiene una serie de herramientas de programación para permitir la creación simple de programaciones a través de una o más Pantallas/Grupos de Pantallas. Estas herramientas permiten a los usuarios definir el orden de los elementos programados para adaptar cómo se debe mostrar el contenido, así como marcar Eventos de alta prioridad para mostrarlos en la parte superior de las listas de programación.

## Prioridad

La Prioridad empuja el contenido importante al frente de cualquier programación existente y anula todos los demás eventos no prioritarios del mismo Tipo de Evento (Diseños/Campañas/Vídeo/Imágenes y Listas de Reproducción) en la programación.

Las Programaciones con una prioridad más alta tienen precedencia sobre aquellas con prioridades más bajas, siendo 0 considerada la más baja.

Por ejemplo, podrías tener un anuncio importante con información sobre una prueba de alarma de incendios que debe ser lo único que se muestre en las Pantallas en un momento específico. Asignar la Prioridad más alta a este Evento aseguraría que sea el único contenido que se muestre.

Al llegar a la hora de finalización del evento prioritario, la programación normal se reanudará en las pantallas.

## Orden de Visualización

Usa Orden de Visualización para determinar el orden de reproducción de múltiples Eventos que se han programado para mostrarse al mismo tiempo.

El orden es una clasificación numérica simple, de números más bajos a más altos, los Eventos marcados con un 1 se reproducirán antes que cualquier Evento marcado con un 2 por ejemplo.

Dejar el campo Orden de Visualización en blanco predeterminará al orden en que se añadió el Evento por primera vez.

{tip}
**NOTA:** Para asegurar que los Diseños se reproduzcan en un orden definido recomendamos añadirlos y ordenarlos en una Campaña de Lista de Diseños. El Orden de Visualización se puede usar entonces para determinar el orden en que las Campañas completas deben reproducirse.

Si las Campañas de Lista de Diseños tienen el mismo Orden de Visualización establecido o este campo se deja en blanco, los Diseños asignados a la Campaña de Lista de Diseños se reproducirán de acuerdo con el **orden de Lista de Reproducción** establecido.
{/tip}

### Máximo de Reproducciones por Hora

Existe una configuración adicional al programar Eventos para limitar el número de veces que el Evento debe mostrarse por hora en las Pantallas. Podrías tener una Imagen promocional que solo debe mostrarse una vez por hora por ejemplo.

- Establece un número aquí o déjalo como 0 para reproducciones ilimitadas.

## Lecturas Adicionales

[Estableciendo un orden de Lista de Reproducción para una Campaña](scheduling_layout_list_campaign.html)

[Mostrando una secuencia de contenido en una Lista de Reproducción](getting_started_showing_a_playlist.html)

## Preguntas Frecuentes

***¿Qué se considera el mismo Tipo de Evento para Prioridad?***

Diseños/Campañas/Imágenes/Vídeos y Listas de Reproducción se tratarán como el mismo Tipo de Evento al tener en cuenta las Prioridades.

***¿Qué pasaría si marcara la casilla Ejecutar a la hora del CMS para un evento?***

Con esto marcado, la hora del Evento sería determinada por la hora del CMS en lugar de usar la hora local de la Pantalla para las Pantallas seleccionadas.

Escenario:

- Hora CMS = GMT
- Pantalla 1 = GMT
- Pantalla 2 = GMT -4

Si un evento se programó para comenzar a las 11:00hrs, el contenido comenzaría a mostrarse en estas Pantallas a las 11:00hrs según sus zonas horarias. Estas dos Pantallas no mostrarán el mismo contenido al mismo tiempo ya que la Pantalla 2 está 4 horas detrás de la Pantalla 1.

Si se marcó Ejecutar a la hora del CMS, la Pantalla 1 comenzará a mostrar a las 11:00hrs, ya que está en la misma zona horaria que el CMS. La Pantalla 2 comenzará a mostrar contenido a las 07:00hrs ya que está 4 horas detrás de la zona horaria del CMS.

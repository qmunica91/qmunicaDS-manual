---
toc: "scheduling"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Crea tus propias Particiones del Día para simplificar la programación"
keywords: "excepciones, horas de operación de pantalla, predefinido"
---

# Partición del Día (Dayparting)

{tip}
En la programación de transmisión, dayparting es la práctica de dividir el día de transmisión en varias partes, en las cuales se transmite un tipo diferente de programa de radio o televisión apropiado para ese período de tiempo.
-- Wikipedia
{/tip}

[[PRODUCTNAME]] admite la creación de múltiples Particiones del Día, que pueden incluir excepciones por día de la semana. Esto significa que un solo día se puede dividir en tantas partes **predefinidas** como sea necesario.

{tip}
Un caso de uso típico sería un Usuario de hostelería que tiene contenido diferente para mostrar para el Desayuno, el Almuerzo y la Cena. La Partición del Día permite a ese Usuario crear una partición del día para Desayuno, Almuerzo y Cena, cada una de las cuales comienza y termina en un día diferente para su selección para simplificar la programación diaria.
{/tip}

{version}
Las **Particiones del Día** también se pueden crear para establecer las [Horas de Operación de Pantallas](displays_settings.html#content-operating-hours).
{/version}

## Añadir Partición del Día

Las Particiones del Día se crean y administran desde **Partición del Día** en el menú principal del CMS.

- Selecciona el botón **Añadir Partición del Día**.
- Completa los campos del formulario para configurar.

{tip}
¡Incluye **Excepciones** para definir diferentes tiempos de inicio y fin para días seleccionados!
{/tip}

Al Guardar, la Partición del Día estará disponible para selección en el menú desplegable **Partición del Día** del formulario de programación al añadir un Evento.

{tip}
El siguiente formulario de Partición del Día muestra un ejemplo de Partición del Día de Desayuno:

![Exanple Breakfast Daypart](img/v4_scheduling_daypart_form.png)

Sábado y Domingo se han configurado como excepciones para que el desayuno comience y termine en diferentes momentos en esos días:

![Daypart form exceptions tab](img/v4_scheduling_daypart_form_exceptions.png)

Al Programar, la Partición del Día **Desayuno** aparecerá en el menú desplegable para selección. Al seleccionar, los selectores de fecha/hora desde/hasta cambiarán a selectores de solo fecha y la hora se tomará de la configuración de Partición del Día - de acuerdo con el día de la semana en que ocurre el Evento.
{/tip}

## Editar Particiones del Día

Haz ediciones a las Particiones del Día existentes usando el menú de fila.

{tip}
¡Añade opciones de Compartir para Particiones del Día para Compartir con otros Usuarios/Grupos de Usuarios!

Actualizar los tiempos de inicio/fin o excepciones para una Partición del Día hará que los eventos futuros existentes se actualicen con los tiempos recién definidos.

Las Programaciones recurrentes existentes, configuradas para recurrir más allá del tiempo actual, tendrán nuevas Programaciones creadas para reflejar la información actualizada.
{/tip}
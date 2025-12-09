---
toc: "widgets"
minHeadingLevel: 2
excerpt: "Usa el Widget de Comando de Shell para ejecutar comandos externos"
keywords: "shell del sistema operativo, terminar comandos"
---

# Comando de Shell

Usa el Comando de Shell para instruir a la Pantalla que ejecute un comando fuera del entorno [[PRODUCTNAME]], usando el shell del sistema operativo.

{feat}Shell Command|v4{/feat}

{tip}
Añade el Widget de Comando de Shell a los Diseños para ejecutar comandos externos, como ‘subir volumen’ para un Diseño con un Widget de Audio configurado para reproducirse, y ‘bajar volumen’ cuando el Diseño termine.
{/tip}

{cloud}
{nonwhite}

Este Módulo está deshabilitado por defecto para clientes **Alojados en Xibo Cloud**. Si deseas utilizar la funcionalidad de Comando de Shell para ejecutar acciones al cargar un Diseño, contacta a nuestro servicio de asistencia a través de [Mi Cuenta](https://xibosignage.com/my-account/tickets?open=true) para solicitar que se habilite este Módulo.

{/nonwhite}
{/cloud}

## Descripción General

- El comando se ejecuta cuando un Diseño/Lista de Reproducción que contiene el Widget de Comando de Shell se reproduce a su hora programada.
- Selecciona un comando almacenado preconfigurado.
- Crea una cadena de comandos usando el constructor de comandos para pasar directamente al shell, se puede encontrar más información [aquí.](displays_command_functionality.html)
- Ingresa una cadena de comandos usando texto libre.
- Los comandos globales permiten que comandos compatibles funcionen con todos los tipos de Reproductor.
- Los Reproductores Android y Linux requieren acceso root para usar Comandos de Shell.
- Habilitar el lanzamiento de comandos creados a través de la Línea de Comandos de Windows (cmd.exe)
- Ejecuta un comando por un período fijo estableciendo una duración, por ejemplo donde tu comando muestra algo en la pantalla por un tiempo y no puede cerrarse por sí mismo.

{tip}
Al marcar la casilla **Establecer una duración** e ingresar un tiempo en segundos en la pestaña **Avanzado**, las opciones estarán disponibles en la pestaña **Configuración** para instruir a [[PRODUCTNAME]] a terminar el comando que comenzó a ejecutar.

En la mayoría de los casos, los comandos que se ejecutan desde un Diseño / Lista de Reproducción tienden a ser comandos en segundo plano que desencadenan que suceda algo como encender/apagar pantalla o reiniciar el dispositivo, etc. En tales casos, la casilla Establecer una duración se puede dejar desmarcada.

Para comandos que se ejecutan en una fecha/hora específica, como 'reinicios', 'encender/apagar' en horarios de apertura/cierre por ejemplo, entonces por favor mira [Añadir Evento](scheduling_events) en la sección de Programación y [Enviar Comando](displays.html#content-send-command) en la sección de Pantallas.
{/tip}

#### Siguiente...

[Funcionalidad de Comandos](displays_command_functionality.html)

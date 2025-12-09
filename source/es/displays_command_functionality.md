---
toc: "displays"
maxHeadingLevel: 4
minHeadingLevel: 2
excerpt: "Configura Comandos para ejecutar vía XMR, en una programación o Diseño"
keywords: "philips intents, android intents, helpers, RS232, enviar comando xmr, cadena de validación, apagar encender monitor"
persona: "display manager, administrator"
---

# Funcionalidad de Comandos

La Funcionalidad de Comandos en [[PRODUCTNAME]] se usa para configurar un conjunto de Comandos para que un Usuario seleccione ejecutar vía **XMR**, en una **Programación** o incluir en un **Diseño**.

{tip}
Los Comandos pueden tener Cadenas de Comando para aplicar a todos los Reproductores o tener una Cadena de Comando diferente por Reproductor, lo cual es particularmente útil si tu red es mixta / conectada a diferentes Pantallas o tiene hardware de Reproductor ligeramente diferente.
{/tip}

Se crea un **registro de Comando** que permite crear un "comando genérico" que puede usarse a través de **Perfiles de Pantalla**, **Eventos Programados** y el **Widget de Comando Shell**.

{tip}
¡Los Comandos proporcionan fácil acceso a la funcionalidad para RS232, Android Intents y Philips SoC (system on chip)!
{/tip}

## Gestión de Comandos

Los Comandos se crean y gestionan desde **Comandos** bajo la sección **Pantallas** del menú principal del CMS:

![Display Commands](img/v4_displays_commands.png)

Usa el menú de fila para un Comando para Editar, Eliminar y establecer opciones de [Compartir](users_features_and_sharing.html#content-share).

### Añadir Comando

Haz clic en el botón **Añadir Comando** y completa los campos relevantes del formulario:

![add_command](img/v4_displays_commands_add_command.png)

Usa el menú desplegable **Comando** para seleccionar una de las siguientes opciones para configurar:

#### Texto Libre

Escribe una Cadena de Comando

{tip}
La Cadena de Comando representa el Comando final ejecutado y puede ser una llamada directa al shell o puede tener un **helper** (ayudante) especificado, ver la sección "Helpers" a continuación.
{/tip}

#### Philips Android

{version}
La integración con Pantallas Comerciales Phillips está disponible desde Android v2 R200.
{/version}

Los siguientes comandos pueden usarse para controlar los LED situados en los lados de algunas Pantallas comerciales Phillips:

```
tpv_led|off
tpv_led|red
tpv_led|green
tpv_led|blue
tpv_led|white
```

Desde Android v2 R215, se ha añadido integración para encender/apagar la retroiluminación de la pantalla usando los siguientes comandos:

```
tpv|backlighton
tpv|backlightoff
```

{tip}
Los siguientes comandos se pueden usar solo para un modelo específico de Android 4; modelo 2016 [10BDL3051T](https://www.philips.co.uk/p-p/10BDL3051T_00/signage-solutions-multi-touch-display)

```
tpv|screenoff
tpv|screenon
```

`screenoff` apagará la pantalla y la pondrá en un estado de bajo consumo que luego se puede volver a encender con `screenon`.

Para todos los demás modelos, por favor usa `backlighton/off` ya que `screenoff` apagará completamente resultando en la necesidad de un reinicio en el sitio.
{/tip}

Los comandos de silenciar/activar sonido también se han añadido desde v2 R215:

```
tpv|mute
tpv|unmute
```

**Ten en cuenta:** `backlighton/off` no silencia el audio, así que si tienes audio reproduciéndose también querrás programar los comandos `mute/unmute` anteriores al mismo tiempo.

#### RS232

Los comandos RS232 se pueden ejecutar en Reproductores usando el prefijo `rs232` en la Cadena de Comando. El formato del comando es `rs232|<cadena de conexión>|<comando>`.

La cadena de conexión debe proporcionarse en el siguiente formato en Windows:

```
<COM#>,<Baud Rate>,<Data Bits>,<Parity|None,Odd,Even,Mark,Space>,<StopBits|None,One,Two,OnePointFive>,<Handshake|None,XOnXOff,RequestToSend,RequestToSendXOnXOff>,<HexSupport|0,1,default 0>
```

**Ten en cuenta:** Si necesitas enviar tu Comando en formato HEX, debes especificar la cadena de bytes en la Cadena de Comando, por ejemplo: `7E 00 00 FF 00 00 00 00 00 00 00 00 00 00 00 00 00 FF`, esto se convertirá en un flujo de bytes por el reproductor. Necesitarás establecer el elemento `HexSupport` de la cadena de conexión a `1`.

La cadena de conexión debe proporcionarse en el siguiente formato en Android:

```
<DeviceName>,<Baud Rate>,<Data Bits>,<Parity>,<StopBits>,<FlowControl>
```

Cada ajuste está representado por un número correspondiente:

```
DATA_BITS_5 = 5;
DATA_BITS_6 = 6;
DATA_BITS_7 = 7;
DATA_BITS_8 = 8;
PARITY_NONE = 0;
PARITY_ODD = 1;
PARITY_EVEN = 2;
PARITY_MARK = 3;
PARITY_SPACE = 4;
STOP_BITS_1 = 1;
STOP_BITS_15 = 3;
STOP_BITS_2 = 2;
FLOW_CONTROL_OFF = 0;
FLOW_CONTROL_RTS_CTS = 1;
FLOW_CONTROL_DSR_DTR = 2;
FLOW_CONTROL_XON_XOFF = 3;
```

El Comando en sí es una cadena que se envía a través de RS232 utilizando los detalles de conexión.

#### Android Intent

Los Perfiles de Pantalla Android pueden usar el helper `intent` para especificar una intención que debe llamarse cuando se ejecuta el Comando. El formato del Comando es `intent|<type|activity,service,broadcast>|<activity>|[<extras>]`.

`[<extras>]` es un parámetro opcional disponible desde **Android v2 R206** usado para proporcionar datos adicionales a la Intención. Esto debe ser una cadena con formato JSON que contenga una matriz con al menos un objeto. El formato del objeto es el siguiente y debe estar en una línea.

```json
{
  "name": "<extra name>",
  "type": "<type|string,int,bool,intArray>",
  "value": <the value of the above type>
}
```

Por ejemplo, en algunos dispositivos puedes programar el firmware para establecer horas de encendido/apagado.

```
[{
  "name": "timeon",
  "type": "intArray",
  "value": [2018, 7, 28, 8, 40]
}, {
  "name": "timeoff",
  "type": "intArray",
  "value": [2018, 7, 28, 21, 40]
}]
```

Esto se establecería en el comando como:

```
intent|broadcast|activity|[{ "name": "timeon", "type": "intArray", "value": [2018, 7, 28, 8, 40] }, { "name": "timeoff", "type": "intArray", "value": [2018, 7, 28, 21, 40] }]
```

{tip}
¡Los Comandos que contienen un helper de intención son ignorados en el Reproductor de Windows!
{/tip}

### Helpers

Los **Command Helpers** son prefijos que se pueden añadir a la Cadena de Comando para realizar una acción más avanzada. Los Comandos sin un prefijo se ejecutan en el shell del sistema operativo que ejecuta el Reproductor. `cmd.exe` en Windows y `shell` en Android.

{nonwhite}
Xibo para Android [Comando Helper para cambiar la zona horaria](/docs/setup/helper-command-to-change-time-zone)
{/nonwhite}

### Validación

La **Cadena de Validación** se usa como una comparación con la salida del **Comando** y si coincide, entonces el Comando se considera un éxito. La Cadena de Validación debe ser una coincidencia exacta.

Esto podría ser útil para una red de Reproductores mixtos de Windows y Android con un comando llamado 'Reiniciar'. La Cadena de Comando para 'Reiniciar' en Windows siendo `shutdown /r /t 0`, y en Android, es `reboot`.

{tip}
Lo mismo también puede ser útil con una red no mixta: imagina una red de reproductores de Windows con diferentes monitores conectados a través de HDMI/RS232. Se puede crear un solo Comando llamado 'Encender Monitor' con las diferentes marcas de monitor representadas por diferentes Perfiles de Configuración de Pantalla, cada uno puede tener una Cadena de Comando diferente para encender/apagar el monitor.
{/tip}

### Disponible en

Selecciona en qué tipo de Pantalla estará disponible el Comando, déjalo en blanco para aplicar el Comando a todos los tipos de Pantalla.

{tip}
¡Las cadenas de **Comando** y **Validación** se pueden anular editando un [Perfil de Pantalla](displays_settings.html#setting_on_the_display) y usando la pestaña **Comando**!
{/tip}

## Enviar Comando XMR

Ejecuta Comandos vía **XMR** desde Pantallas/Grupos de Pantallas usando el menú de fila:

## Programar Comandos

**Programa Comandos** para que se ejecuten a una hora específica

- Haz clic en **Programación** desde el menú principal del CMS.
- Selecciona [Añadir Evento](scheduling_events.html#content-add-event) desde la parte superior de la cuadrícula de Programación.

- Desde el menú desplegable Tipo de Evento selecciona **Comando**.
- Completa los campos del formulario y selecciona el **Comando** a usar y la **Hora de Inicio**.

{tip}
Los comandos programados se ejecutan una vez en el Reproductor y solo requieren una fecha y hora de **Inicio**. El Comando se puede ejecutar hasta 10 segundos después de la hora seleccionada.
{/tip}

## Comandos Shell

Usa el [Widget de Comando Shell](media_module_shellcommand.html) para ejecutar Comandos externos basados en la actividad de los Diseños.

Los Comandos Shell con un Comando como su fuente actúan de la misma manera que los comandos shell normales. El Comando se ejecuta cuando el Widget se muestra en el Diseño.

Un Comando Shell también puede ser una Cadena de Comando con opciones para todos los Reproductores proporcionados. Esto permite a los Usuarios añadir Comandos 'ad-hoc' para un solo uso.

{tip}
¡Recomendamos que los Administradores creen comandos predefinidos cuando sea posible!
{/tip}

## Encender/Apagar Monitor

### HDMI-CEC

HDMI-CEC es un bus que se implementa en casi todos los televisores de pantalla grande nuevos que tienen conectores HDMI. Este bus (que está físicamente conectado dentro de los cables HDMI normales) admite señales de control que pueden realizar encendido, apagado, ajustes de volumen, selección de fuente de video y muchas de las características accesibles a través del control remoto del televisor. También puede controlar la mayoría del otro hardware en el bus HDMI.

[[PRODUCTNAME]] no proporciona una interfaz directa a HDMI-CEC ya que hay muchas especificaciones de fabricantes diferentes, sin embargo, es posible controlar HDMI-CEC a través de un archivo por lotes.

### Serial/RS232

Los monitores de grado industrial a menudo tienen una interfaz serie para encender y apagar el panel del monitor. [[PRODUCTNAME]] puede usar el helper de Comando RS232 para enviar estos Comandos al monitor, generalmente en modo HEX.

Se han probado los siguientes monitores y Comandos:

#### NEC E464

- Encender - `rs232|COM1,9600,8,None,One,None,1|01 30 41 30 41 30 43 02 43 32 30 33 44 36 30 30 30 31 03 73 0d`
- Apagar - `rs232|COM1,9600,8,None,One,None,1|01 30 41 30 41 30 43 02 43 32 30 33 44 36 30 30 30 34 03 76 0d`

#### Sharp LC-42D69U

- Encender - `rs232|COM1,9600,8,None,One,None,1|50 4F 57 52 31 20 20 20 0D`
- Apagar - `rs232|COM1,9600,8,None,One,None,1|50 4F 57 52 00 20 20 20 0D`

#### LG 55LK520

- Encender - `rs232|COM1,9600,8,None,One,None,1|6B 61 20 30 30 20 30 31 0D`
- Apagar - `rs232|COM1,9600,8,None,One,None,1|6B 61 20 30 30 20 30 30 0D`

{tip}
Debe tenerse en cuenta que otros modelos de cada marca también deberían usar los mismos Comandos.
{/tip}

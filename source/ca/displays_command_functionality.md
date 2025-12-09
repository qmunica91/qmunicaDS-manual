---
toc: "displays"
maxHeadingLevel: 4
minHeadingLevel: 2
excerpt: "Configura Comandaments per executar via XMR, en una programació o Disseny"
keywords: "philips intents, android intents, helpers, RS232, enviar comandament xmr, cadena de validació, apagar encendre monitor"
persona: "display manager, administrator"
---

# Funcionalitat de Comandaments

La Funcionalitat de Comandaments en [[PRODUCTNAME]] s'usa per configurar un conjunt de Comandaments perquè un Usuari seleccioni executar via **XMR**, en una **Programació** o incloure en un **Disseny**.

{tip}
Els Comandaments poden tenir Cadenes de Comandament per aplicar a tots els Reproductors o tenir una Cadena de Comandament diferent per Reproductor, la qual cosa és particularment útil si la teva xarxa és mixta / connectada a diferents Pantalles o té maquinari de Reproductor lleugerament diferent.
{/tip}

Es crea un **registre de Comandament** que permet crear un "comandament genèric" que pot usar-se a través de **Perfils de Pantalla**, **Esdeveniments Programats** i el **Widget de Comandament Shell**.

{tip}
¡Els Comandaments proporcionen fàcil accés a la funcionalitat per RS232, Android Intents i Philips SoC (system on chip)!
{/tip}

## Gestió de Comandaments

Els Comandaments es creen i gestionen des de **Comandaments** sota la secció **Pantalles** del menú principal del CMS:

![Display Commands](img/v4_displays_commands.png)

Usa el menú de fila per a un Comandament per Editar, Eliminar i establir opcions de [Compartir](users_features_and_sharing.html#content-share).

### Afegir Comandament

Fes clic al botó **Afegir Comandament** i completa els camps rellevants del formulari:

![add_command](img/v4_displays_commands_add_command.png)

Usa el menú desplegable **Comandament** per seleccionar una de les següents opcions per configurar:

#### Text Lliure

Escriu una Cadena de Comandament

{tip}
La Cadena de Comandament representa el Comandament final executat i pot ser una crida directa al shell o pot tenir un **helper** (ajudant) specificat, veure la secció "Helpers" a continuació.
{/tip}

#### Philips Android

{version}
La integració amb Pantalles Comercials Phillips està disponible des d'Android v2 R200.
{/version}

Els següents comandaments poden usar-se per controlar els LED situats als costats d'algunes Pantalles comercials Phillips:

```
tpv_led|off
tpv_led|red
tpv_led|green
tpv_led|blue
tpv_led|white
```

Des d'Android v2 R215, s'ha afegit integració per encendre/apagar la retroil·luminació de la pantalla usant els següents comandaments:

```
tpv|backlighton
tpv|backlightoff
```

{tip}
Els següents comandaments es poden usar només per a un model específic d'Android 4; model 2016 [10BDL3051T](https://www.philips.co.uk/p-p/10BDL3051T_00/signage-solutions-multi-touch-display)

```
tpv|screenoff
tpv|screenon
```

`screenoff` apagarà la pantalla i la posarà en un estat de baix consum que després es pot tornar a encendre amb `screenon`.

Per a tots els altres models, si us plau usa `backlighton/off` ja que `screenoff` apagarà completament resultant en la necessitat d'un reinici en el lloc.
{/tip}

Els comandaments de silenciar/activar so també s'han afegit des de v2 R215:

```
tpv|mute
tpv|unmute
```

**Tingues en compte:** `backlighton/off` no silencia l'àudio, així que si tens àudio reproduint-se també voldràs programar els comandaments `mute/unmute` anteriors al mateix temps.

#### RS232

Els comandaments RS232 es poden executar en Reproductors usant el prefix `rs232` en la Cadena de Comandament. El format del comandament és `rs232|<cadena de connexió>|<comandament>`.

La cadena de connexió ha de proporcionar-se en el següent format en Windows:

```
<COM#>,<Baud Rate>,<Data Bits>,<Parity|None,Odd,Even,Mark,Space>,<StopBits|None,One,Two,OnePointFive>,<Handshake|None,XOnXOff,RequestToSend,RequestToSendXOnXOff>,<HexSupport|0,1,default 0>
```

**Tingues en compte:** Si necessites enviar el teu Comandament en format HEX, has d'especificar la cadena de bytes en la Cadena de Comandament, per exemple: `7E 00 00 FF 00 00 00 00 00 00 00 00 00 00 00 00 00 FF`, això es convertirà en un flux de bytes pel reproductor. Necessitaràs establir l'element `HexSupport` de la cadena de connexió a `1`.

La cadena de connexió ha de proporcionar-se en el següent format en Android:

```
<DeviceName>,<Baud Rate>,<Data Bits>,<Parity>,<StopBits>,<FlowControl>
```

Cada ajust està representat per un número corresponent:

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

El Comandament en si és una cadena que s'envia a través de RS232 utilitzant els detalls de connexió.

#### Android Intent

Els Profils de Pantalla Android poden usar el helper `intent` per especificar una intenció que s'ha de cridar quan s'executa el Comandament. El format del Comandament és `intent|<type|activity,service,broadcast>|<activity>|[<extras>]`.

`[<extras>]` és un paràmetre opcional disponible des d'**Android v2 R206** usat per proporcionar dades addicionals a la Intenció. Això ha de ser una cadena amb format JSON que contingui una matriu amb almenys un objecte. El format de l'objecte és el següent i ha d'estar en una línia.

```json
{
  "name": "<extra name>",
  "type": "<type|string,int,bool,intArray>",
  "value": <the value of the above type>
}
```

Per exemple, en alguns dispositius pots programar el firmware per establir hores d'encès/apagat.

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

Això s'establiria en el comandament com:

```
intent|broadcast|activity|[{ "name": "timeon", "type": "intArray", "value": [2018, 7, 28, 8, 40] }, { "name": "timeoff", "type": "intArray", "value": [2018, 7, 28, 21, 40] }]
```

{tip}
¡Els Comandaments que contenen un helper d'intent són ignorats en el Reproductor de Windows!
{/tip}

### Helpers

Els **Command Helpers** són prefixos que es poden afegir a la Cadena de Comandament per realitzar una acció més avançada. Els Comandaments sense un prefix s'executen en el shell del sistema operatiu que executa el Reproductor. `cmd.exe` en Windows i `shell` en Android.

{nonwhite}
Xibo per Android [Comandament Helper per canviar la zona horària](/docs/setup/helper-command-to-change-time-zone)
{/nonwhite}

### Validació

La **Cadena de Validació** s'usa com una comparació amb la sortida del **Comandament** i si coincideix, llavors el Comandament es considera un èxit. La Cadena de Validació ha de ser una coincidència exacta.

Això podria ser útil per a una xarxa de Reproductors mixtos de Windows i Android amb un comandament anomenat 'Reiniciar'. La Cadena de Comandament per 'Reiniciar' en Windows sent `shutdown /r /t 0`, i en Android, és `reboot`.

{tip}
El mateix també pot ser útil amb una xarxa no mixta: imagina una xarxa de reproductors de Windows amb diferents monitors connectats a través de HDMI/RS232. Es pot crear un sol Comandament anomenat 'Encendre Monitor' amb les diferents marques de monitor representades per diferents Perfils de Configuració de Pantalla, cadascun pot tenir una Cadena de Comandament diferent per encendre/apagar el monitor.
{/tip}

### Disponible a

Selecciona en quin tipus de Pantalla estarà disponible el Comandament, deixa-ho en blanc per aplicar el Comandament a tots els tipus de Pantalla.

{tip}
¡Les cadenes de **Comandament** i **Validació** es poden anul·lar editant un [Perfil de Pantalla](displays_settings.html#setting_on_the_display) i usant la pestanya **Comandament**!
{/tip}

## Enviar Comandament XMR

Executa Comandaments via **XMR** des de Pantalles/Grups de Pantalles usant el menú de fila:

## Programar Comandaments

**Programa Comandaments** perquè s'executin a una hora específica

- Fes clic en **Programació** des del menú principal del CMS.
- Selecciona [Afegir Esdeveniment](scheduling_events.html#content-add-event) des de la part superior de la quadrícula de Programació.

- Des del menú desplegable Tipus d'Esdeveniment selecciona **Comandament**.
- Completa els camps del formulari i selecciona el **Comandament** a usar i l'**Hora d'Inici**.

{tip}
Els comandaments programats s'executen una vegada en el Reproductor i només requereixen una data i hora d'**Inici**. El Comandament es pot executar fins a 10 segons després de l'hora seleccionada.
{/tip}

## Comandaments Shell

Usa el [Widget de Comandament Shell](media_module_shellcommand.html) per executar Comandaments externs basats en l'activitat dels Dissenys.

Els Comandaments Shell amb un Comandament com la seva font actuen de la mateixa manera que els comandaments shell normals. El Comandament s'executa quan el Widget es mostra en el Disseny.

Un Comandament Shell també pot ser una Cadena de Comandament amb opcions per a tots els Reproductors proporcionats. Això permet als Usuaris afegir Comandaments 'ad-hoc' per a un sol ús.

{tip}
¡Recomanem que els Administradors creïn comandaments predefinits quan sigui possible!
{/tip}

## Encendre/Apagar Monitor

### HDMI-CEC

HDMI-CEC és un bus que s'implementa en gairebé tots els televisors de pantalla gran nous que tenen connectors HDMI. Aquest bus (que està físicament connectat dins dels cables HDMI normals) admet senyals de control que poden realitzar encès, apagat, ajustos de volum, selecció de font de vídeo i moltes de les característiques accessibles a través del control remot del televisor. També pot controlar la majoria de l'altre maquinari en el bus HDMI.

[[PRODUCTNAME]] no proporciona una interfície directa a HDMI-CEC ja que hi ha moltes especificacions de fabricants diferents, no obstant això, és possible controlar HDMI-CEC a través d'un fitxer per lots.

### Serial/RS232

Els monitors de grau industrial sovint tenen una interfície sèrie per encendre i apagar el panell del monitor. [[PRODUCTNAME]] pot usar el helper de Comandament RS232 per enviar aquests Comandaments al monitor, generalment en mode HEX.

S'han provat els següents monitors i Comandaments:

#### NEC E464

- Encendre - `rs232|COM1,9600,8,None,One,None,1|01 30 41 30 41 30 43 02 43 32 30 33 44 36 30 30 30 31 03 73 0d`
- Apagar - `rs232|COM1,9600,8,None,One,None,1|01 30 41 30 41 30 43 02 43 32 30 33 44 36 30 30 30 34 03 76 0d`

#### Sharp LC-42D69U

- Encendre - `rs232|COM1,9600,8,None,One,None,1|50 4F 57 52 31 20 20 20 0D`
- Apagar - `rs232|COM1,9600,8,None,One,None,1|50 4F 57 52 00 20 20 20 0D`

#### LG 55LK520

- Encendre - `rs232|COM1,9600,8,None,One,None,1|6B 61 20 30 30 20 30 31 0D`
- Apagar - `rs232|COM1,9600,8,None,One,None,1|6B 61 20 30 30 20 30 30 0D`

{tip}
S'ha de tenir en compte que altres models de cada marca també haurien d'usar els mateixos Comandaments.
{/tip}

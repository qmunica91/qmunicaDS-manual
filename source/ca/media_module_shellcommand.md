---
toc: "widgets"
minHeadingLevel: 2
excerpt: "Usa el Widget de Comandament de Shell per executar comandaments externs"
keywords: "shell del sistema operatiu, acabar comandaments"
---

# Comandament de Shell

Usa el Comandament de Shell per instruir a la Pantalla que executi un comandament fora de l'entorn [[PRODUCTNAME]], usant el shell del sistema operatiu.

{feat}Shell Command|v4{/feat}

{tip}
Afegeix el Widget de Comandament de Shell als Dissenys per executar comandaments externs, com ‘pujar volum’ per a un Disseny amb un Widget d'Àudio configurat per reproduir-se, i ‘baixar volum’ quan el Disseny acabi.
{/tip}

{cloud}
{nonwhite}

Aquest Mòdul està deshabilitat per defecte per clients **Allotjats en Xibo Cloud**. Si desitges utilitzar la funcionalitat de Comandament de Shell per executar accions al carregar un Disseny, contacta al nostre servei d'assistència a través de [El Meu Compte](https://xibosignage.com/my-account/tickets?open=true) per sol·licitar que s'habiliti aquest Mòdul.

{/nonwhite}
{/cloud}

## Descripció General

- El comandament s'executa quan un Disseny/Llista de Reproducció que conté el Widget de Comandament de Shell es reprodueix a la seva hora programada.
- Selecciona un comandament emmagatzemat preconfigurat.
- Crea una cadena de comandaments usant el constructor de comandaments per passar directament al shell, es pot trobar més informació [aquí.](displays_command_functionality.html)
- Ingressa una cadena de comandaments usant text lliure.
- Els comandaments globals permeten que comandaments compatibles funcionin amb tots els tipus de Reproductor.
- Els Reproductors Android i Linux requereixen accés root per usar Comandaments de Shell.
- Habilitar el llançament de comandaments creats a través de la Línia de Comandaments de Windows (cmd.exe)
- Executa un comandament per un període fix establint una durada, per exemple on el teu comandament mostra alguna cosa a la pantalla per un temps i no pot tancar-se per si mateix.

{tip}
Al marcar la casella **Establir una durada** i ingressar un temps en segons a la pestanya **Avançat**, les opcions estaran disponibles a la pestanya **Configuració** per instruir a [[PRODUCTNAME]] a acabar el comandament que va començar a executar.

En la majoria dels casos, els comandaments que s'executen des d'un Disseny / Llista de Reproducció tendeixen a ser comandaments en segon pla que desencadenen que passi alguna cosa com encendre/apagar pantalla o reiniciar el dispositiu, etc. En tals casos, la casella Establir una durada es pot deixar desmarcada.

Per comandaments que s'executen en una data/hora específica, com 'reinicis', 'encendre/apagar' en horaris d'obertura/tancament per exemple, llavors si us plau mira [Afegir Esdeveniment](scheduling_events) a la secció de Programació i [Enviar Comandament](displays.html#content-send-command) a la secció de Pantalles.
{/tip}

#### Següent...

[Funcionalitat de Comandaments](displays_command_functionality.html)

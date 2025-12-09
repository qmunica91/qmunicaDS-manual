---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Mostra contingut de Pàgina Web afegint el Widget de Pàgina Web als Dissenys"
keywords: "obrir nativament, posició manual, millor ajust, precàrrega, error de càrrega de pàgina web"
---

# Pàgina Web

Inclou contingut d'una pàgina web per ser mostrat en Dissenys i Llistes de Reproducció.

{feat}Webpage|v4{/feat}

{version}
**Nota:** El Widget de Pàgina Web requereix una connexió a internet vàlida per funcionar ja que les pàgines web no són emmagatzemades en memòria cau pel Reproductor.
{/version}

## Descripció General

- Veu una pàgina web completa sense alteracions.
- Opcions d'incrustació Obrir Nativament, Posició Manual i Millor Ajust.
- Escala i desplaça la pàgina web objectiu per mostrar una secció particular de la pàgina web.
- Per contingut amb un fons transparent marca per mostrar el Widget amb un fons transparent.
- Precàrrega contingut fora de pantalla.
- Dispara un web hook per navegar a una [acció](layouts_interactive_actions.html) activa en el cas d'un error de càrrega de pàgina web.

{version}

**NOTA:**

- Fons transparent està disponible en Windows des de v2 R253. [[PRODUCTNAME]] farà el seu millor esforç per fer això quan estigui habilitat per pàgines que tenen un fons transparent, no obstant això, no pot ser suportat en algunes pàgines web.
- Precàrrega fora de pantalla està actualment només disponible des d'Android v2 R207.

{/version}

### Obrir Nativament

Quan se selecciona, el Reproductor obrirà la pàgina web sense cap alteració i obrirà i renderizarà en el navegador com si la URL hagués estat visitada en el dispositiu fora de [[PRODUCTNAME]].

{tip}
**Si us plau tingues en compte:** ¡No hi ha previsualització disponible amb aquesta opció!
{/tip}

### Disparar un web hook

Dispara un web hook per a una acció activa (navegar a Widget, navegar a Disseny un Comandament Programat, etc.) per ser mostrada en el cas que la pàgina web retorni un error i falli al carregar.

{feat}Webpage - Page load error trigger|v4{/feat}

- Ingressa el **Codi de Disparador** d'una Acció configurada per coincidir amb un paràmetre `trigger` de web hook subministrat.

### Posició Manual

Aquesta opció incrustarà la pàgina web en un iframe on els usuaris poden especificar les dimensions requerides.

- Usa les configuracions de Desplaçament i Escalla per forçar que la pàgina/seccions de la pàgina s'ajustin dins de les dimensions per mostrar només una secció de la pàgina web.

### Millor Ajust

Aquesta opció incrustarà la pàgina web en un iframe on els usuaris poden especificar les dimensions requerides.

{version}
**NOTA:** Les opcions **Posició Manual** i **Millor Ajust** no funcionaran amb llocs web que estableixen l'**encapçalament X-Frame-Options**. Si no pots veure la pàgina web usa l'opció Obrir Nativament quan usis Windows / Linux o Android.

Si X-Frame-Options estan establerts, llavors webOS i Tizen no funcionaran en cap mode!

Si X-Frame-Options no estan establerts, llavors el lloc web hauria de mostrar-se en qualsevol dels Reproductors, usant qualsevol de les opcions anteriors.

Usa aquesta [Eina de Comprovació d'Encapçalament X-Frame-Options](https://geekflare.com/tools/x-frame-options-test) per veure si l'encapçalament ha estat establert per a la pàgina web que desitges apuntar.
{/version}

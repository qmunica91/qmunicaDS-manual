---
toc: "configure"
maxHeadingLevel: 3
minHeadingLevel: 2
alias: "tour_cms_settings"
excerpt: "Opcions configurables en els Ajustos del CMS per a Administradors"
keywords: "redimensionar imatges, predeterminats de transició, publicar disseny automàticament, ajustos predeterminats de prova de reproducció, biblioteca neta, ajustos de manteniment, ajustos de xarxa, ajustos regionals, establir zona horària, establir idioma, política de contrasenyes, recordatori de contrasenya, autenticació de dos factors, fonts, aplicacions, disseny predeterminat global"
---

# Ajustos d'Administrador del CMS

{nonwhite}
Un cop el teu CMS estigui instal·lat, es requereix alguna configuració addicional per habilitar tota la funcionalitat. Si us plau consulta la següent guia: [Guia de Configuració Posterior a la Instal·lació del CMS](/docs/setup/xibo-cms-post-installation-setup-guide.html)
{/nonwhite}

Com qualsevol aplicació complexa, el CMS de [[PRODUCTNAME]] ve amb un nombre d'opcions configurables. Aquestes es troben en la pàgina **Configuració** sota la secció **Administració** del menú principal del CMS.

{nonwhite}
{cloud}
Els clients allotjats en **Xibo Cloud** tindran alguns d'aquests camps pre-poblats com a part del servei. Alguns poden canviar-se i altres estan bloquejats per deshabilitar l'edició. Per a més informació, si us plau consulta aquesta pàgina: [Predeterminats i Restriccions del CMS de Xibo Cloud](/docs/setup/xibo-in-the-cloud.html#content-xibo-cloud-cms-defaults-and-restrictions).
{/cloud}
{/nonwhite}

Els ajustos es divideixen en pestanyes de categories relacionades:

![CMS Settings](img/v4_tour_cms_settings_admin.png)

## Configuració

Des d'aquesta pestanya visualitza la **Clau Secreta del CMS** que s'usa per autenticar Reproductors amb el CMS i aplica un **Tema** a les pàgines (si aplica) així com configurar el posicionament predeterminat per al [Menú de Navegació](tour_cms_navigation.html).

## Predeterminats

Usa aquesta pestanya per aplicar valors predeterminats a tots els fitxers de [Mitjans](media_library.html) i establir [Transicions](configure_transitions.html) predeterminades.

També pots configurar Dissenys per **Publicar automàticament** 30 minuts després de l'última edició registrada habilitant la casella de verificació per a aquest ajust.

### Redimensionar Imatges

Se poden especificar llindars i límits predeterminats que després es consideren en el cas que una imatge s'hagi de redimensionar. Això podria ser al pujar una imatge o al descarregar una imatge per un Widget - NASA RSS en un Widget Ticker per exemple.

- #### Llindar de Redimensionament

Estableix un llindar màxim (basat en el costat més llarg) que s'ha de considerar per redimensionar una imatge.

{tip}
Si estableixes un Llindar de Redimensionament de 1920 i puges/descarregues una imatge que és 800, aquesta imatge no necessitaria redimensionar-se. Si vas pujar/descarregar una imatge que era 2400, aquesta es redimensionaria a 1920.
{/tip}

- #### Límit de Redimensionament

Estableix un límit (basat en el costat més llarg) per a imatges pujades/descarregades. Les imatges que excedeixin aquest límit no es processaran i han de reemplaçar-se amb una altra imatge que estigui dins del límit.

Aquest ajust determinarà si el fitxer d'imatge és massa gran per ser processat.

- #### Nombre màxim de Files de Conjunt de Dades

Estableix el nombre màxim permès de files que un Usuari pot crear en un Conjunt de Dades.

{nonwhite}
{cloud}
El valor predeterminat per a clients de Cloud s'estableix en 10,000 files per Conjunt de Dades.
{/cloud}
{/nonwhite}

## **Pantallas**

Estableix valors predeterminats per a **Latitud** i **Longitud** per a totes les vistes prèvies conscients de Geo en tot el CMS.

### Disseny Predeterminat

El Disseny Predeterminat establert aquí s'assignarà automàticament a totes les Pantalles per mostrar-se quan no hi hagi un altre contingut programat o si hi ha un problema que impedeixi que es mostri un Event programat.

{nonwhite}
{tip}
Pots crear el teu propi Disseny per reemplaçar el predeterminat preestablert, però tingues en compte que els dissenys han de mantenir-se simples sense contingut multimèdia o web complex.
{/tip}
{/nonwhite}

Aquest Disseny Predeterminat global pot ser anul·lat per a Pantalles individuals seleccionant un [Disseny Predeterminat](displays.html#content-default-layout) alternatiu per usar.

### Ajustos Predeterminats de Prova de Reproducció

Estableix el **Nivell d'agregació** de la recopilació d'estadístiques de [Prova de Reproducción](displays_metrics.html) per aplicar a tots els **Dissenys** / **Mitjans** i **elements de Widget** per defecte.

- **Individual** - les estadístiques es registren a l'inici i al final de cada element individualment i s'envien de tornada al CMS en cada interval de recopilació.
- **Horari** - registra cada element una vegada, i inclou el nombre total de vegades reproduït i la durada del temps reproduït durant l'hora i s'envia de tornada al CMS en el següent interval de recopilació després que el període d'hora hagi expirat.
- **Diari** - registra cada element una vegada, i inclou el nombre total de vegades reproduït i la durada del temps reproduït durant el dia i s'envia de tornada al CMS en el següent interval de recopilació després que el dia hagi expirat.

{tip}
¡Els Reproductors agreguen només 'registres completats', amb la recopilació feta al final de la durada dels Widgets, així que si un Widget té una durada de 3 hores, l'estadística es registrarà una vegada que el Widget hagi expirat!
{/tip}

- Usa aquesta casella per **habilitar la recopilació** d'estadístiques de Prova de Reproducció a totes les **Pantalles** per defecte.

{tip}
Això es pot alternar encès/apagat editant [Perfils de Configuració de Pantalla](displays_settings.html#content-editing-profiles).
{/tip}

- Marca la casella per establir el valor predeterminat en encès per a la recopilació d'estadístiques de Prova de Reproducció per a tots els **Dissenys** recentment afegits.

{tip}
La recopilació es pot deshabilitar desmarcant la casella en el formulari **Afegir/Editar** Disseny.
{/tip}

Usa els ajustos per habilitar la recopilació d'estadístiques de Prova de Reproducció per aplicar a tots els **Mitjans**, **Llistes de Reproducció** i **Widgets** (Apagat/Encès/Heretar).

{tip}
¡Es pretén que **Widget** sempre estigui establert en Heretar perquè les opcions de Disseny i Mitjans controlin la recopilació!
{/tip}

## General

Visualitza/estableix l'adreça per al **Manual d'Usuari** i marca per enviar **estadístiques anònimes** per ajudar a millorar el programari.

### Neteja de Llibreria (Global)

La Llibreria pot ser *netejada* per un Super Administrador o Usuari perquè es mantingui neta i petita.
**Les accions no poden revertir-se, per la qual cosa això ha d'usar-se amb precaució.**

{tip}
Això podria ser de particular interès si el CMS està instal·lat en un servidor web que té quotes o si als Usuaris se'ls han assignat les seves pròpies quotes.
{/tip}

Els Administradors poden iniciar una operació de neteja de Llibreria en tot el sistema fent clic al botó **Netejar Llibreria** a la cantonada dreta de la pàgina de Configuració:

![Settings Tidy Library](img/v4_tour_cms_settings_tidy_library.png)

Com aquesta funcionalitat és en tot el sistema i per tant opera en **TOTS** els fitxers d'Usuari, es requereix confirmació per eliminar revisions no utilitzades i antigues.

Aquesta opció és més completa i elimina:

- Fitxers temporals
- Fitxers orfes
- Miniatures
- Revisions de mitjans que no s'usen enlloc
- Mitjans que no s'usen enlloc (en cap Disseny / Grup de Pantalles / Pantalles)
- Fitxers genèrics pujats al CMS

#### Fitxers orfes

Els fitxers orfes són una ocurrència rara on un fitxer emmagatzemat en disc en la carpeta de la Llibreria no s'elimina quan l'element de Mitjans s'elimina de la Llibreria. Això significa que el fitxer existeix però el CMS no en sap res al respecte.

### Neteja des de Llibreria d'Usuari

{nonwhite}
{cloud}
La funció de Netejar Llibreria està desactivada per defecte per a clients de **Xibo Cloud Hosting** ja que pot ser potencialment destructiva si les opcions no s'entenen completament.
{/cloud}
{/nonwhite}

Permet a un Usuari netejar fitxers des de la pàgina de [Llibreria](media_library.html#content-tidy-library) usant la casella de verificació per a **Habilitar Neteja de Llibreria**.

## Manteniment

Des d'aquí **Habilitar Manteniment** i **Alertes de Correu Electrònic** per ser enviades i establir les edats màximes de retenció per a **Registres** i **Estadístiques**.

## Xarxa

Des de la pestanya Xarxa completa una **adreça de correu electrònic d'Admin** per a l'administrador general del CMS. Totes les notificacions de correu electrònic generades pel CMS s'enviaran a aquesta adreça.

Assegura't que l'**adreça de correu electrònic d'enviament** i el **nom** estiguin complets abans de configurar qualsevol notificació de correu electrònic addicional en tot el CMS.

{nonwhite}
{noncloud}
També pots proporcionar informació del Servidor Proxy (si el teu CMS està darrere d'un proxy) forçar **HTTPS** i establir límits mensuals d'**Amplada de Banda** i mida de **Llibreria**.
{/noncloud}
{/nonwhite}

## Compartir

Usa el menú desplegable per canviar com apareix el color del Widget en les Llistes de Reproducció per als Usuaris.

- **Acolorit de Mitjans** usarà els colors del **tema** per a cada Widget.
- **Acolorit de Compartir** mostrarà el color del Widget basat en l'**accés d'Usuari** des de les opcions de **Compartir**. (Verd = editable)

Des d'aquí pots establir si els Usuaris han de tenir la capacitat de programar a Pantalles quan les opcions de Compartir estan establertes en Veure per a l'Usuari, així com poder establir si els Usuaris han de poder veure els noms dels Dissenys en programacions que no s'han compartit amb ells.

Marca per permetre als Usuaris guardar el seu contingut en la [Carpeta Arrel](configure_folders.html) de nivell superior o deshabilita per forçar els Usuaris a seleccionar una Carpeta per guardar.

## Regional

Des d'aquesta pestanya estableix l'**Idioma** i la **Zona Horària** predeterminada i el **Format de Data** per usar en tot el CMS.

{tip}
¡Selecciona la ciutat principal més propera a la teva zona horària!
{/tip}

Usa la casella de verificació per detectar l'**idioma del navegador** per usar en el CMS i selecciona quin tipus de **Calendari** ha d'usar-se.

## Resolució de Problemes

Aquesta pestanya s'usa per establir Nivells de Registre que són útils per capturar errors de php i problemes d'entorn.

## Usuaris

Selecciona l'Usuari del Sistema i estableix el Grup d'Usuaris Predeterminat i el Tipus d'Usuari al incorporar nous Usuaris.

{tip}
¡Recomanem que el **Tipus d'Usuari Predeterminat** s'estableixi en **Usuari**!
{/tip}

### Política de Contrasenyes

Ingressa qualsevol expressió regular vàlida en el camp **Expressió Regular de Política de Contrasenyes** perquè totes les sol·licituds de canvi de contrasenya i contrasenyes recentment creades es provin contra això.

{tip}
¡Es mostrarà una descripció de text als Usuaris quan les seves contrasenyes no compleixin amb la política requerida com a avís!
{/tip}

{nonwhite}
{cloud}
Els clients amb [Xibo Cloud Hosting](/hosting) tenen una **política predeterminada establerta** que requereix una contrasenya d'almenys 10 caràcters.
{/cloud}
{/nonwhite}

### Recordatori de Contrasenya

Habilita per proporcionar un enllaç de restabliment de **Has oblidat la teva Contrasenya?** per a **Usuaris** al iniciar sessió perquè puguin recuperar fàcilment l'accés al CMS.

{tip}
¡Assegura't que s'hagi ingressat una **adreça de correu electrònic d'enviament** vàlida en la pestanya **Xarxa** abans d'habilitar aquesta funcionalitat!
{/tip}

Es mostrarà a l'Usuari un enllaç que, un cop clicat, enviarà una **Notificació de Restabliment de Contrasenya** a la seva adreça de correu electrònic segons consta en el seu Perfil d'Usuari.

{tip}
Els **Usuaris** també poden canviar les seves pròpies contrasenyes, un cop hagin iniciat sessió en el CMS, des del seu **Perfil d'Usuari**.
{/tip}

## Autenticació de Dos Factors

[Autenticació de Dos Factors](index.html) pot ser configurada per un Usuari per a major seguretat un cop hagi iniciat sessió.

Un cop configurada, un Usuari necessitaria ingressar el codi enviat per correu electrònic o com es mostra en l'aplicació Google Authenticator per completar l'inici de sessió per obtenir accés al CMS.

{tip}
¡Assegura't que l'usuari hagi proporcionat una adreça de correu electrònic per rebre el correu electrònic generat!
{/tip}

Estableix una **adreça de correu electrònic d'enviament** vàlida en la pestanya **Xarxa** i s'ha ingressat un nom en el camp **Emissor de Dos Factors** perquè quedi clar en l'aplicació Google Authenticator i el correu electrònic quan es generin codis autenticats per iniciar sessió en el CMS.

Restableix l'Autenticació de Dos Factors per a Usuaris des del seu Perfil d'Usuari.

## Aplicacions

[[PRODUCTNAME]] conté una API que permet a aplicacions de tercers connectar-se i consumir les seves dades.

Les aplicacions s'afegeixen i configuren des de **Aplicacions** sota la secció **Administració** del menú principal del CMS.

{tip}
Abans d'usar una Aplicació, cada Usuari ha d'autoritzar l'aplicació per actuar en el seu nom dins del CMS.
Els Usuaris poden veure Aplicacions autoritzades des de la secció Les Meves Aplicacions del seu **Perfil d'Usuari**.
{/tip}

En aquest moment, el CMS no proporciona als Usuaris individuals un mètode per revocar l'accés a una aplicació. Només un Administrador pot eliminar una aplicació completament.

## Fonts

[[PRODUCTNAME]] ve amb un conjunt de fonts estàndard que es poden configurar en molts Widgets:

- Aileron Heavy Regular (Aileron-Heavy.otf)
- Aileron Regular (Aileron-Regular.otf)
- Dancing Script Regular (DancingScript-Regular.ttf)
- Railway Regular (Railway.ttf)
- Linear Regular (linear-by-braydon-fuller.otf)

{version}
**IMPORTANT:** és possible establir una font personalitzada en molts Widgets, ja sigui a través d'una propietat anomenada **Família de Fonts** o a través de la llista de selecció de **Font** de l'editor visual. Si no tria una font, el Reproductor mostrarà la seva pròpia font predeterminada "sans-serif", referida com la font del sistema. Ex. en Android això és usualment Roboto.

Recomanem sempre triar una font on estigui disponible per evitar que els Reproductors mostrin fonts diferents.{/version}

Gestiona des de la pàgina **Fonts** sota la secció **Administració** del menú principal del CMS.

- Usa el menú de fila per veure els **Detalls** d'una Font i veure un exemple de l'estil de font:

![Font Details](img/v4_tour_settings_fonts.png)

Se poden afegir fonts addicionals fent clic al botó **Pujar Font** i usant l'eina de càrrega de fitxers.

{tip}
Si la nova font no es mostra en l'editor de text després de pujar-la, ¡intenta netejar la memòria cau del navegador!
{/tip}

{version}
**NOTA:** Les fonts tenen preferències integrades en elles conegudes com **etiquetes OS/2**. [[PRODUCTNAME]] busca preferències OS/2 i pot usar **fonts amb etiquetes OS/2 0 o 8**.

Les fonts amb altres etiquetes OS/2 poden produir un error al pujar i poden no mostrar-se correctament.
{/version}

---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Afegeix fitxers de PowerPoint a Llistes de Reproducció i Dissenys usant una de les tres opcions disponibles"
keywords: "preparar powerpoint, preparar reproductors windows, habilitar powerpoint en pantalles"
---

# PowerPoint

Mostra presentacions de PowerPoint seleccionant una de les següents opcions:

## 1. Afegir Vídeo (RECOMANYAT)

Per Reproductors que no siguin Windows / usuaris sense una còpia completa de PowerPoint per instal·lar, des d'Office 2010 en endavant les presentacions de PowerPoint es poden exportar com un fitxer de **Vídeo**. Exporta un fitxer de PowerPoint usant l'opció al menú de fitxer des de dins de l'aplicació de PowerPoint.

{version}
**NOTA:** Si els teus Reproductors són dispositius Android o webOS has d'assegurar-te que el format d'exportació sigui MP4 (PowerPoint 2013 en endavant) o convertir el teu vídeo a MP4 usant una eina de tercers.
{/version}

Continua afegint [Vídeo](media_module_video.html) a les teves Llistes de Reproducció i Dissenys.

## 2. Afegir PDF

Per Reproductors que no siguin Windows / usuaris sense una còpia completa de PowerPoint per instal·lar pots guardar el teu PowerPoint com un fitxer **PDF**.

Continua afegint [PDF](media_module_pdf.html) a les teves Llistes de Reproducció i Dissenys.

## 3. Pujar un fitxer PPT preparat (Només Reproductors Windows)

PowerPoint és un format propietari de Microsoft i només es pot mostrar en un reproductor de senyalització basat en Windows que tingui una còpia completa de Microsoft PowerPoint instal·lada en cada Reproductor Windows. (Si us plau mira la secció [Prepara els teus Reproductors Windows](media_module_powerpoint.html#content-prepare-your-windows-players))

{feat}PowerPoint|v4{/feat}

### Prepara la Presentació de PowerPoint.

PowerPoint, per defecte, posarà barres de desplaçament al costat de la teva presentació, a menys que facis el següent per a cada fitxer de PowerPoint *ABANS* de pujar-lo:

1. Obre el teu Document de PowerPoint
2. Presentació amb diapositives -> Configuració de la presentació
3. En "Tipus de presentació", tria "Examinada de forma individual (finestra)" i després desmarca "Mostrar barra de desplaçament"
4. Fes clic a Acceptar
5. Guarda la Presentació
6. Tingues en compte que [[PRODUCTNAME]] no avançarà les diapositives en una Presentació, per la qual cosa has de gravar els temps de diapositives automàtics anant a "Presentació amb diapositives -> Assajar intervals" i després guardar la presentació.

### Pujar al CMS

Usant la cerca d''altres mitjans', usa el menú desplegable **Tipus** per seleccionar **PowerPoint**:

- Puja fitxers PPT directament a Llistes de Reproducció/Dissenys usant la [Cerca a la Biblioteca](layouts_editor_using_library_search) des de la barra d'eines.

- Els fitxers pujats directament a Llistes de Reproducció i Dissenys es guarden automàticament a la [Biblioteca](media_library.html) per a la seva reutilització.
- Els fitxers de PowerPoint també poden pujar-se per avançat a la Biblioteca.
- Estableix [temps d'inici i fi](media_playlists.html#content-widget-expiry-dates) per fitxers de PowerPoint pujats directament a una Llista de Reproducció.
- Guarda fitxers de PowerPoint en Carpetes al pujar, per controlar fàcilment l'accés als Usuaris.

![PowerPoint](img/v4_media_module_powerpoint.png)

{tip}
¡Una Previsualització per fitxers de PowerPoint no està disponible al CMS!
{/tip}

## Prepara els teus Reproductors Windows

Instal·la PowerPoint al teu PC Windows juntament amb el teu Reproductor [[PRODUCTNAME]] i fes els següents ajustos al Registre de Windows per deshabilitar l'avís de windows a l'obrir PowerPoint. **Si us plau assegura't d'haver pres totes les precaucions necessàries al fer aquests canvis**.

```registry
[HKEY_CLASSES_ROOT\PowerPoint.Show.12]
"BrowserFlags"=dword:00000002
"EditFlags"=dword:00010000

[HKEY_CLASSES_ROOT\PowerPoint.Show.8]
"BrowserFlags"=dword:00000002
"EditFlags"=dword:00010000

[HKEY_CLASSES_ROOT\PowerPoint.SlideShow.12]
"BrowserFlags"=dword:800000a0
"EditFlags"=dword:00010000

[HKEY_CLASSES_ROOT\PowerPoint.SlideShow.8]
"BrowserFlags"=dword:00000002
"EditFlags"=dword:00010000
```

Si no et sents còmode canviant el registre, pot ser possible aconseguir els mateixos resultats esperant que [[PRODUCTNAME]] obri el primer PowerPoint i després quan aparegui la notificació emergent, triar "Obrir" el fitxer, i desmarcar la casella perquè no se et pregunti de nou.

### Habilitar PowerPoint en Pantalles

Necessitaràs assegurar-te que el [Perfil de Configuració de Pantalla](displays_settings) de Windows utilitzat per a les Pantalles en les quals pretens usar PowerPoint, ha d'estar primer habilitat:

- Fes clic en **Configuració de Pantalla** sota la secció **Pantalles** del menú principal del CMS.
- Usa el menú de fila per al Perfil de Pantalla de Windows i selecciona **Editar**.
- Des de la pestanya **General**, marca per **Habilitar PowerPoint**.
- **Guardar**.

### Passos Avançats

Al mostrar PowerPoint, [[PRODUCTNAME]] depèn de Windows i PowerPoint per mostrar el contingut. Això significa que la captura i report d'errors està fora del control de [[PRODUCTNAME]]. Per mitigar qualsevol problema recomanem deshabilitar les notificacions d'error de Windows. Això es pot fer seguint els [passos aquí](https://www.lifewire.com/how-do-i-disable-error-reporting-in-windows-2626074).

Si encara experimentes problemes, també pot ser aconsellable deshabilitar el report d'Errors d'Aplicacions d'Office fusionant el pegat de registre a continuació.

```reg
[HKEY_CURRENT_USER\Software\Policies\Microsoft\Office\11.0\Common]
"DWNeverUpload"=dword:00000001

[HKEY_CURRENT_USER\Software\Policies\Microsoft\Office\10.0\Common]
"DWNeverUpload"=dword:00000001

[HKEY_CURRENT_USER\Software\Policies\Microsoft\Office\12.0\Common]
"DWNeverUpload"=dword:00000001
```

{version}
**NOTA:** El reproductor de Windows mostra la presentació de PowerPoint dins d'un contenidor d'Internet Explorer. Internet Explorer usa el directori
`C:\Users\<user>\AppData\Local\Microsoft\Windows\INetCache\Content.MSO` per emmagatzemar en memòria cau fitxers temporals de Microsoft Office que s'identifiquen com provinents de la zona de seguretat d'Internet. Això pot causar que es guardin múltiples còpies de la presentació en aquest directori amb el temps. Windows no elimina automàticament els duplicats en memòria cau d'aquest directori, el que pot consumir espai d'emmagatzematge en el teu disc dur amb el temps. Si trobes múltiples còpies de la teva presentació en memòria cau en aquest directori és segur eliminar-les.

Recomanem crear una tasca programada o script que elimini el contingut d'aquest directori regularment.
{/version}

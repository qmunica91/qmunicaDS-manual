---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Añade archivos de PowerPoint a Listas de Reproducción y Diseños usando una de las tres opciones disponibles"
keywords: "preparar powerpoint, preparar reproductores windows, habilitar powerpoint en pantallas"
---

# PowerPoint

Muestra presentaciones de PowerPoint seleccionando una de las siguientes opciones:

## 1. Añadir Vídeo (RECOMENDADO)

Para Reproductores que no sean Windows / usuarios sin una copia completa de PowerPoint para instalar, desde Office 2010 en adelante las presentaciones de PowerPoint se pueden exportar como un archivo de **Vídeo**. Exporta un archivo de PowerPoint usando la opción en el menú de archivo desde dentro de la aplicación de PowerPoint.

{version}
**NOTA:** Si tus Reproductores son dispositivos Android o webOS debes asegurarte de que el formato de exportación sea MP4 (PowerPoint 2013 en adelante) o convertir tu vídeo a MP4 usando una herramienta de terceros.
{/version}

Continúa añadiendo [Vídeo](media_module_video.html) a tus Listas de Reproducción y Diseños.

## 2. Añadir PDF

Para Reproductores que no sean Windows / usuarios sin una copia completa de PowerPoint para instalar puedes guardar tu PowerPoint como un archivo **PDF**.

Continúa añadiendo [PDF](media_module_pdf.html) a tus Listas de Reproducción y Diseños.

## 3. Subir un archivo PPT preparado (Solo Reproductores Windows)

PowerPoint es un formato propietario de Microsoft y solo se puede mostrar en un reproductor de señalización basado en Windows que tenga una copia completa de Microsoft PowerPoint instalada en cada Reproductor Windows. (Por favor mira la sección [Prepara tus Reproductores Windows](media_module_powerpoint.html#content-prepare-your-windows-players))

{feat}PowerPoint|v4{/feat}

### Prepara la Presentación de PowerPoint.

PowerPoint, por defecto, pondrá barras de desplazamiento al lado de tu presentación, a menos que hagas lo siguiente para cada archivo de PowerPoint *ANTES* de subirlo:

1. Abre tu Documento de PowerPoint
2. Presentación con diapositivas -> Configuración de la presentación
3. En "Tipo de presentación", elige "Examinada de forma individual (ventana)" y luego desmarca "Mostrar barra de desplazamiento"
4. Haz clic en Aceptar
5. Guarda la Presentación
6. Ten en cuenta que [[PRODUCTNAME]] no avanzará las diapositivas en una Presentación, por lo que debes grabar los tiempos de diapositivas automáticos yendo a "Presentación con diapositivas -> Ensayar intervalos" y luego guardar la presentación.

### Subir al CMS

Usando la búsqueda de 'otros medios', usa el menú desplegable **Tipo** para seleccionar **PowerPoint**:

- Sube archivos PPT directamente a Listas de Reproducción/Diseños usando la [Búsqueda en la Biblioteca](layouts_editor_using_library_search) desde la barra de herramientas.

- Los archivos subidos directamente a Listas de Reproducción y Diseños se guardan automáticamente en la [Biblioteca](media_library.html) para su reutilización.
- Los archivos de PowerPoint también pueden subirse por adelantado a la Biblioteca.
- Establece [tiempos de inicio y fin](media_playlists.html#content-widget-expiry-dates) para archivos de PowerPoint subidos directamente a una Lista de Reproducción.
- Guarda archivos de PowerPoint en Carpetas al subir, para controlar fácilmente el acceso a los Usuarios.

![PowerPoint](img/v4_media_module_powerpoint.png)

{tip}
¡Una Previsualización para archivos de PowerPoint no está disponible en el CMS!
{/tip}

## Prepara tus Reproductores Windows

Instala PowerPoint en tu PC Windows junto con tu Reproductor [[PRODUCTNAME]] y haz los siguientes ajustes en el Registro de Windows para deshabilitar el aviso de windows al abrir PowerPoint. **Por favor asegúrate de haber tomado todas las precauciones necesarias al hacer estos cambios**.

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

Si no te sientes cómodo cambiando el registro, puede ser posible lograr los mismos resultados esperando a que [[PRODUCTNAME]] abra el primer PowerPoint y luego cuando aparezca la notificación emergente, elegir "Abrir" el archivo, y desmarcar la casilla para que no se te pregunte de nuevo.

### Habilitar PowerPoint en Pantallas

Necesitarás asegurarte de que el [Perfil de Configuración de Pantalla](displays_settings) de Windows utilizado para las Pantallas en las que pretendes usar PowerPoint, debe estar primero habilitado:

- Haz clic en **Configuración de Pantalla** bajo la sección **Pantallas** del menú principal del CMS.
- Usa el menú de fila para el Perfil de Pantalla de Windows y selecciona **Editar**.
- Desde la pestaña **General**, marca para **Habilitar PowerPoint**.
- **Guardar**.

### Pasos Avanzados

Al mostrar PowerPoint, [[PRODUCTNAME]] depende de Windows y PowerPoint para mostrar el contenido. Esto significa que la captura y reporte de errores está fuera del control de [[PRODUCTNAME]]. Para mitigar cualquier problema recomendamos deshabilitar las notificaciones de error de Windows. Esto se puede hacer siguiendo los [pasos aquí](https://www.lifewire.com/how-do-i-disable-error-reporting-in-windows-2626074).

Si aún experimentas problemas, también puede ser aconsejable deshabilitar el reporte de Errores de Aplicaciones de Office fusionando el parche de registro a continuación.

```reg
[HKEY_CURRENT_USER\Software\Policies\Microsoft\Office\11.0\Common]
"DWNeverUpload"=dword:00000001

[HKEY_CURRENT_USER\Software\Policies\Microsoft\Office\10.0\Common]
"DWNeverUpload"=dword:00000001

[HKEY_CURRENT_USER\Software\Policies\Microsoft\Office\12.0\Common]
"DWNeverUpload"=dword:00000001
```

{version}
**NOTA:** El reproductor de Windows muestra la presentación de PowerPoint dentro de un contenedor de Internet Explorer. Internet Explorer usa el directorio
`C:\Users\<user>\AppData\Local\Microsoft\Windows\INetCache\Content.MSO` para almacenar en caché archivos temporales de Microsoft Office que se identifican como provenientes de la zona de seguridad de Internet. Esto puede causar que se guarden múltiples copias de la presentación en este directorio con el tiempo. Windows no elimina automáticamente los duplicados en caché de ese directorio, lo que puede consumir espacio de almacenamiento en tu disco duro con el tiempo. Si encuentras múltiples copias de tu presentación en caché en este directorio es seguro eliminarlas.

Recomendamos crear una tarea programada o script que elimine el contenido de ese directorio regularmente.
{/version}

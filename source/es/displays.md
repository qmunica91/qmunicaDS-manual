---
toc: "displays"
maxHeadingLevel: 3
minHeadingLevel: 1
aliases:
  - "displays_fileassociations"
  - "what_is_a_display"      
excerpt: "Las Pantallas son una parte esencial de la cartelería digital que comunican entre el CMS y la App del Reproductor Multimedia"
keywords: "app reproductor, reproductor multimedia, conectar pantallas, autorizar pantallas, transferir pantalla, asignar archivos, asignar diseños"
---

# ¿Qué es una Pantalla?

[[PRODUCTNAME]] le ayuda a mostrar contenido en sus pantallas; tanto si tiene contenido existente como si necesita crear el suyo propio, para mostrar en 1 pantalla o en 100.000, ¡[[PRODUCTNAME]] lo hace fácil!

[[PRODUCTNAME]] utiliza el concepto de Pantallas que son gestionadas desde el CMS para controlar cuándo y cómo se muestra el contenido, así como para proporcionar herramientas de gestión de dispositivos para los Usuarios.

Una **Pantalla** es una parte esencial de la cartelería digital ya que hace de puente de comunicación entre el software **CMS** (Sistema de Gestión de Contenidos) y la **App del Reproductor Multimedia**. 

{nonwhite}

## Vídeo explicativo

{video}9H8Ct00qkqs|how_to_what_is_a_display.png{/video}
{/nonwhite}

La **App del Reproductor** se instala en un **Reproductor Multimedia**, que puede ser un dispositivo de hardware físico separado conectado a una pantalla o un Reproductor Multimedia integrado que se encuentra en monitores de señalización profesional System on Chip (SoC) compatibles. Al instalar la App del Reproductor se genera una clave de hardware que crea un registro único de **Pantalla** en el CMS.

Una vez instalada, la App del Reproductor debe ser **Conectada** al CMS utilizando un **Código** o proporcionando una **Clave CMS**. Una vez conectada, una **Pantalla** será registrada esperando **Autorización** en el CMS antes de convertirse en un dispositivo gestionado y comenzar a mostrar contenido del CMS.

## Creando una Pantalla

1. **Descargue** la App del Reproductor
2. **Instale** en el dispositivo Reproductor. Algunos modelos compatibles System on Chip (SoC) ya tendrán la App del Reproductor instalada.
3. **Conecte** la App del Reproductor al CMS.
4. **Autorice** la Pantalla usando el menú de fila de la página **Pantallas** en el CMS.

La Pantalla se conectará regularmente al CMS para comprobar cualquier información de programación actualizada o cualquier contenido nuevo para descargar. La cuadrícula de Pantallas se actualizará para mostrar el estado, indicar si la Pantalla ha iniciado sesión recientemente, mostrar la fecha y hora de cuándo se accedió a la Pantalla por última vez, etc., para ayudarle a gestionar su red.

{tip}
Cualquier actualización será descargada y guardada en la App del Reproductor. Esto significa que si surgiera un problema de conexión entre la Pantalla y el CMS, la Pantalla continuaría mostrando el contenido programado sin conexión hasta que se restableciera la conexión.
{/tip}

Gestione **Pantallas** desde el CMS y use la gama de herramientas de gestión de dispositivos para controlar eficazmente su red. 

## Lecturas Adicionales

[Configuración de Pantalla](displays_configuration.html)

[Crear Grupos de Pantallas](displays_groups)

[Aplicar configuraciones usando Perfiles de Pantalla](displays_settings)

## Preguntas Frecuentes (FAQs)

***¿Qué Reproductores pueden conectarse al CMS usando un código?***

Todos los Reproductores, en la última versión soportan la conexión mediante un código, con la excepción del Reproductor Linux.

***¿Puedo transferir fácilmente una Pantalla a otro CMS?***

Primero debe asegurarse de que tiene la Autenticación de Dos Factores configurada, desde el Perfil de Usuario para usar Transferir a otro CMS desde el menú de fila de una Pantalla. Se pueden transferir múltiples Pantallas usando la opción Con Seleccionados en la parte inferior de la cuadrícula de Pantallas.

***¿Tienen que coincidir las versiones del Reproductor y el CMS?***

Nuestra recomendación es que su CMS y Reproductores sean de la misma versión mayor para obtener los mejores resultados.

***¿Qué significa Asignar Archivos / Asignar Diseños?***

Los archivos de la Librería y los Diseños pueden ser asignados directamente a una Pantalla para que estén siempre disponibles en la biblioteca local del Reproductor. Esto es útil para precargar un Diseño con antelación cuando el Diseño será usado por alguna integración API para activar un cambio por ejemplo. El contenido aún necesitará ser programado para mostrarse en las Pantallas.

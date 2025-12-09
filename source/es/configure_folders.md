---
toc: "configure"
maxHeadingLevel: 3
minHeadingLevel: 2
alias: "tour_folders"
excerpt: "Crea y Gestiona Carpetas para organizar y controlar fácilmente objetos de Usuario"
keywords: "mover y fusionar carpetas, gestión de carpetas, carpetas de inicio, compartir conteniendo de carpeta, forzar carpeta"
---

# Carpetas

Las Carpetas se usan en todo el CMS y proporcionan una excelente manera de organizar y localizar fácilmente elementos de usuario dentro del CMS. Además, las Carpetas pueden tener opciones de visualización, edición y eliminación aplicadas que se aplicarán a todos los elementos guardados en la Carpeta, convirtiéndolo en una forma eficiente de controlar permisos de Usuario/Grupo de Usuarios para elementos de Usuario.

Se anima a los Administradores a asignar Grupos de Usuarios a sus Usuarios, y luego usar opciones de Compartir Carpeta para dar a estos Usuarios acceso apropiado al contenido de cada uno. Las Carpetas se pueden asignar a nuevos Usuarios desde el asistente de incorporación para asegurar que estén listos desde el principio.

Las Carpetas se gestionan desde la sección de Administración del menú principal del CMS donde los administradores pueden ver información detallada incluyendo con quién se ha compartido la Carpeta y un desglose de su contenido.

{nonwhite}

## Vídeo explicativo

{video}kq0vR4FZuAM|how_to_managing_folders.png{/video}
{/nonwhite}

### Creando Carpetas

Solo los administradores pueden crear **Carpetas** bajo la **Carpeta Raíz**.

- Haz clic derecho en la **Carpeta Raíz** y selecciona **Crear** para añadir una nueva Carpeta al árbol.

- Más opciones están disponibles desde el menú contextual haciendo clic derecho en una Carpeta.

- Configura opciones de **Compartir** Ver, Editar y Eliminar para aplicar a Usuarios/Grupos de Usuarios para Carpetas individuales.

Una vez establecido, todos los elementos contenidos o movidos a esa Carpeta heredarán las opciones aplicadas.

{tip}
Solo los Administradores pueden establecer opciones de Compartir para Carpetas.
Todos los elementos de un artículo que necesitan ser compartidos deben moverse también a la Carpeta. Esto incluye archivos de Medios contenidos en Diseños, y Diseños dentro de Campañas, como ejemplo, si los Usuarios también requieren acceso a esos.
{/tip}

Se puede otorgar acceso a los Usuarios a través de la funcionalidad de **Característica**, para crear subcarpetas bajo carpetas principales a las que se les ha dado acceso.

Las Subcarpetas añadidas a una Carpeta heredarán cualquier opción de Compartir aplicada de la Carpeta Principal.

### Carpeta de Inicio

Asigna una Carpeta de Inicio a Usuarios existentes:

- Ve a **Usuarios** bajo la sección **Administración** del menú principal del CMS.
- Usa el menú de fila y selecciona **Establecer Carpeta de Inicio**.
- Selecciona una Carpeta para usar, o haz clic derecho para crear una nueva Carpeta.

{tip}
Si deseas que el Administrador del Grupo tenga la capacidad de establecer Carpeta de Inicio para Usuarios, ¡asegúrate de que tengan la **Característica** apropiada habilitada!
{/tip}

Si no se selecciona una Carpeta, el nuevo contenido se guardará automáticamente en la ubicación de Carpeta de Inicio predeterminada de un Usuario.

### Forzar Guardado en una Carpeta

Los Administradores pueden prevenir que los Usuarios guarden en la Carpeta Raíz y en su lugar forzarlos a seleccionar una Carpeta antes de guardar deshabilitando el uso de la Carpeta Raíz como predeterminado:

- Navega a **Ajustes** bajo la sección **Administración** del menú principal del CMS.
- Haz clic en la pestaña **Compartir**.

- Desmarca la opción **Permitir guardar en la carpeta raíz**.
- Haz clic en el botón **Guardar** en la parte inferior.

Una vez configurado un Usuario ***debe*** seleccionar una Carpeta nombrada.

### Mover Carpeta

Las Carpetas se pueden mover a otra ubicación de Carpeta y añadirse como una Subcarpeta usando la opción **Mover Carpeta** desde el menú contextual para una Carpeta.

La Carpeta y cualquier subcarpeta contenida se moverán como una nueva subcarpeta dentro de la nueva ubicación de Carpeta manteniendo la estructura de Carpeta original.

Mover una Carpeta que no tiene opciones de Compartir establecidas, heredará cualquier opción de **Compartir** aplicada de la Carpeta de destino.

También puedes seleccionar la opción **Fusionar** para añadir el contenido de la Carpeta original a la ubicación seleccionada, siendo la Carpeta original eliminada del árbol de Carpetas.

## Gestión de Carpetas

Los Administradores pueden ver, crear y gestionar todas las Carpetas del CMS desde la página de Carpetas bajo la sección de Administración del menú principal del CMS.

Esta página de gestión mostrará las Carpetas que han sido compartidas con Usuarios así como el contenido de la carpeta. Al ver subcarpetas desde aquí, solo se mostrarán las opciones de compartir asignadas directamente, las opciones heredadas no se mostrarán.

Como solo las carpetas vacías pueden ser eliminadas, mueve, fusiona o elimina contenidos antes de eliminar la carpeta.

## Lectura Adicional

[Gestionando Etiquetas](configure_tags.html)

## Preguntas Frecuentes

***¿Dónde puedo encontrar el conjunto de Características para Carpetas para configurar para Usuarios/Grupos de Usuarios?***

Las Características se aplican a un Usuario/Grupo de Usuarios usando el menú de fila para un Usuario/Grupo de Usuarios seleccionado.

***¿Qué pasos debo seguir para permitir a los Usuarios la capacidad de Crear sus propias Carpetas?***

1. Habilita **Permitir a los usuarios crear Sub-Carpetas....** desde la pestaña Contenido del conjunto de **Característica de Carpetas**.
2. Habilita **Ver** desde las **opciones de Compartir** para la(s) carpeta(s) principal(es) que pueden tener subcarpetas creadas bajo ellas por el Usuario/Grupo de Usuarios.

***¿Qué pasos debo seguir para permitir a los Usuarios acceso para renombrar Carpetas dentro del menú?***

1. Habilita **Renombrar y Eliminar carpetas existentes** desde la pestaña Contenido en el conjunto de **Característica de Carpetas**.
2. Habilita **Editar** desde las **opciones de Compartir** para la(s) carpeta(s) que pueden ser renombradas por el Usuario/Grupo de Usuarios.

***¿Qué pasos debo seguir para permitir a los Usuarios acceso para eliminar Carpetas del menú?***

1. Habilita **Renombrar y Eliminar Carpetas existentes** desde la pestaña Contenido en el conjunto de **Característica de Carpetas**.
2. Habilita **Eliminar** desde las **opciones de Compartir** para la(s) carpeta(s) que pueden ser eliminadas por el Usuario/Grupo de Usuarios.
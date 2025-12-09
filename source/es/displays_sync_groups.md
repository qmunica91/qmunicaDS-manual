---
toc: "displays"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Los Grupos de Sincronización contienen Pantallas para mostrar contenido sincronizado"
keywords: "contenido sincronizado, puerto de publicación, pantalla líder"
persona: "schedule manager, display manager, administrator"
---

# Grupos de Sincronización

Los Grupos de Sincronización contienen las Pantallas que mostrarán contenido sincronizado. El contenido puede sincronizarse para reproducirse en 2 o más Pantallas en una configuración reflejada o de videowall al programar un [Evento Sincronizado](scheduling_events.html#content-synchronised-events).

{feat}Sync Groups|v4{/feat}

{tip}
Sincroniza Listas de Reproducción en diferentes Diseños usando la **Clave de Sincronización de Contenido**.
{/tip}

Las [Pantallas](displays.html) primero deben asignarse a un **Grupo de Sincronización**:

- Haz clic en **Grupos de Sincronización** bajo la sección **Pantallas** del menú principal del CMS.
- Selecciona el botón **Añadir Grupo de Sincronización**.

![Add Sync Group](img/v4_displays_add_sync_groups.png)

Los Grupos de Sincronización pueden guardarse en Carpetas para controlar fácilmente los niveles de interacción de Usuario/Grupo de Usuarios para las Pantallas, además de proporcionar una forma adicional de organización.

{tip}
Todas las Pantallas en un Grupo de Sincronización necesitan comunicarse usando su dirección IP LAN sobre TCP en el puerto de publicación especificado. Este valor predeterminado es 9590 pero puede cambiarse si ese puerto está reservado.

Recomendamos usar una red cableada y dispositivos de alta potencia similares para la mejor Sincronización.
{/tip}

- Al guardar, usa el formulario **Gestionar Membresía** para seleccionar qué Pantallas incluir en este Grupo.

{version}
**NOTA:** Una Pantalla solo puede pertenecer a un Grupo de Sincronización al mismo tiempo.
{/version}

- Al guardar, usa el formulario Editar y utiliza el menú desplegable para seleccionar qué Pantalla debe ser la **Pantalla Líder** para el Grupo de Sincronización.

- Haz clic en **Guardar**

{tip}
El contenido ahora puede programarse al Grupo de Sincronización haciendo clic en **Programar** desde el menú principal del CMS y seleccionando el botón [Añadir Evento Sincronizado](scheduling_events.html#content-synchronised-events).
{/tip}

## Editar / Gestionar Membresía

Gestiona un Grupo de Sincronización utilizando el menú de fila:

- Selecciona **Editar** para establecer una Pantalla Líder alternativa
- Selecciona **Miembros** para gestionar qué Pantallas son miembros del grupo.

#### Siguiente...

[Programando Eventos Sincronizados](scheduling_events.html#content-synchronised-events)

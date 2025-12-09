---
toc: "users"
maxHeadingLevel: 3
minHeadingLevel: 2
alias: "users_features_and_sharing"
excerpt: "Los Grupos de Usuarios proporcionan una manera fácil de gestionar Características para configurar el acceso al sistema para múltiples Usuarios"
keywords: "grupos preconfigurados, crear grupos de usuarios, miembros de grupo, características, compartir, opciones de compartir, miembros"
---

# Grupos de Usuarios y Características

Los Grupos de Usuarios facilitan la incorporación de nuevos Usuarios y la gestión del acceso al sistema. Los Usuarios que pertenecen a un grupo heredarán cualquier Característica que haya sido habilitada para el Grupo de Usuarios.

{nonwhite}

## Vídeo explicativo

{video}PRioJgzvrEY|how_to_creating_user_groups.png{/video}
{/nonwhite}

## Creando Grupos de Usuarios

Los Grupos de Usuarios se crean y gestionan haciendo clic en **Grupos de Usuarios** bajo la sección **Administración** del menú principal del CMS.

Están disponibles grupos preconfigurados que han sido creados para servir funciones comunes dentro del CMS y tienen las **Características** requeridas ya habilitadas para permitir a los Usuarios realizar su rol.

- Para añadir un nuevo grupo, haz clic en el botón **Añadir Grupo de Usuarios** y completa los campos del formulario.
- **Guardar**.

¡Puedes hacer fácilmente una **Copia** de un Grupo de Usuarios desde el menú de fila y hacer cambios al acceso de **Características** para adaptarse a los requisitos sin la necesidad de crear un nuevo grupo desde cero!

## Miembros

Los Usuarios se añaden a un Grupo de Usuarios usando el menú de fila:

- Haz clic en **Miembros**.
- Selecciona qué **Usuarios** deben pertenecer al Grupo de Usuarios seleccionado.
- **Guardar**.

## Características

Las **Características** controlan lo que un Usuario puede ver y hacer dentro del CMS, restringiendo páginas y funcionalidad de páginas. Cuando se combina con opciones de **Compartir**, las opciones de Ver, Editar y Eliminar para elementos de usuario como Carpetas, Medios, Grupos de Pantallas. Estos conceptos aseguran que solo las partes relevantes del CMS sean visibles para los Usuarios con el nivel apropiado de interacción de Usuario aplicado.

- Las Características se configuran desde el menú de fila para un **Usuario** o **Grupo de Usuarios** y se agrupan en pestañas lógicas.

Se recomienda establecer el acceso a características requerido a grupos de usuarios y añadir usuarios al grupo para heredar Características habilitadas para un flujo de trabajo más fácil y seguro con menos margen de error. Si Usuarios específicos requieren más acceso entonces estos se pueden asignar directamente al Usuario.

Un `-` indica que las Características seleccionadas dentro de ese Conjunto de Características han sido habilitadas.

- Usa la flecha para expandir el Conjunto de Características para ver todas las opciones disponibles.

Una marca indica que todas las Características dentro de ese conjunto están habilitadas.

{tip}
Para que un Usuario tenga la capacidad de Compartir elementos con otros Usuarios, la opción "Permitir capacidades de Compartir para todos los objetos de Usuario" dentro del subconjunto funciones de Usuario de Características de Usuario necesita estar habilitada.
{/tip}

## Lectura Adicional

[Establecer Opciones de Compartir en Carpetas](configure_folders.html)

[Creando Usuarios](users_administration.html)

### Preguntas Frecuentes

***¿Si un Usuario pertenece al Grupo de Usuarios Gestor de Pantallas por qué no pueden añadir y autorizar nuevas Pantallas?***

Esto se considera una función de Administración de alto nivel. Un Admin puede añadir nuevas Pantallas a una Carpeta y dar derechos de acceso a esa Carpeta para que el Grupo Gestor de Pantallas la gestione.

***¿Puede un Usuario pertenecer solo a un Grupo de Usuarios?***

Los Usuarios pueden ser asignados a uno o más Grupos de Usuarios para facilitar el compartir y la colaboración.

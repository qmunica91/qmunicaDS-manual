---
toc: "users"
maxHeadingLevel: 3
minHeadingLevel: 2
aliases:
  - "users"
  - "users_user_types"
  - "users_library_quota" 
  - "users_dashboards"
excerpt: "Gestionar Usuarios del CMS"
keywords: "propiedad, tipos de usuario, super admin, administrador de grupo, asistente de incorporación, carpeta de inicio, añadir usuarios, restablecer autenticación de dos factores, forzar cambio de contraseña, cuota de biblioteca, paneles, página de inicio"
---

# Gestión de Usuarios

[[PRODUCTNAME]] tiene diferentes tipos de Usuarios, cada uno permitiendo un nivel variable de acceso a través del CMS para una colaboración eficiente.

Se anima a los Administradores a asignar **Usuarios** a **Grupos de Usuarios** para determinar a qué deben acceder los Usuarios dentro del CMS y compartir **Carpetas** con el Usuario para controlar la interacción (Ver, Editar, Eliminar) de los elementos contenidos dentro de la Carpeta.

{nonwhite}

## Vídeo explicativo

{video}-sESDKREuY0|how_to_creating_users.png{/video}
{/nonwhite}

## Creando Usuarios

Los Usuarios se crean y gestionan haciendo clic en **Usuarios** bajo la sección **Administración** del menú principal del CMS.

- Para añadir nuevos Usuarios, haz clic en el botón **Añadir Usuario**.

Hay dos formas en las que se pueden añadir Usuarios; a través de un asistente de incorporación usando **Grupos de Usuarios** preconfigurados que han habilitado **Características** para funciones comunes que coincidan con el rol o añadiendo manualmente completando un formulario.

- Sigue el asistente seleccionando un rol para añadirlos a un **Grupo de Usuarios**, crea un **Nombre de Usuario** y **Contraseña** y selecciona cualquier **Carpeta** que necesite ser compartida.
- Si necesitas establecer una **Carpeta de Inicio** para el Usuario, haz clic derecho en una Carpeta y usa la opción de menú **Establecer como Inicio**.

Seleccionar **Crear un usuario manualmente**, abrirá el formulario **Añadir Usuario** para completar.

Un **Usuario** solo tendrá acceso a las partes del CMS asignadas al Grupo de Usuarios al que pertenece, así como derechos completos de edición sobre sus propios elementos y la capacidad de compartir esos con otros Usuarios.

Algunos Usuarios pueden necesitar derechos de acceso adicionales para realizar las tareas correctas, como un **Administrador de Grupo**, quien además de tener acceso a las partes del CMS asignadas al Grupo de Usuarios al que pertenece, también tendrá acceso a todos los elementos de todos los Usuarios que pertenezcan al Grupo de Usuarios.

Los **Tipos de Usuario** se pueden seleccionar al crear un nuevo Usuario manualmente o editando un Usuario existente desde el menú de fila.

A los Usuarios también se les asigna un panel que sirve como **Página de Inicio**:

- El **Panel de Iconos** es la vista de **Usuario** por defecto y está destinado como un lanzador hacia otras áreas del CMS.
- El **Panel de Estado** es una vista de alto nivel para **Usuarios Super Admin** que muestra información relacionada con el uso de Biblioteca y Ancho de Banda así como Actividad de Pantalla.
- El **Panel de Gestor de Medios** da una visión general del estado de los Medios de la Biblioteca en el CMS.
- El **Panel de Lista de Reproducción** solo se asigna al **Grupo de Usuarios de Panel de Lista de Reproducción** que da una vista restringida del CMS con un Usuario solo capaz de seleccionar Listas de Reproducción específicas para gestionar.

Para hacer cambios al predeterminado de un Usuario, usa el menú de fila y selecciona editar y usa el menú desplegable para **Página de Inicio**.

## Eliminando Usuarios

Eliminar un Usuario es irreversible y eliminará todos sus elementos propios incluyendo; Medios, Diseños y Programaciones, incluso si estos elementos están siendo usados por otros Usuarios en el sistema. **Reasigna elementos** a otro Usuario para hacerlos el nuevo propietario de todos los elementos actualmente propiedad del Usuario que deseas eliminar. Alternativamente, usa la casilla de verificación **Retirado** en la parte inferior del formulario **Editar Usuario** para que los elementos permanezcan en uso en el CMS.

{nonwhite}
{cloud}
Por favor asegúrate de que la cuenta de usuario por defecto llamada `xibo_admin` no sea modificada o eliminada para que nuestros agentes de soporte puedan asistirte con tu CMS cuando sea necesario.
{/cloud}
{/nonwhite}

{white}
{cloud}
Por favor asegúrate de que la cuenta de usuario por defecto llamada `cms_admin` no sea modificada o eliminada para que puedas ser asistido con tu CMS cuando sea necesario.
{/cloud}
{/white}

## Lectura Adicional

[Gestionando Carpetas](configure_folders.html)

[Configurando Características](users_groups.html)

## Preguntas Frecuentes

***¿Hay alguna forma de asegurar que los Usuarios cambien su contraseña dentro del sistema?***

Edita un Usuario desde el menú de fila y selecciona la pestaña Opciones para encontrar la configuración "Forzar Cambio de Contraseña". Los Usuarios serán redirigidos a una página para restablecer su contraseña, la próxima vez que inicien sesión.

***¿Tengo un usuario que ha perdido acceso a su aplicación Google Authenticator y no tiene acceso al correo electrónico o códigos de recuperación guardados?***

Edita el Usuario desde el menú de fila y usa la casilla de verificación para Restablecer Autenticación de Dos Factores. El Usuario ahora puede configurar la autenticación de dos factores desde su Perfil de Usuario.

***¿Cómo puedo añadir un Usuario a un Grupo de Usuarios?***

Usa el menú de fila y selecciona Grupos de Usuarios para gestionar la membresía del grupo.

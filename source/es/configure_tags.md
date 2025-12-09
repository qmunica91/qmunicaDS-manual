---
toc: "configure"
maxHeadingLevel: 3
minHeadingLevel: 2
alias: "tour_tags"
excerpt: "Creación y Gestión de Etiquetas usadas en todo el CMS"
keywords: "valores asociados, etiquetas del sistema, valor, requerido, asignando etiquetas, eliminar etiquetas en masa"
---

# Etiquetas

Las Etiquetas se usan en todo el CMS para organizar y categorizar fácilmente elementos para facilitar a los Usuarios su localización y uso. Las Etiquetas actúan como palabras clave o rótulos que cuando se asignan a elementos mejoran la funcionalidad de búsqueda para los Usuarios.

{nonwhite}

## Vídeo explicativo

{video}gHRMKiiXdRA|how_to_managing_tags.png{/video}
{/nonwhite}

Las Etiquetas pueden ser creadas por Usuarios desde varios formularios en todo el CMS, así como creadas y gestionadas por Administradores desde la página de Etiquetas bajo la sección Administración del menú principal del CMS.

Crea y asigna **Etiquetas** a elementos en todo el CMS usando el campo de Etiqueta en los formularios. A medida que se introduce texto, un ayudante de autocompletar mostrará posibles coincidencias para facilitar a los Usuarios ver qué Etiquetas ya están disponibles para seleccionar:

- Selecciona una **Etiqueta** de la lista o crea una nueva escribiendo directamente en el campo de Etiqueta.

Las Etiquetas también pueden ser creadas por Administradores desde la página de **Etiquetas** bajo la sección **Administración** del menú principal del CMS.

- Haz clic en el botón **Añadir Etiqueta** y dale un **Nombre**.

Las Etiquetas opcionalmente pueden tener Valores de Etiqueta asociados con ellas. Por ejemplo, podrías tener una Etiqueta Recepción, con áreas de recepción en múltiples sitios. Estas podrían diferenciarse usando Valores creando una cadena separada por comas de números, 1,2,3.

La casilla de verificación **Valor Requerido** se usa para asegurar que un Usuario ***debe*** seleccionar un Valor para asignar exitosamente la Etiqueta al elemento.

Una vez habilitada, cuando la Etiqueta es seleccionada por Usuarios, cualquier Valor asociado se mostrará para selección. Se mostrará un mensaje de advertencia a los Usuarios que no seleccionen un Valor para avisarles que lo hagan.

Los Usuarios también pueden añadir Valores asociados a Etiquetas usando el campo **Valor de Etiqueta** en los formularios.

Los Administradores pueden ver todas las **Etiquetas del Sistema** desde la página de gestión de Etiquetas y ver informes de Uso usando el menú de fila para cada Etiqueta individual.

Usa la opción **Con Seleccionados** en la parte inferior de la cuadrícula para **Eliminar** Etiquetas en masa.

## Lectura Adicional

[Gestionando Carpetas](configure_folders.html)

## Preguntas Frecuentes

***¿Puedo usar opciones de filtro para excluir Etiquetas de las búsquedas?***

- Ingresa `-Etiqueta` para excluir la etiqueta de los resultados de búsqueda.
- Ingresa `-|Valor` para excluir el valor de los resultados de búsqueda.
- Ingresa `-Etiqueta|Valor` para excluir tanto etiqueta como valor de los resultados de búsqueda.

¡Puedes tener una mezcla separada por comas de todo lo anterior!

- Si quieres mostrar todos los elementos que **no** tienen una etiqueta entonces ingresa `--no-tag`

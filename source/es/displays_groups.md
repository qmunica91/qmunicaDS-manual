---
toc: "displays"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Crea Grupos de Pantallas para facilitar la programación y asignación de multimedia"
keywords: "pertenencia a grupo dinámico, añadir grupo de pantallas"
---

# Grupos de Pantallas

Agrupa **Pantallas** específicas para permitir que el contenido y las programaciones abarquen múltiples Pantallas con un solo **Evento** configurado, ahorrando tiempo y reduciendo errores. Agrupar Pantallas hace que sea más fácil gestionar una red en expansión. Simplemente añade **Pantallas** recién conectadas a un **Grupo de Pantallas** existente para heredar programaciones y comenzar a mostrar contenido rápidamente.

Agrupa Pantallas por industria o ubicación para facilitar la actualización y segmentación de contenido que difiere por áreas o propósito.

Los Grupos de Pantallas pueden contener una mezcla de **Pantallas** singulares así como otros **Grupos de Pantallas** para permitirte apuntar fácilmente a las Pantallas correctas para mostrar tu contenido.

Por ejemplo, podrías tener Pantallas ubicadas dentro de tiendas en diferentes niveles, destinadas a alcanzar diferentes audiencias, por lo que podrías tener Grupos de Pantallas que contengan:

- Todas las Pantallas en tienda A
- Todas las Pantallas en tienda B
- Todas las Pantallas que dan a la calle
- Todas las Pantallas en nivel 1
- Todas las Pantallas en nivel 2
- Todas las Pantallas internas
- Todas las Pantallas externas

**Crea Grupos de Pantallas** y asigna automáticamente **Pantallas** con criterios coincidentes **dinámicamente** o selecciona **manualmente** la pertenencia a la Pantalla.

- Haz clic en Añadir Grupo de Pantallas desde la cuadrícula de Grupos de Pantallas.

## Grupos Dinámicos

Para asignar miembros dinámicamente, marca la casilla **Grupo Dinámico**.
- Establece los **criterios de filtro** a usar en el formato de expresiones separadas por comas regulares o comparaciones de cadenas simples. 
- Prefija las expresiones con un `-` para excluir de los filtros. Por ejemplo, todas las Pantallas que contienen `a` pero no `b` en el nombre serían `a, -b`
- Las **Etiquetas de Criterio** también se pueden filtrar usando filtros OR/AND adicionales para Pantallas con múltiples Etiquetas asignadas.

## Grupos Manuales

Para asignar miembros manualmente, deja la casilla sin marcar y haz clic para Guardar el formulario:

- Usa el menú de fila para el nuevo registro de Grupo de Pantallas y selecciona **Miembros** usando la casilla de verificación para cada Pantalla.

El Árbol de Relaciones muestra los ancestros y descendientes. Los Grupos de Pantallas Padre, mostrados arriba del Grupo seleccionado pasarán su programación a los grupos de Pantallas debajo.

## Grupos Anidados

Los Grupos de Pantallas pueden anidarse para simplificar la programación permitiendo que los subgrupos hereden permisos de un grupo padre.

## Lecturas Adicionales

[Configurando Pantallas](displays_configuration)

[Grupos de Sincronización](displays_sync_groups)

[Configuraciones de Perfil de Pantalla](displays_settings)

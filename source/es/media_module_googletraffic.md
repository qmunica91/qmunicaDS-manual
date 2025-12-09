---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Muestra datos con una clave API de Google Maps"
---

# Tráfico de Google

Muestra datos de tráfico configurados con una clave API de Google Maps en Diseños y Listas de Reproducción.

{version}
**IMPORTANTE:** Este Módulo requiere una clave API de Google que tiene cargos de uso asociados. Por favor asegúrate de estar al tanto de los cargos de uso antes de ingresar tu clave en la configuración de este Módulo.
{/version}

{feat}Google Traffic Maps|v4{/feat}

## Instalación

El Módulo de Tráfico de Google debe configurarse con una clave API de Google Maps antes de usar. La documentación "[get a key](https://developers.google.com/maps/documentation/javascript/get-api-key)" describe el proceso y las diferencias entre las claves.

El Módulo de Tráfico de Google se instala desde la página **Módulos** bajo la sección **Administración** del menú principal del CMS.

- Haz clic en el botón **Instalar Módulo** y selecciona el Módulo para instalar.
- Después de la instalación, selecciona el Módulo de la cuadrícula y usa el menú de fila para seleccionar **Editar**.

- Completa los campos del formulario e incluye la **clave API**.

Este formulario también contiene configuraciones para proporcionar una **duración por defecto** y una **duración mínima**. Por favor asegúrate de entender estas dos configuraciones y configurarlas de una manera adecuada para tu entorno.

{version}
**IMPORTANTE:** La API de Google se cobra por carga de mapa y, por lo tanto, cuánto tiempo permanece el Widget en pantalla tiene una relación directa con los cargos que acumularás.
{/version}

{tip}
Hasta que se ingrese una clave API, el Widget no se renderizará en el Editor de Diseños o el Reproductor, aunque aún puedes añadir el Widget a tus Diseños.

Este Módulo requiere una **conexión a internet válida** en el Reproductor para funcionar.
{/tip}

Los términos de uso de la API de Google Maps deben leerse y entenderse antes de usar este Módulo. En el momento de escribir esto, estos términos se pueden encontrar [aquí](https://developers.google.com/maps/terms).

## Descripción General

- Ingresa la Latitud y Longitud a usar.

- Usa la Ubicación de Pantalla para usar la Latitud y Longitud registradas para una Pantalla.

- Reutiliza fácilmente 1 Diseño en múltiples Pantallas para mostrar el tráfico en la ubicación correcta para cada Pantalla usando la configuración de Ubicación de Pantalla.

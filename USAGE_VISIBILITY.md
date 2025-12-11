# Guía Definitiva: Publicación y Visibilidad

## 1. CONTROLAR QUÉ SE PUBLICA
Edita `visibility.json`:
*   `"public"`: Visible para **todos**.
*   `"full"`: Visible **SOLO** en la web completa (Intranet).
*   `"draft"`: **OCULTO**.

## 2. GENERAR LA WEB (Un Clic)
Ejecuta:
```bash
./build.sh
```
Esto creará una CÓPIA MAESTRA en la carpeta `output/public`.
*   La web pública está en la raíz.
*   La intranet está escondida en la carpeta `/full`.

## 3. PUBLICAR (Hostinger) - ¡Muy Fácil!

1.  **Subir Archivos**:
    *   Sube **SOLO** el contenido de `output/public` a tu hosting (carpeta `public_html`).
    *   ¡Ya está! No tienes que subir dos carpetas separadas.

2.  **Proteger la Intranet (Contraseña)**:
    *   Entra en tu panel de Hostinger (hpanel).
    *   Busca **"Directorios Protegidos"** (Directory Privacy).
    *   Selecciona la carpeta `public_html/full`.
    *   Ponle un usuario y contraseña (ej. "admin" / "manual").

¡Listo!
*   Entra a `manual.qmunica.com` -> Web Pública.
*   Entra a `manual.qmunica.com/full` -> Te pedirá contraseña -> Web Completa.

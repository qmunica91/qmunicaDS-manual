---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Incrusta HTML i Javascript per mostrar en Dissenys i Llistes de Reproducció"
keywords: "contingut de precàrrega, CSS, etiquetes de capçalera de script"
---

# Contingut Incrustat (Embedded Content)

Incrusta HTML i JavaScript per ser mostrat en Dissenys i Llistes de Reproducció.

{feat}Embedded HTML|v4{/feat}

## Descripció General

- Fes millores personalitzades sense modificar l'aplicació principal.
- Per contingut amb un fons transparent marca per mostrar el Widget amb un fons transparent.
- Escala contingut amb el Disseny.
- Precàrrega contingut fora de pantalla.

- Ingressa text o HTML per incrustar.
- Usa un full d'estil CSS per controlar l'estil visual.
- Inclou etiquetes `script` per incrustar contingut al HEAD del document. (Si us plau mira la secció a continuació).

{version}
**NOTA:**

- Fons transparent i Escala està disponible en Windows des de v2 R253.

- Precàrrega fora de pantalla està actualment només disponible des d'Android v2 R207.

{/version}

### Contingut HEAD per Incrustar

JavaScript ha d'estar embolicat en etiquetes `script`. [[PRODUCTNAME]] afegirà automàticament jQuery.

El mètode `EmbedInit()` serà cridat pel Reproductor i es pot usar per iniciar de forma segura qualsevol JavaScript personalitzat en el moment apropiat. El mètode està predeterminat en qualsevol nou Element de mitjans Incrustat.

```html
<script type="text/javascript">
function EmbedInit()
{
    // Init es cridarà quan aquesta pàgina es carregui en el client.

    return;
}
</script>
```

{tip}
Mostra HTML incrustat amb contingut Active-X en un Reproductor Windows, amb la configuració de seguretat d'IE, perquè els fitxers locals puguin executar contingut actiu per defecte. Això es pot fer en Eines -> Opcions d'Internet -> Avançat -> Seguretat -> "Permetre que el contingut actiu s'executi en fitxers en El Meu PC".
{/tip}

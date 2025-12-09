---
toc: "configure"
maxHeadingLevel: 3
minHeadingLevel: 2
alias: "tour_folders"
excerpt: "Crea i Gestiona Carpetes per organitzar i controlar fàcilment objectes d'Usuari"
keywords: "moure i fusionar carpetes, gestió de carpetes, carpetes d'inici, compartir contingut de carpeta, forçar carpeta"
---

# Carpetes

Les Carpetes s'usen en tot el CMS i proporcionen una manera excel·lent d'organitzar i localitzar fàcilment elements d'usuari dins del CMS. A més, les Carpetes poden tenir opcions de visualització, edició i eliminació aplicades que s'aplicaran a tots els elements guardats en la Carpeta, convertint-lo en una forma eficient de controlar permisos d'Usuari/Grup d'Usuaris per a elements d'Usuari.

Es recomana als Administradors assignar Grups d'Usuaris als seus Usuaris, i després usar opcions de Compartir Carpeta per donar a aquests Usuaris accés apropiat al contingut de cadascun. Les Carpetes es poden assignar a nous Usuaris des de l'assistent d'incorporació per assegurar que estiguin llestos des del principi.

Les Carpetes es gestionen des de la secció d'Administració del menú principal del CMS on els administradors poden veure informació detallada incloent amb qui s'ha compartit la Carpeta i un desglossament del seu contingut.

{nonwhite}

## Vídeo explicatiu

{video}kq0vR4FZuAM|how_to_managing_folders.png{/video}
{/nonwhite}

### Creant Carpetes

Només els administradors poden crear **Carpetes** sota la **Carpeta Arrel**.

- Fes clic dret en la **Carpeta Arrel** i selecciona **Crear** per afegir una nova Carpeta a l'arbre.

- Més opcions estan disponibles des del menú contextual fent clic dret en una Carpeta.

- Configura opcions de **Compartir** Veure, Editar i Eliminar per aplicar a Usuaris/Grups d'Usuaris per a Carpetes individuals.

Un cop establert, tots els elements continguts o moguts a aquesta Carpeta heretaran les opcions aplicades.

{tip}
Només els Administradors poden establir opcions de Compartir per a Carpetes.
Tots els elements d'un article que necessiten ser compartits han de moure's també a la Carpeta. Això inclou fitxers de Mitjans continguts en Dissenys, i Dissenys dins de Campanyes, com a exemple, si els Usuaris també requereixen accés a aquests.
{/tip}

Es pot atorgar accés als Usuaris a través de la funcionalitat de **Característica**, per crear subcarpetes sota carpetes principals a les quals se'ls ha donat accés.

Les Subcarpetes afegides a una Carpeta heretaran qualsevol opció de Compartir aplicada de la Carpeta Principal.

### Carpeta d'Inici

Assigna una Carpeta d'Inici a Usuaris existents:

- Ves a **Usuaris** sota la secció **Administració** del menú principal del CMS.
- Usa el menú de fila i selecciona **Establir Carpeta d'Inici**.
- Selecciona una Carpeta per usar, o fes clic dret per crear una nova Carpeta.

{tip}
Si desitges que l'Administrador del Grup tingui la capacitat d'establir Carpeta d'Inici per a Usuaris, ¡assegura't que tinguin la **Característica** apropiada habilitada!
{/tip}

Si no se selecciona una Carpeta, el nou contingut es guardarà automàticament en la ubicació de Carpeta d'Inici predeterminada d'un Usuari.

### Forçar Guardat en una Carpeta

Els Administradors poden prevenir que els Usuaris guardin en la Carpeta Arrel i en el seu lloc forçar-los a seleccionar una Carpeta abans de guardar deshabilitant l'ús de la Carpeta Arrel com predeterminat:

- Navega a **Configuració** sota la secció **Administració** del menú principal del CMS.
- Fes clic en la pestanya **Compartir**.

- Desmarca l'opció **Permetre guardar en la carpeta arrel**.
- Fes clic al botó **Guardar** a la part inferior.

Un cop configurat un Usuari ***ha de*** seleccionar una Carpeta nomenada.

### Moure Carpeta

Les Carpetes es poden moure a una altra ubicació de Carpeta i afegir-se com una Subcarpeta usant l'opció **Moure Carpeta** des del menú contextual per a una Carpeta.

La Carpeta i qualsevol subcarpeta continguda es mouran com una nova subcarpeta dins de la nova ubicació de Carpeta mantenint l'estructura de Carpeta original.

Moure una Carpeta que no té opcions de Compartir establertes, heretarà qualsevol opció de **Compartir** aplicada de la Carpeta de destí.

També pots seleccionar l'opció **Fusionar** per afegir el contingut de la Carpeta original a la ubicació seleccionada, sent la Carpeta original eliminada de l'arbre de Carpetes.

## Gestió de Carpetes

Els Administradors poden veure, crear i gestionar totes les Carpetes del CMS des de la pàgina de Carpetes sota la secció d'Administració del menú principal del CMS.

Aquesta pàgina de gestió mostrarà les Carpetes que han estat compartides amb Usuaris així com el contingut de la carpeta. Al veure subcarpetes des d'aquí, només es mostraran les opcions de compartir assignades directament, les opcions heretades no es mostraran.

Com només les carpetes buides poden ser eliminades, mou, fusiona o elimina continguts abans d'eliminar la carpeta.

## Lectura Addicional

[Gestionant Etiquetes](configure_tags.html)

## Preguntes Freqüents

***On puc trobar el conjunt de Característiques per a Carpetes per configurar per a Usuaris/Grups d'Usuaris?***

Les Característiques s'apliquen a un Usuari/Grup d'Usuaris usant el menú de fila per a un Usuari/Grup d'Usuaris seleccionat.

***Quins passos he de seguir per permetre als Usuaris la capacitat de Crear les seves pròpies Carpetes?***

1. Habilita **Permetre als usuaris crear Sub-Carpetes....** des de la pestanya Contingut del conjunt de **Característica de Carpetes**.
2. Habilita **Veure** des de les **opcions de Compartir** per a la(s) carpeta(s) principal(s) que poden tenir subcarpetes creades sota elles per l'Usuari/Grup d'Usuaris.

***Quins passos he de seguir per permetre als Usuaris accés per reanomenar Carpetes dins del menú?***

1. Habilita **Reanomenar i Eliminar carpetes existents** des de la pestanya Contingut en el conjunt de **Característica de Carpetes**.
2. Habilita **Editar** des de les **opcions de Compartir** per a la(s) carpeta(s) que poden ser reanomenades per l'Usuari/Grup d'Usuaris.

***Quins passos he de seguir per permetre als Usuaris accés per eliminar Carpetes del menú?***

1. Habilita **Reanomenar i Eliminar Carpetes existents** des de la pestanya Contingut en el conjunt de **Característica de Carpetes**.
2. Habilita **Eliminar** des de les **opcions de Compartir** per a la(s) carpeta(s) que poden ser eliminades per l'Usuari/Grup d'Usuaris.
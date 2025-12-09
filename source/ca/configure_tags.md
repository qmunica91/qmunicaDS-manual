---
toc: "configure"
maxHeadingLevel: 3
minHeadingLevel: 2
alias: "tour_tags"
excerpt: "Creació i Gestió d'Etiquetes usades en tot el CMS"
keywords: "valors associats, etiquetes del sistema, valor, requerit, assignant etiquetes, eliminar etiquetes en massa"
---

# Etiquetes

Les Etiquetes s'usen en tot el CMS per organitzar i categoritzar fàcilment elements per facilitar als Usuaris la seva localització i ús. Les Etiquetes actuen com paraules clau o rètols que quan s'assignen a elements milloren la funcionalitat de cerca per als Usuaris.

{nonwhite}

## Vídeo explicatiu

{video}gHRMKiiXdRA|how_to_managing_tags.png{/video}
{/nonwhite}

Les Etiquetes poden ser creades per Usuaris des de diversos formularis en tot el CMS, així com creades i gestionades per Administradors des de la pàgina d'Etiquetes sota la secció Administració del menú principal del CMS.

Crea i assigna **Etiquetes** a elements en tot el CMS usant el camp d'Etiqueta en els formularis. A mesura que s'introdueix text, un ajudant d'autocompletar mostrarà possibles coincidències per facilitar als Usuaris veure quines Etiquetes ja estan disponibles per seleccionar:

- Selecciona una **Etiqueta** de la llista o crea una nova escrivint directament en el camp d'Etiqueta.

Les Etiquetes també poden ser creades per Administradors des de la pàgina d'**Etiquetes** sota la secció **Administració** del menú principal del CMS.

- Fes clic al botó **Afegir Etiqueta** i dóna-li un **Nom**.

Les Etiquetes opcionalment poden tenir Valors d'Etiqueta associats amb elles. Per exemple, podries tenir una Etiqueta Recepció, amb àrees de recepció en múltiples llocs. Aquestes podrien diferenciar-se usant Valors creant una cadena separada per comes de números, 1,2,3.

La casella de verificació **Valor Requerit** s'usa per assegurar que un Usuari ***ha de*** seleccionar un Valor per assignar exitosament l'Etiqueta a l'element.

Un cop habilitada, quan l'Etiqueta és seleccionada per Usuaris, qualsevol Valor associat es mostrarà per a selecció. Es mostrará un missatge d'advertència als Usuaris que no seleccionin un Valor per avisar-los que ho facin.

Els Usuaris també poden afegir Valors associats a Etiquetes usant el camp **Valor d'Etiqueta** en els formularis.

Els Administradors poden veure totes les **Etiquetes del Sistema** des de la pàgina de gestió d'Etiquetes i veure informes d'Ús usant el menú de fila per a cada Etiqueta individual.

Usa l'opció **Amb Seleccionats** a la part inferior de la quadrícula per **Eliminar** Etiquetes en massa.

## Lectura Addicional

[Gestionant Carpetes](configure_folders.html)

## Preguntes Freqüents

***Puc usar opcions de filtre per excloure Etiquetes de les cerques?***

- Ingressa `-Etiqueta` per excloure l'etiqueta dels resultats de cerca.
- Ingressa `-|Valor` per excloure el valor dels resultats de cerca.
- Ingressa `-Etiqueta|Valor` per excloure tant etiqueta com valor dels resultats de cerca.

¡Pots tenir una barreja separada per comes de tot l'anterior!

- Si vols mostrar tots els elements que **no** tenen una etiqueta llavors ingressa `--no-tag`

---
toc: "scheduling"
maxHeadingLevel: 3
minHeadingLevel: 2
alias: "layouts_overlay"
excerpt: "Crea un Disseny de Superposició que un cop programat s'asseurà damunt d'altres Dissenys en la programació"
keywords: "mostrar damunt de contingut existent"
---

# Dissenys de Superposició

Un Disseny de Superposició es mostrarà damunt d'altres Dissenys un cop Programat.

{tip}
Els Dissenys de Superposició també poden Programar-se per usar-se amb Dissenys dins d'una [Campanya de Llista de Dissenys](scheduling_layout_list_campaign.html).
{/tip}

Els Dissenys de Superposició romanen a dalt mentre el teu contingut programat normal canvia a sota. Això és particularment útil per a logotips, informació important o avisos d'emergència, per exemple.

![Overlay Layout](img/v4_layouts_overlay.png)

## Crear un Disseny de Superposició

Els Dissenys de Superposició es creen exactament de la mateixa manera que tots els altres **Dissenys**. Afegeix contingut perquè s'ajusti al voltant dels teus dissenys existents perquè el teu Disseny de Superposició pugui "seure damunt" d'altres Dissenys que estan **Programats** al mateix temps que la Superposició. El teu Disseny de Superposició mostrarà tot el seu contingut important mentre els Dissenys "a sota" es reprodueixen en rotació.

{tip}
[[PRODUCTNAME]] no renderitzarà el fons en els Reproductors quan un Disseny es programa com un Disseny de Superposició.
{/tip}

{version}
**NOTA:** Els Dissenys que contenen Widgets / Multimèdia que usen el navegador Edge no es poden usar amb un Disseny de Superposició ja que el contingut no pot seure damunt d'altre contingut sota aquestes circumstàncies. Això inclouria HLS i YouTube Integrat. Si el seu contingut no és un vídeo llavors el navegador CEF es pot usar en el seu lloc.
{/version}

Els Dissenys de Superposició es comporten d'una manera diferent als Dissenys quan es programen i només renderitzaran el contingut multimèdia una vegada, per la qual cosa no mostraran cap contingut actualitzat.

Si el teu Disseny de Superposició inclou contingut que necessita ser actualitzat, com Widgets de Calendari o Ticker per exemple, s'ha d'afegir una Llista de Reproducció al Disseny i incloure els mitjans a la Llista de Reproducció. Llavors, quan carregui el següent element en la Llista de Reproducció, recarregarà els altres elements per mostrar contingut actualitzat.

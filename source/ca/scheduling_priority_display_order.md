---
toc: "scheduling"
maxHeadingLevel: 3
minHeadingLevel: 1
alias: "schedule_management"
excerpt: "Estableix l'ordre de reproducció i la importància dels esdeveniments al programar contingut"
keywords: "tipus d'esdeveniment, anul·lar programacions, limitar nombre de reproduccions, executar a l'hora del cms"
---

# Usant Prioritat i Ordre de Visualització

[[PRODUCTNAME]] té una sèrie d'eines de programació per permetre la creació simple de programacions a través d'una o més Pantalles/Grups de Pantalles. Aquestes eines permeten als usuaris definir l'ordre dels elements programats per adaptar com s'ha de mostrar el contingut, així com marcar Esdeveniments d'alta prioritat per mostrar-los a la part superior de les llistes de programació.

## Prioritat

La Prioritat empeny el contingut important al capdavant de qualsevol programació existent i anul·la tots els altres esdeveniments no prioritaris del mateix Tipus d'Esdeveniment (Dissenys/Campanyes/Vídeo/Imatges i Llistes de Reproducció) en la programació.

Les Programacions amb una prioritat més alta tenen precedència sobre aquelles amb prioritats més baixes, sent 0 considerada la més baixa.

Per exemple, podries tenir un anunci important amb informació sobre una prova d'alarma d'incendis que ha de ser l'única cosa que es mostri en les Pantalles en un moment específic. Assignar la Prioritat més alta a aquest Esdeveniment asseguraria que sigui l'únic contingut que es mostri.

A l'arribar a l'hora de finalització de l'esdeveniment prioritari, la programació normal es reprendrà en les pantalles.

## Ordre de Visualització

Usa Ordre de Visualització per determinar l'ordre de reproducció de múltiples Esdeveniments que s'han programat per mostrar-se al mateix temps.

L'ordre és una classificació numèrica simple, de números més baixos a més alts, els Esdeveniments marcats amb un 1 es reproduiran abans que qualsevol Esdeveniment marcat amb un 2 per exemple.

Deixar el camp Ordre de Visualització en blanc predeterminarà a l'ordre en què es va afegir l'Esdeveniment per primera vegada.

{tip}
**NOTA:** Per assegurar que els Dissenys es reprodueixin en un ordre definit recomanem afegir-los i ordenar-los en una Campanya de Llista de Dissenys. L'Ordre de Visualització es pot usar llavors per determinar l'ordre en què les Campanyes completes han de reproduir-se.

Si les Campanyes de Llista de Dissenys tenen el mateix Ordre de Visualització establert o aquest camp es deixa en blanc, els Dissenys assignats a la Campanya de Llista de Dissenys es reproduiran d'acord amb l'**ordre de Llista de Reproducció** establert.
{/tip}

### Màxim de Reproduccions per Hora

Existeix una configuració addicional al programar Esdeveniments per limitar el nombre de vegades que l'Esdeveniment ha de mostrar-se per hora en les Pantalles. Podries tenir una Imatge promocional que només s'ha de mostrar una vegada per hora per exemple.

- Estableix un número aquí o deixa-ho com 0 per reproduccions il·limitades.

## Lectures Addicionals

[Establint un ordre de Llista de Reproducció per a una Campanya](scheduling_layout_list_campaign.html)

[Mostrant una seqüència de contingut en una Llista de Reproducció](getting_started_showing_a_playlist.html)

## Preguntes Freqüents

***Què es considera el mateix Tipus d'Esdeveniment per Prioritat?***

Dissenys/Campanyes/Imatges/Vídeos i Llistes de Reproducció es tractaran com el mateix Tipus d'Esdeveniment al tenir en compte les Prioritats.

***Què passaria si marqués la casella Executar a l'hora del CMS per a un esdeveniment?***

Amb això marcat, l'hora de l'Esdeveniment seria determinada per l'hora del CMS en lloc d'usar l'hora local de la Pantalla per a les Pantalles seleccionades.

Escenari:

- Hora CMS = GMT
- Pantalla 1 = GMT
- Pantalla 2 = GMT -4

Si un esdeveniment es va programar per començar a les 11:00hrs, el contingut començaria a mostrar-se en aquestes Pantalles a les 11:00hrs segons les seves zones horàries. Aquestes dues Pantalles no mostraran el mateix contingut al mateix temps ja que la Pantalla 2 està 4 hores darrere de la Pantalla 1.

Si es va marcar Executar a l'hora del CMS, la Pantalla 1 començarà a mostrar a les 11:00hrs, ja que està en la mateixa zona horària que el CMS. La Pantalla 2 començarà a mostrar contingut a les 07:00hrs ja que està 4 hores darrere de la zona horària del CMS.

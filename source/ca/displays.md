---
toc: "displays"
maxHeadingLevel: 3
minHeadingLevel: 1
aliases:
  - "displays_fileassociations"
  - "what_is_a_display"      
excerpt: "Les Pantalles són una part essencial de la cartelleria digital que comuniquen entre el CMS i l'App del Reproductor Multimèdia"
keywords: "app reproductor, reproductor multimèdia, connectar pantalles, autoritzar pantalles, transferir pantalla, assignar fitxers, assignar dissenys"
---

# Què és una Pantalla?

[[PRODUCTNAME]] l'ajuda a mostrar contingut en les seves pantalles; tant si té contingut existent com si necessita crear el seu propi, per mostrar en 1 pantalla o en 100.000, ¡[[PRODUCTNAME]] ho fa fàcil!

[[PRODUCTNAME]] utilitza el concepte de Pantalles que són gestionades des del CMS per controlar quan i com es mostra el contingut, així com per proporcionar eines de gestió de dispositius per als Usuaris.

Una **Pantalla** és una part essencial de la cartelleria digital ja que fa de pont de comunicació entre el programari **CMS** (Sistema de Gestió de Continguts) i l'**App del Reproductor Multimèdia**. 

{nonwhite}

## Vídeo explicatiu

{video}9H8Ct00qkqs|how_to_what_is_a_display.png{/video}
{/nonwhite}

L'**App del Reproductor** s'instal·la en un **Reproductor Multimèdia**, que pot ser un dispositiu de maquinari físic separat connectat a una pantalla o un Reproductor Multimèdia integrat que es troba en monitors de senyalització professional System on Chip (SoC) compatibles. En instal·lar l'App del Reproductor es genera una clau de maquinari que crea un registre únic de **Pantalla** al CMS.

Un cop instal·lada, l'App del Reproductor ha de ser **Connectada** al CMS utilitzant un **Codi** o proporcionant una **Clau CMS**. Un cop connectada, una **Pantalla** serà registrada esperant **Autorització** al CMS abans de convertir-se en un dispositiu gestionat i començar a mostrar contingut del CMS.

## Creant una Pantalla

1. **Descarregui** l'App del Reproductor
2. **Instal·li** en el dispositiu Reproductor. Alguns models compatibles System on Chip (SoC) ja tindran l'App del Reproductor instal·lada.
3. **Connecti** l'App del Reproductor al CMS.
4. **Autoritzi** la Pantalla usant el menú de fila de la pàgina **Pantalles** al CMS.

La Pantalla es connectarà regularment al CMS per comprovar qualsevol informació de programació actualitzada o qualsevol contingut nou per descarregar. La quadrícula de Pantalles s'actualitzarà per mostrar l'estat, indicar si la Pantalla ha iniciat sessió recentment, mostrar la data i hora de quan es va accedir a la Pantalla per última vegada, etc., per ajudar-lo a gestionar la seva xarxa.

{tip}
Qualsevol actualització serà descarregada i desada a l'App del Reproductor. Això significa que si sorgís un problema de connexió entre la Pantalla i el CMS, la Pantalla continuaria mostrant el contingut programat sense connexió fins que es restablís la connexió.
{/tip}

Gestioni **Pantalles** des del CMS i utilitzi la gamma d'eines de gestió de dispositius per controlar eficaçment la seva xarxa. 

## Lectures Addicionals

[Configuració de Pantalla](displays_configuration.html)

[Crear Grups de Pantalles](displays_groups)

[Aplicar configuracions usant Perfils de Pantalla](displays_settings)

## Preguntes Freqüents (FAQs)

***Quins Reproductors poden connectar-se al CMS usant un codi?***

Tots els Reproductors, en l'última versió suporten la connexió mitjançant un codi, amb l'excepció del Reproductor Linux.

***Puc transferir fàcilment una Pantalla a un altre CMS?***

Primer ha d'assegurar-se que té l'Autenticació de Dos Factors configurada, des del Perfil d'Usuari per usar Transferir a un altre CMS des del menú de fila d'una Pantalla. Es poden transferir múltiples Pantalles usant l'opció Amb Seleccionats a la part inferior de la quadrícula de Pantalles.

***Han de coincidir les versions del Reproductor i el CMS?***

La nostra recomanació és que el seu CMS i Reproductors siguin de la mateixa versió major per obtenir els millors resultats.

***Què significa Assignar Fitxers / Assignar Dissenys?***

Els fitxers de la Llibreria i els Dissenys poden ser assignats directament a una Pantalla perquè estiguin sempre disponibles a la biblioteca local del Reproductor. Això és útil per precarregar un Disseny amb antelació quan el Disseny serà usat per alguna integració API per activar un canvi per exemple. El contingut encara necessitarà ser programat per mostrar-se a les Pantalles.

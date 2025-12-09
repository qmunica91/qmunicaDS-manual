---
toc: "widgets"
maxHeadingLevel: 3
minHeadingLevel: 2
alias: "media_module_agenda"
excerpt: "Mostra esdeveniments de Calendari extrets d'un feed iCal"
keywords: "feed ical"
---

# Calendari

Mostra esdeveniments de Calendari extrets d'un feed iCal en qualsevol lloc d'un Disseny usant **Elements** o selecciona una **Plantilla Estàtica** per mostrar resultats en Dissenys/Llistes de Reproducció.

{feat}Calendar View|v4{/feat}

Les dades del Calendari són proporcionades per un feed iCal que alimentarà els Elements configurats i les Plantillas Estàtiques.

{tip}
Assegura't que la URL del feed ICS estigui disponible per al CMS. Si el feed es carrega en un navegador sense autenticació, llavors el feed hauria de mostrar-se al CMS sense problemes.

Per més informació sobre com veure el teu Google Calendar en aplicacions, usa el següent enllaç seleccionant l'opció **Obtenir el teu calendari (només vista)**: https://support.google.com/calendar/answer/37648?hl=es
{/tip}

## Elements de Calendari

Els Elements estan disponibles per selecció al afegir el Widget de Calendari a un [Disseny](layouts_editor.html) per donar als Usuaris més control sobre quins components del Widget de Calendari usar i on es poden col·locar.

![Calendar Elements](img/v4_media_modules_calendar_elements.png)

Cada Element té un conjunt d'opcions de configuració en el Panell de Propietats. Ingressa el feed iCal per usar per retornar resultats des de la pestanya **Configurar**.

Controla com els articles han de ciclar-se especificant una [Ranura de Dades](https://test.xibo.org.uk/manual/en/layouts_editor.html#content-data-slots) per usar per a cadascun dels Elements afegits. Els Elements de Dades poden complementar-se encara més afegint Elements Globals per afegir formes i text que es poden posar en un Grup d'Elements per a una configuració i posicionament més fàcils.

Aprofita les Plantilles (Stencils) per afegir un grup predissenyat d'Elements al teu Disseny.

{tip}
¡Tots els Elements en la Plantilla es tracten com 'un' quan es configuren i es poden duplicar fàcilment amb un clic dret!
{/tip}

## Plantilles Estàtiques de Calendari

Les Plantilles Estàtiques defineixen com han d'organitzar-se i estilitzar-se els resultats retornats i són una manera simple de mostrar les teves dades usant plantilles preestilitzades.

![Calendar Elements](img/v4_media_modules_calendar_templates.png)

Les Plantilles es poden configurar per fer canvis en l'aparença del disseny usant una gamma d'opcions en el Panell de Propietats. Ingressa un iCal per retornar resultats des de la pestanya **Configurar** per a cada Plantilla afegida al Disseny/Llista de Reproducció.

## Descripció General

- Retorna esdeveniments dins d'un rang de dates especificat.
- Opcions per excloure esdeveniments de tot el dia i actuals del feed perquè no es mostrin.
- Usar zones horàries d'esdeveniments i calendari.
- Establir durada per element.
- Especificar quants esdeveniments mostrar.
- Executar un disparador de Web Hook quan es detectin certes condicions.
- Les dades per a aquest mitjà són emmagatzemades en memòria cau pels Reproductors per reproducció fora de línia.

### Disparadors de Web Hook

Dispara una [Acció](layouts_interactive_actions.html) de Web Hook quan hi ha un **Esdeveniment Actual** o **Sense Esdeveniment** des de la pestanya Disparador.

{tip}
**Escenari d'Exemple**:

Un usuari té un calendari de sala de reunions configurat usant el Widget de Calendari en un Disseny que mostra l'ocupació actual per una sala i voldria canviar els llums LED per mostrar quan està vacant o en ús.

- L'usuari primer necessitaria crear [Comandaments de Shell](displays_command_functionality.html#content-shell-commands) que emetessin comandaments a un dispositiu LED IoT o als LED integrats en algunes de les Pantalles Comercials de Philips.
- A continuació, una [Acció Interactiva](layouts_interactive_actions.html) necessitaria definir-se en el **Disseny**, que **Navegaria a Widget** i **Apuntaria a la Pantalla**, amb el [Widget de Comandament de Shell.](media_module_shellcommand.html)
- Des de la pestanya **Disparador**, assigna els codis per disparar els **Web Hooks** per **Esdeveniment Actual** i **Sense Esdeveniment**.

{/tip}

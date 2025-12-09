---
toc: "scheduling"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Crea una Campanya Publicitària amb programació automàtica basada en criteris establerts"
keywords: "cost per reproducció, impressions per reproducció, prova de reproducció"
---

# Campanyes Publicitàries

Crea Campanyes Publicitàries on [[PRODUCTNAME]] calcularà quantes reproduccions es necessiten per satisfer els criteris ingressats i gestionarà la programació automàticament per tu.

{tip}
¡Habilita la funció **Accés a Campanyes Publicitàries** per a cada Usuari/Grup d'Usuaris que hagi de tenir accés complet a aquesta funció!
{/tip}

## Crear una Campanya Publicitària

Fes clic en **Campanyes** sota la secció **Disseny** del menú principal del CMS:

- Fes clic al botó **Afegir Campanya** a la part superior de la quadrícula.

- Selecciona **Campanya Publicitària** des del menú desplegable i completa els camps del formulari:

![Add Ad Campaign](img/v4_layouts_campaign_add_ad_campaign.png)

Les Carpetas s'usen per organitzar, cercar i Compartir objectes d'Usuari fàcilment amb altres Usuaris/Grups d'Usuaris. Les Campanyes Publicitàries guardades en una Carpeta heretaran les opcions d'accés aplicades a aquesta Carpeta.

{tip}
¡Si els usuaris també han de tenir accés als Dissenys/Contingut de Disseny, assegura't que això també es guardi en la mateixa Carpeta!
{/tip}

- Dóna a la teva Campanya Publicitària un **Nom** per a una identificació fàcil en el CMS incloent Etiquetes opcionals.

{tip}
¡Etiquetes i Carpetes també es poden assignar a múltiples Campanyes usant l'opció **Amb Seleccionats** a la part inferior de la quadrícula de Campanyes!
{/tip}

- Usa el menú desplegable per establir el **Tipus d'Objectiu** per aquesta Campanya Publicitària com **Reproduccions**, **Pressupost** o **Impressions**.
- Inclou el número **Objectiu** total per aquesta Campanya Publicitària en relació amb el seu Tipus d'Objectiu seleccionat.

- Fes clic en **Guardar**.

A continuació, s'han d'establir els criteris per permetre a [[PRODUCTNAME]] calcular la freqüència de reproducció.

- Des de la quadrícula, usa el menú de fila per la **Campanya Publicitària** i selecciona **Editar**:

![Edit Ad Campaign](img/v4_campaigns_edit_ad_campaign.png)

- Proporciona Dates i Hores d'**Inici** i **Fi** per la Campanya Publicitària. (Aquesta informació és requerida i **no pot** deixar-se en blanc)
- Selecciona de les **Pantalles** i **Grups de Pantalles** disponibles per reproduir aquesta Campanya Publicitària. (Aquesta informació és requerida i **no pot** deixar-se en blanc)

{tip}
¡Assegura't que les Pantalles tinguin els **Detalls de Pantalla** ingressats correctament per a les Pantalles seleccionades que reprodueixen aquesta Campanya Publicitària, assegurant que els camps **Cost per reproducció** i **Impressions per reproducció** s'hagin completat!
{/tip}

- Fes clic en **Guardar**.

{tip}
¡La **Prova de Reproducció** necessita configurar-se en **ON** per a totes les Pantalles/Grups de Pantalles seleccionats aquí, per assegurar informes precisos i reproduccions!
{/tip}

- Assigna un Disseny usant el menú desplegable **Afegir Disseny**.

Un cop que se selecciona un Disseny, hi ha més opcions de programació disponibles:

![Assign Layouts Ad Campaign](img/v4_campaigns_assign_layouts_ad_campaign.png)

- Selecciona quins **Dies de la Setmana** ha d'estar actiu aquest Disseny en aquesta Campanya Publicitària.

- Tria de [Particions del Dia](scheduling_dayparting.html) existents si aquest Disseny només s'ha de mostrar en moments predefinits seleccionats.

{tip}
Les Campanyes Publicitàries poden incloure múltiples instàncies del mateix Disseny amb diferents Particions del Dia assignades si és necessari.

Per exemple, si necessites mostrar el mateix Disseny per a una partició del dia 'Matí' definida així com una partició del dia 'Nit' definida, ¡afegeix el Disseny dues vegades i defineix les particions del dia requerides individualment per a cadascun!
{/tip}

- Dibuixa àrees en el mapa per proporcionar reproduccions basades en **geo tanques** per a qualsevol pantalla mòbil, amb contingut per mostrar a l'entrar en una àrea definida.

{tip}
¡Pots tenir múltiples àrees definides en el mateix mapa!
{/tip}

- Fes clic en **Guardar**.

El Disseny s'afegirà a la Campanya que es pot editar/eliminar si és necessari usant el menú de fila:

![View Ad Campaigns](img/v4_campaigns_view_added_ad_campaigns.png)

Continua construint la teva Campanya Publicitària seleccionant Dissenys i definint opcions de programació.

{tip}
¡La **Prova de Reproducció** necessita configurar-se en **ON** per a tots els Dissenys afegits a la Campanya Publicitària per assegurar informes precisos i reproduccions!
{/tip}

[[PRODUCTNAME]] programarà automàticament per complir amb els criteris de reproducció requerits per assolir els Objectius ingressats.

Les Campanyes Publicitàries es poden veure en la **Programació** com entrades bloquejades que no es poden editar des del propi programador.

**Agenda** es pot usar per veure una vista de reproducció més detallada de la Campanya Publicitària i previsualitzar els Dissenys inclosos.

El progrés de la Campanya Publicitària es mostrarà en la quadrícula de Campanyes i a l'obrir la Campanya Publicitària, sempre que la Prova de Reproducció s'hagi configurat en ON per a totes les Pantalles i Dissenys seleccionats per a la Campanya. Així com els camps Cost per reproducció i Impressions per reproducció completats per a totes les Pantalles seleccionades.

{version}
**NOTA**: Si s'omet la informació anterior, els informes no poden actualitzar-se per reflectir Reproduccions, Despesa, Impressions i Objectiu, els quals mostraran un valor de 0. La Campanya Publicitària en si també intentarà posar-se al dia per augmentar l'Objectiu, la qual cosa resultarà en què els Dissenys es reprodueixin cada cop amb més freqüència fins que sigui l'únic contingut mostrat per complir amb l'objectiu.
{/version}

![Ad Campaign Grid](img/v4_campaigns_ad_campaign_grid.png)

{tip}
La pestanya Referència es pot usar per proporcionar informació de referència per a la Campanya seleccionada. Un cop afegida, aquesta informació es pot veure en la quadrícula de Campanyes i a través de l'API.
{/tip}

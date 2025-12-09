---
toc: "media"
maxHeadingLevel: 3
minHeadingLevel: 2
alias: "media_module_menu_board"
excerpt: "Crea i Gestiona informació de Taulers de Menú"
keywords: "categories, productes, opcions de producte"
---

 # Taulers de Menú (Menu Boards)

La interfície de Taulers de Menú proporciona una manera senzilla perquè els usuaris creïn i gestionin informació de 'categories' i 'productes' independentment dels Dissenys. Un cop creats, les dades del Tauler de Menú es poden afegir en qualsevol lloc d'un Disseny usant Elements dels Widgets [Tauler de Menú: Categoria](media_module_menuboards_category.html) i [Tauler de Menú: Productes](media_module_menuboards_products.html) disponibles en l'[Editor de Dissenys.](layouts_editor.html)

{version}
**Nota:** ¡Els Widgets de Tauler de Menú no estan disponibles per afegir a una Llista de Reproducció!
{/version}

## Resum de Característiques

- Crear i definir Categories.
- Incloure informació detallada del producte.
- Seleccionar Imatges per usar des de la teva Biblioteca.
- Mantenir contingut sense accedir a Dissenys.
- Reutilitzar a través de múltiples Widgets/Dissenys.

Els Taulers de Menú es creen i gestionen independentment dels Dissenys i, per tant, no requereixen accés d'usuari a Dissenys o a l'Editor de Dissenys per afegir o gestionar categories/dades de productes continguts en un Tauler de Menú.

## Creant un Tauler de Menú

Els Taulers de Menú es creen i gestionen seleccionant **Taulers de Menú** sota la secció **Biblioteca** del menú principal del CMS:

![Menu Board](img/v4_media_menuboards_grid.png)

- Selecciona el botó **Afegir Tauler de Menú** i completa els camps del formulari per crear un nou registre:

![Menu Board Add](img/v4_media_menuboards_add.png)

- Dóna al teu Tauler de Menú un **Nom** per a una identificació fàcil al CMS. Proporciona una **Descripció** interna opcional i ingressa un **Codi** si fas referència a aquest Tauler de Menú a través de l'API.

- Fes clic en **Guardar**.

## Crear i Configurar Categories

Les categories defineixen l'estructura de les teves dades:

- Usa el menú de fila per a un registre de Tauler de Menú i selecciona **Veure Categories**.

![Menu Board row menu](img/v4_media_menuboards_row_menu.png)

Fes clic al botó **Afegir Categoria** i completa els camps del formulari requerits:

![Add Category](img/v4_media_menuboards_add_category.png)

{tip}
**Codi** és per a ús avançat al fer referència a l'API.
{/tip}

- Fes clic en **Següent** per repetir aquest procés i afegir les **Categories** requerides per al Tauler de Menú.
- Selecciona **Guardar** a l'ingressar l'última Categoria a usar.

## Afegir Productes

Les dades del producte s'afegeixen a les Categories per proporcionar tota la informació clau que es pot seleccionar per mostrar-se en Pantalles.

- Usa el menú de fila per a una Categoria i selecciona **Veure Productes**:

![Products](img/v4_media_menuboards_products.png)

- Crea noves dades de Producte fent clic al botó **Afegir Producte** i completa tots els camps del formulari rellevants:

![Add Products](img/v4_media_menuboards_add_product.png)

{tip}
¡El Widget [Taulers de Menú: Productes](media_module_menuboards_products.html) es pot configurar per atenuar productes que estan marcats com no disponibles per mostrar en Pantalles!
{/tip}

### Opcions de Producte

Usa aquesta pestanya per proporcionar més opcions de producte:

![Product Options](img/v4_media_menuboards_product_options.png)

{tip}
Usa Opcions per proporcionar ofertes especials, gangues limitades, etc., per a aquest producte en particular.
{/tip}

- Repeteix el procés per afegir més Productes/Opcions de Producte a la Categoria.

{tip}
¡Cada Categoria es mostrarà com una pestanya separada en la quadrícula de Productes perquè puguis canviar fàcilment entre Categories per afegir i editar informació del producte!
{/tip}

![Product Tabs](img/v4_media_menuboards_product_tabs.png)

Fes clic en **Veure Categories** per tornar a la quadrícula de Categories per veure i editar les existents usant el menú de fila o **Afegir Categoria**.

Les dades del Tauler de Menú s'afegeixen a Dissenys usant el Widget [Tauler de Menú: Categoria](media_module_menuboards_category.html) que té elements de dades que s'usen principalment per afegir informació de 'encapçalament' i el Widget [Tauler de Menú: Productes](media_module_menuboards_products.html) que permet una col·locació precisa dels detalls del Producte en Dissenys.

{tip}
Els Taulers de Menú s'editen independentment dels Dissenys, per la qual cosa no hi ha necessitat d'accedir o editar el(s) Disseny(s) als quals s'ha afegit el Tauler de Menú. ¡Els canvis estaran disponibles en el sistema immediatament llestos per ser recollits pels Reproductors en la seva pròxima recol·lecció, sense necessitat de fer cap edició als Dissenys!
{/tip}

{nonwhite}
Fes un cop d'ull a la nostra guia per veure un exemple de com utilitzar Taulers de Menú per a les teves Pantalles: [Usant Taulers de Menú](https://community.xibo.org.uk/t/utilising-menu-boards-in-v4/30749)
{/nonwhite}

#### Següent...

[Afegir Disseny](layouts_editor.html)

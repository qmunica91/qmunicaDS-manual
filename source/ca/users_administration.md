---
toc: "users"
maxHeadingLevel: 3
minHeadingLevel: 2
aliases:
  - "users"
  - "users_user_types"
  - "users_library_quota" 
  - "users_dashboards"
excerpt: "Gestionar Usuaris del CMS"
keywords: "propietat, tipus d'usuari, super admin, administrador de grup, assistent d'incorporació, carpeta d'inici, afegir usuaris, restablir autenticació de dos factors, forçar canvi de contrasenya, quota de biblioteca, panells, pàgina d'inici"
---

# Gestió d'Usuaris

[[PRODUCTNAME]] té diferents tipus d'Usuaris, cadascun permetent un nivell variable d'accés a través del CMS per a una col·laboració eficient.

S'anima als Administradors a assignar **Usuaris** a **Grups d'Usuaris** per determinar a què han d'accedir els Usuaris dins del CMS i compartir **Carpetes** amb l'Usuari per controlar la interacció (Veure, Editar, Eliminar) dels elements continguts dins de la Carpeta.

{nonwhite}

## Vídeo explicatiu

{video}-sESDKREuY0|how_to_creating_users.png{/video}
{/nonwhite}

## Creant Usuaris

Els Usuaris es creen i gestionen fent clic en **Usuaris** sota la secció **Administració** del menú principal del CMS.

- Per afegir nous Usuaris, fes clic al botó **Afegir Usuari**.

Hi ha dues formes en què es poden afegir Usuaris; a través d'un assistent d'incorporació usant **Grups d'Usuaris** preconfigurats que han habilitat **Característiques** per a funcions comunes que coincideixin amb el rol o afegint manualment completant un formulari.

- Segueix l'assistent seleccionant un rol per afegir-los a un **Grup d'Usuaris**, crea un **Nom d'Usuari** i **Contrasenya** i selecciona qualsevol **Carpeta** que necessiti ser compartida.
- Si necessites establir una **Carpeta d'Inici** per a l'Usuari, fes clic dret en una Carpeta i usa l'opció de menú **Establir com a Inici**.

Seleccionar **Crear un usuari manualment**, obrirà el formulari **Afegir Usuari** per completar.

Un **Usuari** només tindrà accés a les parts del CMS assignades al Grup d'Usuaris al qual pertany, així com drets complets d'edició sobre els seus propis elements i la capacitat de compartir aquests amb altres Usuaris.

Alguns Usuaris poden necessitar drets d'accés addicionals per realitzar les tasques correctes, com un **Administrador de Grup**, qui a més de tenir accés a les parts del CMS assignades al Grup d'Usuaris al qual pertany, també tindrà accés a tots els elements de tots els Usuaris que pertanyin al Grup d'Usuaris.

Els **Tipus d'Usuari** es poden seleccionar al crear un nou Usuari manualment o editant un Usuari existent des del menú de fila.

Als Usuaris també se'ls assigna un panell que serveix com a **Pàgina d'Inici**:

- El **Panell d'Icones** és la vista d'**Usuari** per defecte i està destinat com un llançador cap a altres àrees del CMS.
- El **Panell d'Estat** és una vista d'alt nivell per a **Usuaris Super Admin** que mostra informació relacionada amb l'ús de Biblioteca i Ample de Banda així com Activitat de Pantalla.
- El **Panell de Gestor de Mitjans** dóna una visió general de l'estat dels Mitjans de la Biblioteca al CMS.
- El **Panell de Llista de Reproducció** només s'assigna al **Grup d'Usuaris de Panell de Llista de Reproducció** que dóna una vista restringida del CMS amb un Usuari només capaç de seleccionar Llistes de Reproducció específiques per gestionar.

Per fer canvis al predeterminat d'un Usuari, usa el menú de fila i selecciona editar i usa el menú desplegable per a **Pàgina d'Inici**.

## Eliminant Usuaris

Eliminar un Usuari és irreversible i eliminarà tots els seus elements propis incloent; Mitjans, Dissenys i Programacions, fins i tot si aquests elements estan sent usats per altres Usuaris en el sistema. **Reassigna elements** a un altre Usuari per fer-los el nou propietari de tots els elements actualment propietat de l'Usuari que desitges eliminar. Alternativament, usa la casella de verificació **Retirat** a la part inferior del formulari **Editar Usuari** perquè els elements romanguin en ús al CMS.

{nonwhite}
{cloud}
Si us plau assegura't que el compte d'usuari per defecte anomenat `xibo_admin` no sigui modificat o eliminat perquè els nostres agents de suport puguin assistir-te amb el teu CMS quan sigui necessari.
{/cloud}
{/nonwhite}

{white}
{cloud}
Si us plau assegura't que el compte d'usuari per defecte anomenat `cms_admin` no sigui modificat o eliminat perquè puguis ser assistit amb el teu CMS quan sigui necessari.
{/cloud}
{/white}

## Lectura Addicional

[Gestionant Carpetes](configure_folders.html)

[Configurant Característiques](users_groups.html)

## Preguntes Freqüents

***Hi ha alguna forma d'assegurar que els Usuaris canviïn la seva contrasenya dins del sistema?***

Edita un Usuari des del menú de fila i selecciona la pestanya Opcions per trobar la configuració "Forçar Canvi de Contrasenya". Els Usuaris seran redirigits a una pàgina per restablir la seva contrasenya, la pròxima vegada que iniciïn sessió.

***Tinc un usuari que ha perdut accés a la seva aplicació Google Authenticator i no té accés al correu electrònic o codis de recuperació guardats?***

Edita l'Usuari des del menú de fila i usa la casella de verificació per Restablir Autenticació de Dos Factors. L'Usuari ara pot configurar l'autenticació de dos factors des del seu Perfil d'Usuari.

***Com puc afegir un Usuari a un Grup d'Usuaris?***

Usa el menú de fila i selecciona Grups d'Usuaris per gestionar la pertinença del grup.

---
toc: "media"
maxHeadingLevel: 3
minHeadingLevel: 2
excerpt: "Característica comercial per mostrar de forma segura serveis de panell de control"
keywords: "connector, microsoft power bi, grafana, matomo"
---

# Servei de Panell (Dashboard Service)

{white}
Si desitges aprofitar aquesta funció, si us plau contacta al teu Administrador.
{/white}

{nonwhite}
El Servei de Panells de Xibo és una característica comercial que permet als Usuaris mostrar de forma segura serveis de panell; Microsoft Power BI, Grafana i Matomo, en Dissenys amb automatització i autenticació manejades per Xibo.

**Tingues en compte:** Aquesta característica comercial requereix una API per configuració com s'explica més endavant [aquí](/pricing#dashboards).

Un cop que el Connector ha estat configurat, afegeix panells per mostrar en Dissenys usant el [Widget de Panells](/manual/ca/media_module_dashboard.html)

## Configurar Connector

Des del CMS:

- Fes clic en **Aplicacions** sota la secció **Administració** del menú principal.
- Desplaça't cap avall fins a la secció **Connectors** de la pàgina.
- Fes clic al botó **Configurar** per al connector **Xibo** **Dashboard Service**:

![Dashboard Connector](img/v4_media_dashboard_connector.png)

- Ingressa la clau API que se t'ha donat (disponible en [El Meu Compte](/login)).

{tip}
¡Els clients en un Pla de Negocis o Empresarial tindran la seva clau API preemplenada!
{/tip}

- Marca per **Habilitar** per començar a proporcionar els serveis de panell

![Configure Connector](img/v4_media_dashboard_configure_connector.png)

- Fes clic en **Guardar.**

- Fes clic al botó **Configurar** novament per al connector de servei de Panell de Xibo.
- Usant la secció **Credencials** del formulari, selecciona el(s) servei(s) de panell que desitges usar:

![Dashboard Credentials](img/v4_media_dashboard_credentials.png)

Ingressa les següents credencials:

- Nom d'usuari
- Contrasenya
- Secret de Dos Factors (si és necessari)
- URL (si és necessari)

{tip}
Grafana no admet autenticació de múltiples factors, així que si us plau deixa el camp **Secret de Dos Factors** **buit** al configurar aquesta integració.

Si us plau mira la següent pàgina per més informació sobre com obtenir una URL per usar amb aquest servei, mecanismes d'autenticació suportats i possibles limitacions [Xibo Dashboard Service](/docs/setup/xibo-dashboard-service)
{/tip}

- Fes clic en **Guardar** i espera uns moments mentre aquestes credencials es registren exitosament.

El teu Panell està llest per ser afegit a Dissenys usant el [Widget de Panell](/manual/ca/media_module_dashboard.html)
{/nonwhite}
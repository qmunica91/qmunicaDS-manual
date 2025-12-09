---
toc: "configure"
maxHeadingLevel: 3
minHeadingLevel: 2
alias: "tour_transitions"
excerpt: "Opcions de Gestió de Transicions per a Usuaris"
keywords: "predeterminats de transició, fosa d'entrada, fosa de sortida, volar, transicions de llista de reproducció, transicions de sortida"
---

# Gestió de Transicions

{feat}Transitions|v4{/feat}

{version}

**Nota:** Les transicions no són compatibles amb Reproductors Tizen per als següents Widgets:

- [Vídeo](media_module_video.html)
- [Entrada de Vídeo](media_module_video_in.html)
- [Vídeo Local](media_module_localvideo.html)

{/version}

Les transicions es gestionen des de la pàgina **Transicions** sota la secció **Administració** del menú principal del CMS. Configura quines Transicions han d'estar disponibles per als Usuaris per a assignació a elements de Mitjans:

![Transitions Grid](img/v4_tour_transitions_grid.png)

- **Fosa d'Entrada (Fade In)** - Augmenta Opacitat de 0 a 100.
- **Fosa de Sortida (Fade Out)** - Disminueix Opacitat de 100 a 0.
- **Volar (Fly)** - Volar cap a dins o fora en un punt cardinal.

## Predeterminats de Transició

{version}
Els valors predeterminats globals es poden establir per a Transicions per Administradors des de la pàgina de [Ajustos del CMS](tour_cms_settings.html#content-defaults).
{/version}

Les Transicions Predeterminades es poden habilitar fàcilment per a tots els Widgets afegits a un Disseny marcant la casella **Aplicar Transicions automàticament?** des del panell de propietats del Disseny:

![Transitions Layout](img/v4_tour_transitions_layout.png)

{version}

**NOTA:** Quan s'han aplicat Predeterminats de Transició, els camps de Transició del Widget es mostraran com entrades en blanc:

![Transitions Widget](img/v4_tour_transitions_widget.png)

Això és perquè només les Transicions ingressades **manualment** per a un Widget es mostraran en els camps del formulari.
{/version}

## Transicions de Llista de Reproducció

Aquestes són les Transicions entre **elements de Mitjans** en una [Llista de Reproducció](media_playlists.html) i s'estableixen com transicions d'**Entrada** i **Sortida**.

{tip}
El formulari de Transició s'adapta depenent de la Transició seleccionada i les opcions disponibles per a aquesta transició. En la majoria dels casos és necessari seleccionar una durada per a la Transició en Milisegons i en el cas de Volar, també s'ha de seleccionar una direcció.
{/tip}

## Transició de Sortida de Llista de Reproducció

Una Transició de Sortida de Llista de Reproducció ocorre quan l'últim Element de Mitjans que es mostra en una [Llista de Reproducció](media_playlists.html) es mostra i permet establir una Transició de Sortida diferent.
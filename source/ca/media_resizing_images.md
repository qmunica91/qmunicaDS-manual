<!--toc=media-->

# Canvi de Mida d'Imatges (Resizing Images)

{version}
**Nota:** Aquesta característica està disponible des de v2.2.0
{/version}

Es poden especificar llindars i límits per defecte que després es consideren en el cas que una imatge s'hagi de redimensionar. Això podria ser al pujar una imatge o una imatge sent descarregada per un Widget - NASA RSS en un Widget Ticker per exemple.

Les configuracions es poden configurar des de la pàgina **Configuració** sota la secció **Administració** del menú principal del CMS.

- Fes clic a la pestanya **Predeterminats**:

![Resizing Images](img/v3_media_resizing_images.png)

## Llindar de Redimensionament

- Estableix un llindar màxim (basat en el costat més llarg) que s'ha de considerar per redimensionar una imatge.

{tip}
Si estableixes un Llindar de Redimensionament de 1920 i puges/descarregues una imatge que és 800, aquesta imatge no necessitaria redimensionar-se. Si puges/descarregues una imatge que fos 2400, aquesta es redimensionaria llavors a 1920.
{/tip}

## Límit de Redimensionament

- Estableix un límit (basat en el costat més llarg) per a imatges pujades/descarregades. Les imatges que excedeixin aquest límit no es processaran i s'han de reemplaçar amb una altra imatge que estigui dins del límit.

Aquesta configuració determinarà si el fitxer d'imatge és massa gran per ser processat.
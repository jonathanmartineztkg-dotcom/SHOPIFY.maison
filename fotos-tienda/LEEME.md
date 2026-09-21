# Fotos de modelo — las que entraron a la tienda

> **Estado al 21/9: las 6 ya están subidas a la tienda**, con su texto alternativo y asignadas a
> las variantes de su color. Lo de abajo queda como registro de qué es cada una y de lo que falta.

Son las fotos que estaban en la raíz del repo (`Photorealistic Short(NN).png` y
`model_reclining_podium_cyan_leopard_shorts.png`), **sin el sello "Ai"** que traían en la esquina
superior izquierda, recortadas a 4:5 y en el tamaño que acepta Shopify.

Los originales quedan en la raíz, sin tocar, por si hace falta volver a empezar.

## Qué es cada una

| Archivo | Color del catálogo | Pose | Tamaño |
|---|---|---|---|
| `maison-short-leopardo-cafe-modelo-frente.jpg` | Café | De pie, de frente | 3277×4096 |
| `maison-short-leopardo-cafe-modelo-espalda.jpg` | Café | De pie, de espaldas | 3276×4096 |
| `maison-short-leopardo-rosa-modelo-banco.jpg` | Rosa | Sentada en banco | 3276×4096 |
| `maison-short-leopardo-purpura-modelo.jpg` | Púrpura | De pie, brazos arriba | 3276×4096 |
| `maison-short-leopardo-gris-negro-modelo.jpg` | Gris Negro | Apoyada en la pared | 3276×4096 |
| `maison-short-leopardo-cian-modelo.jpg` | Cian | Recostada sobre cubo | 1843×2304 |

Los colores están confirmados **contra las fotos limpias que ya están en la tienda**, no a ojo:
el púrpura es `purpura` y no `azul`, y el gris es `gris-negro` (manchas casi negras) y no
`gris-claro` ni `gris-oscuro`.

## Lo que hay que saber antes de subirlas

- **3277×4096 = 13,4 MP.** Shopify rechaza arriba de 20 MP, así que las originales
  (5568×6912 = 38,5 MP) **no se pueden subir tal cual**. Por eso están en este tamaño.
- **La de cian es la más chica** (1843×2304). Sirve, pero tiene menos de la mitad de resolución que
  las otras. Si se puede regenerar más grande, mejor.
- **El fondo no es el mismo que el de las fotos limpias.** Estas tienen fondo blanco frío
  (entre `#E9E7E8` y `#F4F2F6`); las fotos de producto de la tienda tienen crema `#F5EFEA`, que es
  el que combina con el fondo de la tienda (`--mm-paper #fdf9f8`). En la galería se va a notar el
  salto. Es media hora de trabajo emparejarlos; queda pendiente de decidir.

## Cómo entran en el cambio 1 de `05-proximos-cambios.md`

El cambio 1 ("al elegir un color, que aparezca primero una modelo con ese color") necesita que cada
foto lleve el nombre del color en el **texto alternativo**. Estaban las 10 vacías; **ya se cargaron
los 16 textos** (estos 6 más los 10 que ya estaban). Los que quedaron:

| Foto | Texto alternativo |
|---|---|
| café frente | `Short de leopardo color Café, vista con modelo` |
| café espalda | `Short de leopardo color Café, vista de espaldas con modelo` |
| rosa | `Short de leopardo color Rosa, vista con modelo` |
| púrpura | `Short de leopardo color Púrpura, vista con modelo` |
| gris negro | `Short de leopardo color Gris Negro, vista con modelo` |
| cian | `Short de leopardo color Cian, vista con modelo` |

A las 8 fotos limpias que ya estaban se les cargó el suyo con el mismo criterio:
`Short de leopardo color Azul, foto de producto`, y así con cada color.

**Hecho:** la foto de modelo quedó asignada a las 4 tallas de cada uno de los 5 colores que la
tienen — 20 variantes. Azul, gris claro y gris oscuro siguen con su foto limpia, así que las 32
variantes tienen foto y se cumple el requisito de `05-proximos-cambios.md`
(`updateMedia` no hace nada si una variante no tiene foto).

**Queda pendiente decidir:** café y rosa ahora tienen **dos** fotos de modelo cada uno (la vieja de
1600×2000 y la nueva). Cuando se programe el filtro por color habrá que quedarse con una, porque el
plan dice dos fotos por color: modelo + limpia.

## Lo que todavía falta

Quedan **3 colores sin foto de modelo**: **Azul**, **Gris claro** y **Gris oscuro**.
Hasta tenerlas, el filtro de galería por color solo se puede encender para los 5 colores que sí la
tienen, o hay que dejar la foto limpia como primera para los que faltan.

Para que peguen con estas: fondo claro y parejo, formato 4:5, cuerpo entero, la misma modelo si se
puede, y **sin el sello "Ai"** (o avisar y se le quita acá, como a estas).

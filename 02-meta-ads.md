# Meta Ads

## Cuenta

| Dato | Valor |
|---|---|
| Cuenta publicitaria | `1511851970599751` — "CP - MAISON - HOLANDA" |
| Portafolio comercial | `888159824276269` — Maison Meszarics |
| Página de Facebook | `1030473910154205` |
| Instagram | `@maisonmeszarics` — 3.489 seguidores, 18 publicaciones |
| Píxel | `996412940009765` |
| Zona horaria | **Europe/Amsterdam** → el día de Meta cierra a las **16:00 de México** (19:00 de Argentina) |
| Moneda | USD |

## Campaña activa

| Entidad | ID | Estado |
|---|---|---|
| Campaña "MX · Shorts Leopardo · Video vs Estáticos" | `120252740568350725` | Activa, fin **27/9 23:59** (Ámsterdam) |
| Grupo **Estáticos** — MX Mujeres 18-45 | `120252740574710725` | **Activo**, ~$6,30/día |
| Grupo Video | `120252740576790725` | Pausado (17/9) |

Anuncios del grupo de estáticos:

| Anuncio | ID | Nota |
|---|---|---|
| **3 · Garantía 7 días** | `120252740747420725` | **El ganador**, y el único activo: casi todo el gasto, los carritos y las 2 ventas |
| 2 · $501 con envío | `120252740746430725` | **Pausado el 23/9.** $0,18 en 7 días, 0 carritos |
| 1 · Envío gratis | `120252740746060725` | **Pausado el 23/9.** $0,34 en 7 días, 0 carritos |

Configuración: México, mujeres 18-45, sin intereses.
**Advantage+ Audience y Advantage+ Creative desactivados** (pedido del cliente).

> **Corrección del 23/9.** Acá decía "optimiza a compra". **Es falso.** El conjunto de estáticos tiene
> `optimization_goal: LANDING_PAGE_VIEWS`. O sea que a Meta se le está pidiendo la gente más barata
> que *abra* la página, no la que compre. Eso explica el clic de $0,03 y el 0,56 % de carritos.
>
> **No se puede arreglar editando el conjunto.** Meta responde:
> *"You can't edit your pixel, conversion event, custom conversion or optimization for an ad set
> after the ad set is published. To run an ad set with your desired changes, create a new ad set."*
> Hay que **armar un conjunto nuevo**. Con 2 compras en 15 días no alcanza para optimizar a compra
> (Meta pide del orden de 50 por semana), así que el paso realista es optimizar a **agregar al
> carrito**, que tiene 16 eventos.

### Ubicaciones del conjunto de estáticos

Manuales, no Advantage+. Historias, Reels y feed **no son conjuntos**: son ubicaciones de un mismo
conjunto. Confundir las dos cosas ya costó dos vueltas.

**Antes del 23/9:** Facebook `feed`, `story`, `facebook_reels`, `profile_feed` · Instagram `stream`,
`story`, `reels`, `profile_feed`.

**Desde el 23/9 (Reels fuera):** Facebook `feed`, `story` · Instagram `stream`, `story`.

Editar las ubicaciones **reinicia el aprendizaje** y además Meta **pausa el conjunto sola** al
guardar el cambio (`status_forced_to_paused: true`). Hay que volver a activarlo a mano con
`ads_activate_entity` o desde Ads Manager, o el conjunto se queda apagado sin avisar.

### Reparto por ubicación del conjunto de estáticos (8–22/9, $60,58)

| Ubicación | Gasto | Clics | Visitas | Carritos | Ventas |
|---|---|---|---|---|---|
| Reels de Instagram | $35,60 | 1.443 | 810 | 6 | 1 |
| Feed de Instagram | $9,33 | 442 | 170 | 1 | — |
| Reels de Facebook | $7,46 | 229 | 157 | 0 | — |
| Historias de Instagram | $4,21 | 217 | 94 | 2 | — |
| **Feed de Facebook** | **$3,51** | 191 | 83 | **2** | **1** |
| Historias de Facebook | $0,46 | 27 | 20 | 0 | — |
| Perfil de Facebook | $0,01 | 1 | 0 | 0 | — |

**71 % del presupuesto se iba a Reels** ($43,06 de $60,58). El feed de Facebook trajo una venta con
$3,51; los Reels de Instagram trajeron la otra con $35,60. Diez veces más caro.

### Los dos conjuntos, 8–22/9

| Conjunto | Gasto | Visitas | Carritos | Ventas | Estado |
|---|---|---|---|---|---|
| Estáticos | $60,58 | 1.334 | 11 | **2** | Activo |
| Video | $28,37 | 418 | 2 | 0 | Pausado el 17/9 |

El video se llevó **casi un tercio de todo lo gastado** sin traer una venta. Por eso se pausó.

Ojo con las "visitas": son las que atribuye Meta. Shopify cuenta 2.863 porque cuenta todo el
tráfico. Las dos cifras son correctas y miden cosas distintas.

### Cuándo se armó todo (horario de Argentina)

| Qué | Cuándo |
|---|---|
| Campaña "Video vs Estáticos" creada | 7/9, 18:07 |
| Los dos conjuntos | 7/9, 18:08 (con 16 segundos de diferencia) |
| Los 3 anuncios de estáticos | 7/9, 18:51 |
| Anuncio de video y el "NO USAR" | 8/9, 09:52–09:59 |
| Última edición del conjunto antes del 23/9 | 17/9, 21:25 |

El registro de actividad de Meta —el que dice **quién** hizo cada cambio— no está habilitado en esta
cuenta ("is being gradually rolled out"). Para el quién hay que mirar el historial en Ads Manager.

## Qué funciona

- **Mensaje de garantía** > precio > envío gratis. Garantía: 4,8–5,4 % de CTR.
- **Estáticos > video.** El video trae clics, pero no carritos.
- Público amplio en México sin intereses: funciona y es barato (~$0,02–0,05 por clic).
- Ciudades con más visitas: Culiacán, Guadalajara, León. Casi todo desde el celular.

## Reglas técnicas de esta cuenta (aprendidas a los golpes)

- **Cambiar la fecha de fin de la campaña la pausa sola.** Siempre revisar el estado y reactivar después.
- En campaña la fecha de fin es `stop_time`; en grupo es `end_time`.
- La fecha de inicio de un grupo ya iniciado no se puede editar.
- Meta no acepta tope de gasto de campaña menor a $100: el límite se maneja con fechas + presupuesto diario.
- **No subir el presupuesto de un grupo que vende más de un 20 % de golpe**: reinicia el aprendizaje.
  Para escalar, subir ~20 % cada 2–3 días, o abrir un grupo nuevo.
- Tocar la tienda (fotos, textos, precios) **no** afecta el aprendizaje de Meta.

## Presupuesto acordado

- $10 por día. Hoy corre solo el grupo de estáticos (~$6,30/día).
- El margen que sobra se piensa usar en un **grupo nuevo** (anuncios con fotos nuevas + retargeting)
  **sin tocar el grupo que vende**.

## Próximos movimientos pensados para Meta

1. Grupo nuevo con 2–3 estáticos del mensaje de garantía y las fotos nuevas.
2. Retargeting: visitantes de la tienda (~1.300) y carritos abandonados, a $2–3 por día.
3. Video nuevo recién cuando haya material mejor; el actual no convierte.

# Cómo se hacen los informes

Todo lo que hace falta para rehacer un informe sin volver a descubrir nada: el comando, los
archivos, las consultas exactas que sacan cada número y las trampas del camino.

---

## La regla que no se negocia

**En lo que ve el cliente no va ningún dato interno de las cuentas.** Nada de:

- El nombre de la cuenta publicitaria (`CP · MAISON · HOLANDA`) ni la palabra **Holanda**.
- IDs de campaña, de conjunto, de anuncio, del píxel o del portafolio.
- Nombres de archivos del tema, IDs de temas, rutas del repo.
- La LLC, el EIN ni nada fiscal.

El pie del informe dice **"Números de Meta y de Shopify"**, y punto. Si hace falta identificar el
origen, alcanza con "la campaña de México".

Los IDs viven en `02-meta-ads.md`, que es interno y no se manda.

---

## Rehacer el PDF: un comando

```bash
python3 informes/construir.py informes/2026-09-23-donde-se-cae-la-venta.html
```

Deja el PDF en `reportes/` con el mismo nombre del HTML. Para elegir otra salida:

```bash
python3 informes/construir.py informes/<cuerpo>.html reportes/<nombre>.pdf
```

**Un informe nuevo** se hace copiando el HTML de uno viejo, cambiando el contenido y corriendo el
mismo comando. El estilo no se toca.

### Los archivos

| Archivo | Qué es |
|---|---|
| `informes/construir.py` | El que arma el PDF. Junta todo y llama a Chrome sin ventana |
| `informes/estilo.css` | El estilo de la marca. **Compartido por todos los informes** |
| `informes/impresion.css` | Solo para el PDF: A4, márgenes, qué no se puede partir entre páginas |
| `informes/figtree.css` | Figtree en base64, los 5 pesos. 135 KB. **No borrar** |
| `informes/<fecha>-<tema>.html` | El cuerpo de cada informe. Solo contenido, sin `<head>` ni estilos |
| `reportes/` | Los PDF ya armados, que son los que recibe el cliente |

El cuerpo empieza con `<!-- titulo: Dónde se está cayendo la venta -->`. De ahí sale el título del
PDF: `Maison Meszarics — Dónde se está cayendo la venta`.

### El estilo, en corto

Fondo blanco, texto `#171412`, rosa `#b97c8c` solo en los títulos de sección, Figtree. Arriba, 4
cifras clave en recuadros; después tablas simples y notas con borde rosa a la izquierda. Sin jerga:
"visitas", "carritos", "ventas". Nada de ROAS, CPM ni CTR sin explicar.

`estilo.css` tiene tema claro y oscuro (por si el cuerpo se mira en pantalla). `construir.py`
**borra los bloques oscuros** antes de imprimir: el PDF es siempre blanco.

---

## De dónde sale cada número

### Meta

Herramienta `ads_get_ad_entities`. La cuenta y los IDs están en `02-meta-ads.md`.

**Los dos conjuntos, con sus totales:**

```
level: adset
time_range: {"since":"2026-09-08","until":"2026-09-22"}
fields: name, amount_spent, impressions, clicks, ctr, adds_to_cart,
        purchases, landing_page_views
filtering: campaign.id IN [<id de la campaña>]
```

**El reparto por ubicación de un conjunto:**

```
level: adset
object_ids: [<id del conjunto>]
breakdowns: ["publisher_platform", "platform_position"]
fields: amount_spent, impressions, clicks, adds_to_cart, purchases,
        landing_page_views
```

Sin `object_ids` y a nivel campaña, el desglose mezcla los dos conjuntos y los números no cierran
con lo que uno espera. **Siempre pedirlo por conjunto.**

**Los anuncios de un conjunto:**

```
level: ad
date_preset: last_7d
fields: name, amount_spent, impressions, clicks, ctr, frequency,
        adds_to_cart, purchases, landing_page_views, effective_status
```

**Cuándo se creó cada cosa:**

```
fields: name, created_time, updated_time, start_time, end_time, effective_status
```

Vienen en horario de **Ámsterdam** (UTC+2 en septiembre). Argentina es **−5 h**, México **−8 h**.

**Las ubicaciones y el objetivo de un conjunto:** pedir `targeting` y `optimization_goal`.

### Shopify

Herramienta `run-analytics-query`, en ShopifyQL.

```sql
FROM sessions SHOW sessions, sessions_with_cart_additions,
  sessions_that_reached_checkout, sessions_that_completed_checkout,
  conversion_rate TIMESERIES day SINCE -15d UNTIL today

FROM sales SHOW orders, gross_sales, net_sales, total_sales,
  average_order_value SINCE -20d UNTIL today

FROM sessions SHOW sessions GROUP BY session_device_type, session_country
  SINCE -15d UNTIL today ORDER BY sessions DESC LIMIT 10
```

El precio que ve México sale de la tienda, no de una cuenta a mano:

```bash
curl -s https://maisonmeszarics.com/products/<handle>.js | python3 -c \
  "import json,sys; print(json.load(sys.stdin)['price'])"
```

---

## Trampas

- **Las "visitas" de Meta y las de Shopify no son lo mismo.** Meta cuenta solo las que atribuye a un
  clic suyo; Shopify cuenta todo el tráfico. El 22/9 eran 1.752 contra 2.863. **Las dos son
  correctas.** Si van las dos en el mismo informe, hay que aclararlo o parece un error.
- **Editar un conjunto lo pausa solo.** Cualquier cambio que no sea el nombre devuelve
  `status_forced_to_paused: true` y el conjunto queda apagado **sin avisar**. Hay que reactivarlo a
  mano. Si no, te enterás dos días después mirando por qué no gastó.
- **El objetivo de un conjunto no se puede cambiar una vez publicado.** Meta contesta: *"You can't
  edit your pixel, conversion event, custom conversion or optimization for an ad set after the ad
  set is published."* Hay que armar un conjunto nuevo.
- **Editar las ubicaciones reinicia el aprendizaje.** Dos o tres días entregando raro. No sacar
  conclusiones en ese lapso y no encadenar dos cambios seguidos.
- **El registro de actividad** (`ads_account_get_activity_logs`), el que dice **quién** hizo cada
  cambio, no está habilitado en esta cuenta. Para el quién hay que mirar el historial en Ads Manager.
- **Chrome no confía en la CA del proxy** de este entorno. Un `<link>` a Google Fonts falla en
  silencio y el PDF sale con la tipografía del sistema. Por eso `figtree.css` está en base64.
- **`section { break-inside: avoid }` deja páginas medio vacías.** Se protegen las tablas y las
  notas, no las secciones enteras.

---

## Los desgloses del 23/9/2026

Período **8 al 22 de septiembre**. Este es el corte que usó el informe del 23/9.

### Los dos conjuntos

| Conjunto | Gasto | Visitas (Meta) | Carritos | Ventas | Estado |
|---|---|---|---|---|---|
| Estáticos | $60,58 | 1.334 | 11 | 2 | Activo |
| Video | $28,37 | 418 | 2 | 0 | Pausado el 17/9 |
| **Total** | **$88,95** | **1.752** | **13** | **2** | |

### Ubicaciones del conjunto de Estáticos

| Ubicación | Gasto | Clics | Visitas | Carritos | Por carrito | Ventas |
|---|---|---|---|---|---|---|
| Reels de Instagram | $35,60 | 1.443 | 810 | 6 | $5,93 | 1 |
| Feed de Instagram | $9,33 | 442 | 170 | 1 | $9,33 | — |
| Reels de Facebook | $7,46 | 229 | 157 | 0 | — | — |
| Historias de Instagram | $4,21 | 217 | 94 | 2 | $2,11 | — |
| Feed de Facebook | $3,51 | 191 | 83 | 2 | **$1,76** | 1 |
| Historias de Facebook | $0,46 | 27 | 20 | 0 | — | — |
| Perfil de Facebook | $0,01 | 1 | 0 | 0 | — | — |

71 % del presupuesto se iba a Reels ($43,06 de $60,58). **Reels salió el 23/9.**

### Anuncios del conjunto de Estáticos (últimos 7 días al 23/9)

| Anuncio | Gasto | Impresiones | Clics | CTR | Carritos | Ventas | Estado |
|---|---|---|---|---|---|---|---|
| 3 · Garantía 7 días | $42,59 | 37.278 | 1.786 | 4,79 % | 9 | 2 | Activo |
| 2 · $501 con envío | $0,18 | 134 | 7 | 5,22 % | 0 | — | Pausado el 23/9 |
| 1 · Envío gratis | $0,34 | 198 | 12 | 6,06 % | 0 | — | Pausado el 23/9 |

### Shopify, día por día

| Día | Visitas | Carritos | Pagos | Ventas |
|---|---|---|---|---|
| 15/9 | 233 | 9 | 6 | 1 |
| 16/9 | 366 | 2 | 1 | — |
| 17/9 | 229 | 0 | 0 | — |
| 18/9 | 243 | 0 | 0 | — |
| 19/9 | 136 | 1 | 1 | 1 |
| 20/9 | 266 | 0 | 0 | 0 |
| 21/9 | 233 | 3 | 0 | 0 |
| 22/9 | 248 | 0 | 0 | 0 |

Del 7 al 22/9: **2.863 visitas, 16 carritos, 8 pagos iniciados, 2 ventas por $88,41.** Ticket
promedio $44,21 — una compradora se llevó 2 unidades. 2.594 de las visitas fueron de México y desde
el celular.

### Las referencias del rubro

| | Hoy | Normal en ropa | Distancia |
|---|---|---|---|
| Visitas que agregan al carrito | 0,56 % | 5 – 8 % | 9 a 14 veces |
| Visitas que compran | 0,07 % | 1 – 2 % | 14 a 29 veces |

Con 2.863 visitas, una tienda que convierte normal habría hecho **entre 29 y 57 ventas**. Son
referencias del rubro para dar contexto, **no una proyección de esta tienda**, y en el informe hay
que decirlo así.

### Cuándo se armó la campaña (horario de Argentina)

| Qué | Cuándo |
|---|---|
| Campaña "Video vs Estáticos" | 7/9, 18:07 |
| Los dos conjuntos | 7/9, 18:08 |
| Los 3 anuncios de estáticos | 7/9, 18:51 |
| Anuncio de video y el "NO USAR" | 8/9, 09:52–09:59 |
| Última edición antes del 23/9 | 17/9, 21:25 |
| Anuncios 1 y 2 pausados, Reels fuera | 23/9 |

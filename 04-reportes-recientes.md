# Reportes recientes

## Números al 19 de septiembre de 2026

### Campaña "Video vs Estáticos" (desde el 8/9)

| Métrica | Valor |
|---|---|
| Invertido | **$68,55 USD** |
| Impresiones | 54.925 |
| Personas alcanzadas | 37.544 |
| Clics | 2.498 (CTR 4,55 %) |
| Visitas a la tienda | 1.300 |
| Carritos | 12 |
| Pagos iniciados | 7 |
| **Ventas** | **2 — $88,02 USD** |

### Antes y después de las fotos nuevas

| | Antes (8–10/9) | Después (15–19/9) |
|---|---|---|
| Visitas | 548 | ~750 |
| Carritos | 2 | 10 |
| Ventas | 0 | 2 |
| Visitas que agregan al carrito | 0,4 % | ~1,3 % |

El primer día y medio después de reactivar (15–16/9) llegó al 2,5 %; en los días siguientes bajó.
Es normal que oscile con volúmenes tan chicos: conviene mirarlo por semana, no por día.

### Día por día desde la reactivación (grupo de estáticos)

| Día | Gasto | Visitas | Carritos | Ventas |
|---|---|---|---|---|
| 15/9 | $2,38 | 36 | 2 | — |
| 16/9 | $6,88 | 163 | 6 | **1 ($58,68)** |
| 17/9 | $4,30 | 115 | 1 | — |
| 18/9 | $6,56 | 137 | — | — |
| 19/9 (parcial) | $4,97 | 100 | 1 | **1 ($29,34)** |

El grupo de video, hasta que se pausó el 17/9: 199 visitas, 0 carritos.

## Números al 23 de septiembre de 2026

Tomados de Meta y de Shopify el 23/9. **El informe del 23/9 los tiene completos.**

### Campaña "Video vs Estáticos" (8–22/9)

| Métrica | Valor |
|---|---|
| Invertido | **$88,95 USD** |
| Impresiones | 72.696 |
| Personas alcanzadas | 47.412 |
| Clics | 3.333 (CTR 4,58 %) |
| Costo por clic | $0,03 |
| **Ventas** | **2 — $88,41 USD** (ROAS 0,99) |

### Shopify (7–22/9)

| Métrica | Valor |
|---|---|
| Visitas | 2.863 (2.594 de México, celular) |
| Visitas con carrito | 16 — **0,56 %** |
| Visitas que llegaron al pago | 8 |
| Ventas | 2 — **0,07 %** |
| Ticket promedio | $44,21 (una compradora se llevó **2 unidades**) |

**Del 20 al 22/9: 747 visitas, 3 carritos, 0 ventas.** Tres días sin vender.

### Por ubicación

Ver el reparto completo del conjunto de estáticos (8–22/9) en `02-meta-ads.md`: **71 % del
presupuesto se iba a Reels**. Ya está sacado.

No hay gasto en Audience Network, así que los clics baratos no vienen de ahí.

### El objetivo del conjunto: la palanca que faltaba

`optimization_goal: LANDING_PAGE_VIEWS`. Ver la corrección del 23/9 en `02-meta-ads.md`.

### Hecho el 23/9

1. Pausados los anuncios **1 · Envío gratis** y **2 · $501 con envío**. Queda solo
   **3 · Garantía 7 días**. Entre los dos pausados gastaron $0,52 en 7 días y no trajeron ni un
   carrito: pausarlos no cambia el reparto del presupuesto, deja la cuenta limpia.
2. **Sacado Reels** de las ubicaciones del conjunto de estáticos. Queda en feed e historias de
   Facebook e Instagram, con el mismo presupuesto de $6,30/día. **Reinicia el aprendizaje**: los
   primeros días entrega raro y más caro.

### El cuello de botella, con referencias del rubro

| | Hoy | Normal en ropa | Distancia |
|---|---|---|---|
| Visitas que agregan al carrito | 0,56 % | 5 – 8 % | **9 a 14 veces menos** |
| Visitas que compran | 0,07 % | 1 – 2 % | **14 a 29 veces menos** |

Con 2.863 visitas, una tienda que convierte normal habría hecho **entre 29 y 57 ventas**. Los rangos
son referencias del rubro para dar contexto, no una proyección de esta tienda.

## PDF entregados al cliente (carpeta `reportes/`)

| Archivo | Fecha | Qué dice |
|---|---|---|
| `Maison-Meszarics-semana-1.pdf` | 1/9 | Primera semana de anuncios, día por día, recomendaciones |
| `Maison-Meszarics-propuesta.pdf` | 1/9 | Tres planes de trabajo con precios |
| `Maison-dias-8-9-sept.pdf` | 9/9 | Primeros dos días de la campaña actual |
| `Maison-antes-de-gastar-el-resto.pdf` | 9/9 | Diagnóstico de fotos y recomendación de pausar |
| `Maison-como-vamos-16-sept.pdf` | 16/9 | Primera venta, antes/después, próximos pasos |
| `Maison-donde-se-cae-la-venta-23-sept.pdf` | 23/9 | Los anuncios traen gente y la tienda no convierte: 2.863 visitas, 16 carritos, 2 ventas. Ubicaciones, referencias del rubro y qué hacer |

**Aviso sobre el último PDF:** dice que la campaña termina el "jueves 18". El 18 fue **viernes**,
y después la campaña se extendió al 27. Si se reenvía, avisar que esa fecha quedó vieja.

## Estilo de los reportes

Todos siguen el mismo diseño, para que el cliente los reconozca:
- Fondo blanco, texto `#171412`, acento rosa `#b97c8c` solo en títulos de sección.
- Tipografía Figtree.
- Arriba, 4 cifras clave en recuadros; después tablas simples y notas con borde rosa a la izquierda.
- Lenguaje sin jerga: "visitas", "carritos", "ventas". Nada de ROAS, CPM ni CTR sin explicar.
- Se generan como HTML y se pasan a PDF con Chrome headless
  (`--print-to-pdf --no-pdf-header-footer`). Fuentes HTML en `C:\Users\acer\maison-docs\`.

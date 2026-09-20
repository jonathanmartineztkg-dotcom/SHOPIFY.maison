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

## PDF entregados al cliente (carpeta `reportes/`)

| Archivo | Fecha | Qué dice |
|---|---|---|
| `Maison-Meszarics-semana-1.pdf` | 1/9 | Primera semana de anuncios, día por día, recomendaciones |
| `Maison-Meszarics-propuesta.pdf` | 1/9 | Tres planes de trabajo con precios |
| `Maison-dias-8-9-sept.pdf` | 9/9 | Primeros dos días de la campaña actual |
| `Maison-antes-de-gastar-el-resto.pdf` | 9/9 | Diagnóstico de fotos y recomendación de pausar |
| `Maison-como-vamos-16-sept.pdf` | 16/9 | Primera venta, antes/después, próximos pasos |

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

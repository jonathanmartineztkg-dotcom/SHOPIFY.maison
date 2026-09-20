# Tienda Shopify — sistema de diseño

Este archivo describe **cómo se ve y cómo está construida** la tienda, para poder cambiarla sin
romper lo que ya funciona. Datos verificados contra el tema publicado al 19/9/2026.

## Datos básicos

| Dato | Valor |
|---|---|
| Dominio | `maisonmeszarics.com` |
| Tienda | `an7i08-cf.myshopify.com` |
| Tema publicado | **"Jonathan Martinez"**, ID `152283250778` (base Dawn) |
| Tema de respaldo | Dawn, ID `150477963354` — **no borrar** |
| Producto único | `shorts-deportivos-de-cintura-alta-con-estampado-de-leopardo` (ID `8063780585562`) |
| Precio | $29 USD (se muestra en MXN, ~$498) |
| Variantes | 4 tallas (S, M, L, XL) × 8 colores = 32 |
| Colores | Rosa, Café, Azul, Púrpura, Cian, Gris Negro, Gris claro, Gris oscuro |
| Copia local del tema | `C:\Users\acer\maison-trabajo` |

## Identidad visual

**La idea:** tienda femenina, cálida y limpia. Fondo crema en vez de blanco, un solo acento rosa
empolvado, negro casi café para texto y botones. Nada de degradados, nada de colores saturados en la
interfaz: el color lo ponen las fotos del producto.

### Colores (variables en `assets/mm-custom.css`)

| Variable | Valor | Uso |
|---|---|---|
| `--mm-paper` | `#fdf9f8` | Fondo de toda la tienda (crema cálido) |
| `--mm-ink` | `#17110f` | Texto principal, botones |
| `--mm-rose` | `#b97c8c` | Acento: barra de anuncio, íconos, enlaces al pasar el mouse |
| `--mm-rose-soft` | `#f6eef0` | Franjas suaves (garantías de la home) |
| `--mm-hair` | `#e8dcde` | Líneas finas y punteadas |
| `--mm-muted` | `#9a8b86` | Texto secundario, etiquetas |
| `--mm-chip` | `#ddd0d2` | Bordes de selectores |
| (texto medio) | `#6b5c58` | Párrafos largos |

El fondo de las fotos de producto es crema `#F5EFEA` — combina con `--mm-paper`.

### Tipografía

| Fuente | Dónde | Cómo se carga |
|---|---|---|
| **Figtree** (400–800) | Todo: cuerpo, títulos, botones | Google Fonts en `layout/theme.liquid`, línea ~324 |
| **Cormorant itálica** (500–600) | Solo acentos: "Impuestos incluidos", "Elige tu color" y la clase `.mm-serif` | Misma línea |
| Assistant | Respaldo (la del tema Dawn original) | — |

Reglas de uso:
- Títulos en **caja normal**, no en mayúsculas. Las mayúsculas se reservan para etiquetas chicas
  (ej. "SIN COSTURAS", la barra de anuncio) con `letter-spacing` amplio.
- La itálica serif es **la voz de la marca**: se usa poco, para que destaque.
- Agregar una fuente nueva **cuesta velocidad**. Se midió que Figtree + Cormorant dejan la página
  en 0,55–0,82 s; cualquier fuente extra hay que medirla.

### Otros rasgos

- **Botones negros y cuadrados** (sin redondeo), texto blanco.
- **Líneas punteadas** (`1px dashed --mm-hair`) como separadores en la ficha. Ver "Punteadas" más abajo.
- **Foto de producto a sangre con recorte 4:5** en la ficha.
- Selectores de talla **cuadrados** en fila de 4; colores como **círculos con el color real**.
- Íconos de línea fina (trazo 1,6–1,7), nunca rellenos.

## Estructura de la home (`templates/index.json`)

Orden actual:

1. **`mm_hero`** (`sections/mm-hero.liquid`) — foto grande con título, bajada y botón.
   - Título "Sin costuras, sin transparencias", botón "Comprar el short".
   - La foto sale de un **archivo del tema** (`assets/mm-portada-rosa.jpg`) vía el ajuste `imagen_archivo`,
     que manda sobre el selector de imagen. Si se vacía ese ajuste, usa la imagen elegida en el editor.
2. **`mm_garantias`** — franja rosa suave con 4 garantías con ícono
   (garantía 7 días, envío gratis, sin devolver nada, pago seguro).
3. **`mm_fichas`** — 4 fichas con foto y enlace (los ocho colores, tallas, tejido, envío y garantía).
4. **`mm_colores`** — "Elige tu color", título en Cormorant itálica, 4 colores con precio.
5. **`mm_cierre`** — "Hecho para el cuerpo que lo usa", foto de la modelo café y botón con el precio adentro.

Todas son secciones propias y se pueden editar desde el editor de temas de Shopify.

## Estructura de la ficha de producto (`templates/product.json`)

Orden de bloques:

```
vendor → title → mm_guarantee → price → variant_picker → mm_sizehelp
→ buy_buttons → mm_shipping → description → mm_info
```

| Bloque | Qué muestra | Archivo |
|---|---|---|
| `title` | Título corto "Short deportivo sin costuras" | `snippets/mm-title.liquid` + ajuste `mm_short_title` |
| `mm_guarantee` | Línea rosa de garantía (donde irían las estrellas) | `snippets/mm-guarantee.liquid` |
| `price` | Precio + "Impuestos incluidos" en la misma línea | `snippets/mm-price.liquid` |
| `variant_picker` | Color primero (círculos), después Talla con enlace a la guía | `snippets/product-variant-picker.liquid` (editado) |
| `mm_sizehelp` | "¿Entre dos tallas?" → WhatsApp | `snippets/mm-size-help.liquid` |
| `mm_shipping` | Envío gratis en una línea | `snippets/mm-shipping-line.liquid` |
| `mm_info` | 4 acordeones: Guía de tallas, Envío y entrega, Devoluciones, Cómo queda y de qué está hecho | `snippets/mm-product-info.liquid` |

Los acordeones de envío y devoluciones **son necesarios para Meta**: la política de anuncios pide
que la información de envío y devolución sea visible en la página de destino.

### Galería de la ficha

- Orden: **modelo café (portada) → modelo rosa → los 8 colores** (fotos 4096 px, fondo crema).
- Cada color tiene asignada su foto: al elegir un color, la galería salta a esa foto.
- Recorte 4:5 con `object-fit: cover`. **Ojo:** Dawn aplica la proporción dos veces
  (en `.product-media-container` y en `.product__media`); el CSS anula las dos.
- `snippets/product-thumbnail.liquid` está modificado para pedir la imagen **1,25 veces más grande**
  cuando la foto es cuadrada (si no, se ve borrosa en el celular por el recorte).

## Punteadas (las líneas cortadas)

Están todas en `assets/mm-custom.css`, bloque "Punteados: el marco del boceto" (~línea 363):

| Selector | Dónde aparece |
|---|---|
| `variant-selects` | Arriba de los selectores de color/talla |
| `.mm-shipline` | Arriba de la línea de envío gratis |
| `.product__description` | Arriba de la descripción |
| `.mm-acc` | Debajo de cada acordeón |
| `.mm-acc:first-of-type` | Arriba del primer acordeón |

## Pie de página

- `sections/mm-pie-enlaces.liquid`: correo arriba, 3 columnas en acordeón (celular) o abiertas (escritorio), redes.
- En la ficha de producto las columnas se ocultan (la info ya está en los acordeones).
- Debajo, el pie de Dawn con tarjetas de pago y políticas, todo sobre el mismo fondo crema.

## Botón flotante de WhatsApp

`snippets/mm-whatsapp-float.liquid`. Número `5491132882892`. Etiqueta "Escribinos".
**No tocarlo** sin que lo pida Jony.

## Archivos propios del tema

```
assets/mm-custom.css            todos los estilos propios (~44 KB; muchos respaldos .bakN)
assets/mm-portada-rosa.jpg      foto del héroe de la home
sections/mm-hero.liquid         héroe
sections/mm-garantias.liquid    franja de garantías
sections/mm-fichas.liquid       4 fichas
sections/mm-colores.liquid      elige tu color
sections/mm-cierre.liquid       cierre con botón
sections/mm-pie-enlaces.liquid  pie
sections/mm-faq.liquid          página de preguntas frecuentes
sections/mm-tracking.liquid     página de rastreo
snippets/mm-*.liquid            piezas de la ficha
```

## Trampas (leer antes de tocar nada)

1. **Nunca usar `shopify theme push --only`** en esta tienda. Borra del tema remoto lo que no esté
   en el lote: ya dejó la tienda en 404 una vez. Siempre `push` completo.
2. **Antes de cada `push`, hacer `pull`.** Se editan cosas desde el admin y desde otras sesiones;
   un `push` sin bajar antes pisa esos cambios.
3. **`section-footer.css` carga después de `mm-custom.css`**: para ganarle hay que subir especificidad.
4. **No poner** `.shopify-section .color-scheme-1{background:transparent}`: la barra de anuncio
   usa el mismo esquema y se queda sin el rosa.
5. Shopify **minifica el CSS** al servirlo: los comentarios desaparecen y los tamaños no coinciden
   con el local. Para comprobar que una subida llegó, buscar una regla concreta en el CSS servido.
6. El color elegido en los círculos, si no se fuerza con `!important`, Dawn lo pinta de negro.
7. `variant-selects` es selector de tipo y Dawn le gana: prefijar con `.product__info-container`.
8. **Verificar el diseño en un navegador real**, no con capturas de Chrome headless:
   no emula bien el celular y ya dio falsos problemas tres veces.

## Comandos

```bash
cd C:\Users\acer\maison-trabajo
shopify theme pull --store an7i08-cf.myshopify.com --theme 152283250778
shopify theme push --store an7i08-cf.myshopify.com --theme 152283250778 --allow-live
```

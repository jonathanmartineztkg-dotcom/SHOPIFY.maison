# Próximos cambios en la tienda

Cambios pedidos por Jony el 19/9/2026, para hacer desde otra sesión.
Todos son **cambios de tienda**: no afectan a Meta y se pueden hacer con la campaña corriendo.
Lo único que no hay que tocar es el grupo de anuncios que vende (ver `02-meta-ads.md`).

Antes de empezar: `theme pull`, nunca `push --only`, y revisar el resultado en un celular real
(ver "Trampas" en `03-tienda-diseno.md`).

---

## Para decidir antes de empezar

Quedan tres puntos por cerrar antes de programar (el primero ya se resolvió):

1. ~~**El "video corto con la M o el nombre"**: ¿dónde va?~~ **Resuelto el 20/9.**
   Va como logo animado en el encabezado (SVG, no video) y el video queda para el Reel y la
   portada de Facebook. Las piezas están hechas: ver `06-logo-redondo.md`.
2. **Punteadas**: ¿cuáles se sacan? Hay una propuesta en el cambio 2.
3. **Banner de la home**: ¿qué mensaje lleva? La propuesta está en el cambio 3.
4. **Segunda tipografía**: ¿Cormorant (ya cargada, costo cero) o una fuente nueva? Ver el cambio 4.

---

## 1. Al elegir un color, que aparezca primero una modelo con ese color

**Lo que se quiere:** la clienta toca "Café" y la galería le muestra primero una modelo con el short
café, y al final la foto limpia del producto café. **No agregar más fotos que esas dos por color.**

**Estado actual:** en la tienda hay foto de modelo solo en **rosa y café**; las 8 fotos limpias ya están.
En `fotos-tienda/` hay 6 fotos de modelo más, listas para subir, que suman **púrpura, cian y gris negro**.
Al elegir un color, hoy la galería salta a la foto limpia de ese color, pero siguen visibles todas las demás.

**Cómo hacerlo bien:**

- **Primero, el contenido:** al 20/9 faltan **3 fotos de modelo**: **azul, gris claro y gris
  oscuro**. Púrpura, cian y gris negro ya están hechas, más una segunda de café (de espaldas) y una
  nueva de rosa: todas en `fotos-tienda/`, sin el sello "Ai" y en 4:5.
  Las que falten tienen que salir con la misma estética: fondo claro, luz pareja, 4:5, sin marcas de IA.
  Sin esas 3 el cambio no se puede terminar para los 8 colores.
- **Después, la técnica:** filtrar la galería por color.
  - Cargar en el **texto alternativo** de cada foto el nombre exacto del color (`Café`, `Gris claro`…).
    Verificado contra la tienda el 20/9: **hoy las 10 fotos del producto lo tienen vacío**, así que
    hay que cargarlo en todas. Los textos propuestos están en `fotos-tienda/LEEME.md`.
  - En la sección del producto, mostrar solo las fotos cuyo texto alternativo coincide con el color
    elegido: **primero la de modelo, después la limpia**. Verificado en el código del tema (Dawn 15.5,
    `assets/product-info.js`, función `updateMedia`): al cambiar de variante pide la sección de nuevo al
    servidor y sincroniza la galería, agregando y quitando fotos. Así que el filtro se hace en Liquid,
    sin librerías ni apps.
  - **Requisito:** `updateMedia` no hace nada si la variante no tiene foto asignada
    (`if (!variantFeaturedMediaId) return;`). Las 32 variantes tienen que tener su foto, si no la
    galería no cambia al elegir ese color.
  - Las dos fotos que no son de un color (si se deja alguna general) van con texto alternativo vacío
    y se muestran siempre, o no se muestran.
- La foto que Shopify asigna a cada variante pasa a ser **la de modelo** de ese color.

**Ojo:** el texto alternativo también lo leen Google y los lectores de pantalla. Usar algo como
"Short de leopardo color Café, vista con modelo" y filtrar por la palabra del color, no por el texto entero.

---

## 2. Sacar algunas punteadas

Hoy hay 5 líneas punteadas en la ficha (detalle en `03-tienda-diseno.md`, sección "Punteadas").

**Propuesta:**

| Línea | Recomendación | Por qué |
|---|---|---|
| Arriba de los selectores de color/talla | **Sacar** | Corta el bloque de compra justo donde tiene que leerse de corrido |
| Arriba de la línea de envío | **Sacar** | El envío debe sentirse parte del botón, no un apartado |
| Arriba de la descripción | Dejar | Separa "comprar" de "informarse" |
| Entre acordeones (abajo de cada uno + arriba del primero) | Dejar | Es lo que les da forma de lista |

Se cambia en `assets/mm-custom.css`, bloque "Punteados: el marco del boceto".
Borrar el `border-top` de `variant-selects` y de `.mm-shipline`, y revisar que el espaciado no quede
desparejo (ese bloque también tiene `padding-top`).

---

## 3. Cambiar el banner que aparece después de la primera imagen de la home

**Hoy:** debajo del héroe está `mm_garantias`, la franja rosa suave con 4 íconos
(garantía, envío gratis, sin devolver nada, pago seguro). No tiene botón.

**Lo que se quiere:** un banner con **enlace directo a la compra, justo abajo**.

**Propuesta:**
- Que el banner diga **el mensaje de la garantía**: es el que funciona en los anuncios
  ("Si no te queda, te devolvemos tu dinero. 7 días."). Quien llega del anuncio encuentra lo mismo
  que la convenció.
- Botón **"Comprar el short"** que lleve directo a la ficha.
- Cuando exista la promo de 2 unidades, este es el lugar para anunciarla.
- Las 4 garantías no se pierden: se pueden bajar como una línea chica debajo del botón,
  o quedar en la ficha, donde ya están.

**Cómo:** mejor una sección nueva (`mm-banner`) con título, texto, botón y enlace editables desde el
editor, que reutilizar la de garantías. Así se pueden alternar sin programar.

---

## 4. Segunda tipografía para los títulos de la información del producto

**Qué títulos:** los 4 acordeones de la ficha: "Guía de tallas", "Envío y entrega", "Devoluciones",
"Cómo queda y de qué está hecho". Envío y devoluciones **tienen que estar visibles para Meta**,
así que conviene que se lean bien y se noten.

**Recomendación:** usar **Cormorant itálica**, que ya está cargada:
- **Costo cero en velocidad.** Ya se descarga para "Impuestos incluidos" y "Elige tu color".
- Es la voz de la marca y va a quedar coherente con la home.
- Tamaño sugerido: 1,7–1,9 rem, peso 600. Cormorant es chica de ojo, a menos tamaño se pierde.

Si se prefiere una fuente distinta, sumarla a la misma URL de Google Fonts en `layout/theme.liquid`
y **medir la velocidad antes y después**. La página hoy carga en 0,55–0,82 s.

Se aplica sobre `.mm-acc summary` en `assets/mm-custom.css`.

---

## 5. Video corto con la M o el nombre de la marca

> **Hecho el 20/9.** El plan completo y las piezas listas para usar están en `06-logo-redondo.md`
> y en la carpeta `marca/`. Lo de abajo es el análisis que llevó a esa decisión.

**No se puede como foto de perfil:** Instagram y las páginas de Facebook solo aceptan imagen fija.

**Opciones reales, de mejor a peor:**

| Opción | Dónde se ve | Costo |
|---|---|---|
| **Logo animado en el encabezado de la tienda**: la M se dibuja una vez al entrar y queda fija | Arriba de todo en la tienda | Muy bajo: se hace con SVG + CSS, pesa unos pocos KB |
| Video corto como **portada de la página de Facebook** | Facebook | Nulo, se sube desde Facebook |
| **Reel** o historia destacada de Instagram con la animación | Instagram | Nulo |
| Pantalla de carga con la animación al abrir la tienda | Toda la tienda | **No recomendado**: frena la entrada y baja las ventas |

Para la foto de perfil de Instagram y Facebook: la **M fija**, sacada del primer cuadro de la animación,
para que todo quede igual.

---

## Otros pendientes que conviene hacer en la misma pasada

| Pendiente | Esfuerzo | Nota |
|---|---|---|
| **Voseo** en guía de tallas, envíos, devoluciones y rastreo (13 casos: "Medí", "elegí", "Recibís", "escribinos"…) | Bajo | Archivos: `snippets/mm-product-info.liquid`, `sections/mm-faq.liquid`, `sections/mm-tracking.liquid` |
| 4 páginas heredadas vacías publicadas (`/pages/the-maison`, `about-us`, `authenticity`, `contact`) | Bajo | Se despublican desde el admin |
| **Promo "llevá 2"** (ej. el segundo a mitad de precio) | Bajo | Descuento automático de Shopify. Anunciarla en el banner del cambio 3 |
| Checkout más corto (ocultar "empresa" y la segunda línea de dirección) | Muy bajo | Configuración → Pagos/Checkout |
| Campo RFC/CURP | — | **Esperar** a que Abby confirme la línea DDP. Si es DDP, no hace falta |
| Foto del tejido de cerca, a contraluz | Contenido | Responde "¿se transparenta?", la duda número uno |

**No incluido a propósito:** el pack con suplemento para estrías. Requiere registro sanitario en
México y Meta rechaza anuncios con promesas sobre el cuerpo. Se dejó para más adelante.

---

## Orden recomendado

1. **Rápidos y sin riesgo** (una tarde): voseo, páginas vacías, punteadas, tipografía de los acordeones, checkout más corto.
2. **Banner de la home** con la garantía y el botón de compra.
3. **Promo "llevá 2"** y anunciarla en el banner.
4. **Producir las 6 fotos de modelo** que faltan y, con ellas, el filtro de galería por color.
5. **Logo animado**: ya está definido y armado, solo falta instalarlo (`06-logo-redondo.md`).

Después de cada paso: revisar en un celular real, y si se quiere medir el efecto, anotar la fecha
del cambio para cruzarla con los números de Meta.

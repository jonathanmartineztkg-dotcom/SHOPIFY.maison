# Ficha, galería por color y tipografía

Pedidos de Jony del 21/9/2026. Todo verificado contra el tema publicado, contra el CSS que la
tienda sirve y contra el `product-info.js` que corre hoy en el navegador.

## Qué archivo va dónde

| Archivo de `marca/` | Dónde va en el tema |
|---|---|
| `product-media-gallery.liquid` | Reemplaza `snippets/product-media-gallery.liquid` |
| `mm-cambios-21-09.css` | Se pega **al final** de `assets/mm-custom.css` |
| *(una línea)* | La URL de Google Fonts en `layout/theme.liquid`, ~línea 324 |

Después: `push` completo, nunca `--only`, y revisar en un celular real.

---

## 1. La galería por color

### Lo que pasaba de verdad

El problema que viste —eliges Café y aparece una modelo con el short rosa— no era un detalle:
la ficha estaba mostrando **9 fotos mezcladas de todos los colores**.

La causa está en un ajuste del tema, `hide_variants`, que está **activado**. Lo que hace es:
mostrar la foto de la variante elegida, y esconder **las demás fotos que sean de alguna variante**.
Las fotos que **no** están asignadas a ninguna variante se muestran **siempre**, sea cual sea el
color.

Cuando el 21/9 se asignaron las fotos de modelo nuevas a las variantes, las **dos viejas** (la de
café y la de rosa) dejaron de ser fotos de variante. Y la de café de espaldas nunca lo fue.
Resultado: esas tres pasaron a mostrarse en todos los colores. Por eso, en Café, aparecía la modelo
de rosa.

El contador de la ficha lo confirma: decía **9** cuando el producto tiene 16 fotos.

### Cómo se arregla

El archivo nuevo filtra la galería **por el texto alternativo** de cada foto:

- muestra solo las fotos cuyo texto alternativo contiene el nombre exacto del color elegido;
- **primero las que dicen "modelo"**, después la foto limpia del producto;
- si un color no tiene foto de modelo, queda **solo la limpia** y no hay nada para deslizar.

Los nombres de los colores no se pisan entre sí (`Gris claro` no coincide con `Gris oscuro`), así
que el filtro es exacto. Lo verifiqué contra los 16 textos alternativos que están cargados hoy.

**Red de seguridad:** si ninguna foto coincidiera con el color —por ejemplo porque a una se le borró
el texto alternativo desde el admin— el filtro se apaga solo y muestra la galería completa, como
Dawn de fábrica. La ficha nunca queda sin fotos.

### Cómo queda cada color

| Color | Qué se ve | Cuántas |
|---|---|---|
| Café | modelo de frente, modelo de espaldas, **modelo vieja**, foto limpia | 4 |
| Rosa | modelo nueva, **modelo vieja**, foto limpia | 3 |
| Púrpura | modelo, foto limpia | 2 |
| Cian | modelo, foto limpia | 2 |
| Gris Negro | modelo, foto limpia | 2 |
| Azul | foto limpia | 1, sin deslizar |
| Gris claro | foto limpia | 1, sin deslizar |
| Gris oscuro | foto limpia | 1, sin deslizar |

**Lo que hay que decidir:** las dos fotos de modelo **viejas** (café y rosa) son de 1600×2000, menos
de la mitad de resolución que las nuevas, y son las que hacen que café tenga 4 fotos y rosa 3.
Sacándolas queda café con 3 (frente, espaldas, limpia) y rosa con 2, que es exactamente lo pedido:
las modelos primero y el artículo al final. **Decilo y las quito** — es un minuto desde acá o desde
el admin.

### Por qué esto funciona sin tocar JavaScript

Verificado leyendo el `product-info.js` que la tienda sirve hoy:

- Al cambiar de color, Dawn pide la sección de nuevo al servidor y **sincroniza la lista de fotos**:
  agrega las que faltan, saca las que sobran y las reordena para que queden igual que en el HTML
  nuevo. O sea, respeta el filtro y el orden que arma el Liquid.
- **Requisito, que ya se cumple:** `updateMedia` arranca con `if (!variantFeaturedMediaId) return;`.
  Si una variante no tuviera foto asignada, la galería no cambiaría al elegir ese color. Las 32
  variantes tienen foto desde el 21/9.
- **Cuidado para más adelante:** `updateMedia` solo sincroniza la lista principal, **no la de
  miniaturas**. Hoy no importa porque el diseño de la galería está en "stacked" y las miniaturas no
  se dibujan. Por las dudas, el archivo nuevo las apaga mientras el filtro esté activo: si algún día
  se cambia a "thumbnail", no van a quedar miniaturas viejas de otros colores.

---

## 2. El botón del héroe con esquinas redondeadas

Está en el bloque 1 del CSS, con el redondeo en una sola variable (`--mm-radio`, arranca en 8 px).
Cambiando ese número cambia todo: `0` vuelve a cuadrado, `999px` lo hace pastilla.

**Una advertencia de coherencia:** el sistema de diseño de la tienda dice "botones negros y
**cuadrados**, sin redondeo". Si solo se redondea el del héroe, se nota el parche apenas bajás y ves
el botón de compra cuadrado. Por eso el mismo bloque redondea también el botón del cierre, el de
"Agregar al carrito" y el de pago rápido. Si preferís que el redondeo sea **solo** del héroe, hay
que borrar esas tres líneas — pero no lo recomiendo.

Aparte, ese botón se lee como barra blanca y no como botón por una razón de proporción: mide 50 px
de alto con texto de 14,5 px, o sea un rectángulo casi vacío. El redondeo ayuda; subir el texto a
15 px y bajar el alto a 44 ayuda más. Eso está en las maquetas del lienzo, no en este CSS, para no
mezclar dos cambios en uno.

---

## 3. Las garantías en una sola fila

En celular pasan de **2×2 a 4 en fila**, como se ven hoy en escritorio. La altura baja de unos
170 px a unos 75 px: media pantalla de celular recuperada, que es donde se decide la compra.

Los íconos pasan de rosa a negro. No es capricho: el trazo rosa `#b97c8c` sobre el fondo rosa
`#f6eef0` da **1,9:1** de contraste, y el mínimo para que un gráfico se vea es 3:1. Por eso se veían
lavados. Si el rosa te gusta igual, se borra ese bloque y listo.

**Recomendación aparte, desde el editor:** con 4 columnas en un celular cada etiqueta tiene unos
90 px. "Garantía de 7 días" entra en dos renglones. Acortándolas a **"7 días"**, **"Envío gratis"**,
**"Sin devolver"** y **"Pago seguro"** entran en uno solo y la tira queda más limpia todavía.

---

## 4. Las punteadas

Fuera las de los acordeones, como pediste. Está en el bloque 3 del CSS.

La trampa: los acordeones tienen **cuatro** líneas, no dos. Además de las punteadas hay dos
**sólidas** cargadas antes en el mismo archivo. Si se borraran solo las punteadas quedarían las
sólidas y se vería casi igual, pero peor: líneas enteras en vez de cortadas. El bloque apaga las
cuatro y compensa el aire que se pierde.

La punteada de arriba de la descripción se deja: es la única que separa "comprar" de "informarse".

---

## 5. La tipografía más alta y más angosta

Medí el título real de la home —"Sin costuras, sin transparencias"— en cuatro tipografías, todas al
mismo tamaño de 40 px. La comparación está en `marca/comparacion-tipografias.png`.

| Tipografía | Ancho de la línea más larga | Qué tanto achica |
|---|---|---|
| **Figtree 800** (lo que hay hoy) | 339 px | — |
| Oswald 600 | 292 px | −14 % |
| **Barlow Condensed 700** | 271 px | **−20 %** |
| Big Shoulders Display 700 | 254 px | −25 % |

Ese es el punto: al ser más angosta, el mismo título ocupa menos, así que **se puede agrandar** y
seguir entrando. Por eso el CSS sube el título del héroe de 3 rem a 3,9 rem en celular y de 5,2 a
6,6 rem en escritorio: más grande y más alto, en el mismo lugar.

**Recomiendo Barlow Condensed 700.** Razones:

- Tiene minúsculas de verdad. La tienda tiene una regla: **títulos en caja normal, las mayúsculas se
  reservan para etiquetas chicas**. Eso deja afuera a las condensadas que son solo mayúsculas, como
  Bebas Neue.
- Es angosta pero no industrial. Big Shoulders achica más, pero tiene un aire de cartel de fábrica
  que pelea con una marca cálida y femenina. Oswald achica poco y se ve en todas partes.
- Convive bien con Figtree, que sigue siendo el cuerpo.

Si querés algo más de carácter y menos seguro, **Big Shoulders Display 700** es la otra que miraría:
es la más angosta de las cuatro y se ve más editorial. Es una decisión de gusto, las dos funcionan.

### Dónde se usa, para que quede coherente

Tres tipografías, tres trabajos, sin mezclar:

| Tipografía | Para qué |
|---|---|
| **Barlow Condensed 700** | Los títulos grandes: el del héroe, el del cierre y los de las 4 fichas |
| **Cormorant itálica** | La voz de la marca, en acentos chicos: "Impuestos incluidos", "Elige tu color" |
| **Figtree** | Todo lo demás: cuerpo, botones, etiquetas |

El CSS ya la aplica sobre `.mm-hero__tit`, `.mm-cierre__tit` y `.mm-ficha__tit`. Los acordeones
quedan afuera a propósito: para esos, el plan ya recomendaba Cormorant itálica.

### La línea que hay que cambiar

En `layout/theme.liquid`, ~línea 324, hoy dice:

```
https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800&family=Cormorant:ital,wght@1,500;1,600&display=swap
```

Cambiar por:

```
https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700&family=Figtree:wght@400;500;600;700;800&family=Cormorant:ital,wght@1,500;1,600&display=swap
```

Un solo peso, que es lo que cuesta menos. **Medir la velocidad antes y después**: la página carga
hoy en 0,55–0,82 s y esa es una regla del proyecto, no una sugerencia. Si se va arriba de 0,9 s,
volver atrás.

---

## Orden para subirlo

1. `theme pull`.
2. Reemplazar `snippets/product-media-gallery.liquid`.
3. Pegar `mm-cambios-21-09.css` al final de `assets/mm-custom.css`.
4. Cambiar la línea de Google Fonts en `layout/theme.liquid`.
5. `push` **completo**.
6. En un celular real: elegir cada uno de los 8 colores y confirmar la tabla de arriba.
7. Medir la velocidad. Si subió, el sospechoso es la tipografía.

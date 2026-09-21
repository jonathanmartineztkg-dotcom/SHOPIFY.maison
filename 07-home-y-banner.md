# La home y la barra de arriba — posibilidades

Pedido de Jony el 20/9/2026. Todo lo de acá está **verificado contra el tema publicado**
(`Jonathan Martinez`, ID `152283250778`) y contra el CSS que la tienda sirve hoy, no supuesto.

Las propuestas de diseño salen de tiendas del rubro que están bien posicionadas, no de un estilo
inventado. Las que se miraron para esto:

| Tienda | Qué se le mira |
|---|---|
| **Gymshark** | La barra de arriba: rota 5 mensajes, todos clicables, porcentajes en número |
| **Oner Active** | La barra mezcla oferta + "SHOP NOW" + confianza. Héroe con un solo botón |
| **Cakes Body** | El botón del héroe nombra lo que te llevás ("SHOP THE BUNDLE"), y el descuento va sobre el pack |
| **Popflex** | Urgencia sin descuento: etiqueta de "Low Stock" en vez de rebaja |

---

## 1. La barra de arriba con carrusel

**La buena noticia: no hay que programar nada.** La barra de la tienda es la de Dawn sin tocar
(`sections/announcement-bar.liquid`), y **ya trae el carrusel**. Lo confirmé leyendo el archivo:
cuando hay más de un bloque cambia sola a `slideshow-component`, con rotación automática y
velocidad configurable. Admite hasta 12 mensajes, y cada uno tiene **texto + enlace**.

Hoy hay un solo bloque, por eso no rota.

### Cómo se hace (5 minutos, desde el editor)

1. Editor de temas → **Encabezado → Barra de anuncios**.
2. **Agregar bloque → Anuncio**, una vez por mensaje.
3. Marcar **"Rotación automática"** (viene **desactivada** de fábrica — es el paso que se olvida).
4. Velocidad: **5 segundos** (el rango va de 3 a 10).

### Los mensajes que propongo

Tres, en este orden. Más de tres y el último no lo ve nadie: con 5 segundos cada uno, la vuelta
completa ya son 15 segundos.

| # | Texto | Enlace |
|---|---|---|
| 1 | `30% de descuento en tu primer pedido` | La ficha del producto |
| 2 | `Comprar el short` | La ficha del producto |
| 3 | `Envío gratis a todo México` | `/policies/shipping-policy` |

El 2 es el "texto clicable para comprar" que pediste. Dawn le pone sola **una flecha que se
desplaza al pasar el mouse** a todo mensaje que tenga enlace, así que se va a ver que es clicable
sin agregarle nada.

Dos detalles de redacción, sacados de Gymshark:

- **El porcentaje en número** (`30%`), no en letras. Se lee de un vistazo.
- **Menos de 45 caracteres** por mensaje. Arriba de eso, en celular se corta o se achica.

**Ojo:** el mensaje 1 solo se puede poner si el descuento es real. Eso es el punto 2 de acá abajo.

### El único retoque de código

Dawn le mete a la barra **dos flechitas de "anterior / siguiente"** a los costados. En una barra
fina y rosa como la nuestra quedan apretadas y se ven mal en celular. El CSS para esconderlas está
en `marca/mm-barra-anuncio.css`: se sigue pudiendo deslizar con el dedo y la rotación automática
sigue andando; solo desaparecen los botones.

---

## 2. El descuento del 30 %

Lo pediste como **"un descuento, sin modificar el precio"**. Eso se hace y es la forma correcta:
en Shopify el descuento va aparte del precio del producto.

### Cómo se hace sin tocar el precio

Shopify admin → **Descuentos → Crear descuento → Descuento automático**:

- 30 % sobre el producto.
- **El precio de la ficha no se toca**: sigue diciendo $29 USD (~$498 MXN) en el producto.
  Shopify muestra el tachado y el nuevo precio, y lo aplica solo en el carrito.
- Se respeta la regla del proyecto de no cambiar el precio sin el cliente: el campo de precio
  queda igual.

### Tres formas, de más a menos costo de margen

| | Qué es | Qué paga la clienta | Efecto |
|---|---|---|---|
| **A** | 30 % sobre la unidad | $20,30 (~$350) | El más simple. Se lleva 30 % del margen en cada venta |
| **B** | **El segundo a 30 %** | $49,30 las dos (~$850) | Sube el ticket en vez de bajarlo. Es lo que ya estaba pensado como "llevá 2" |
| **C** | A o B, **con fecha de corte** | Igual | La urgencia sale de la fecha, no del número |

**Lo que recomiendo: B + C.** "El segundo con 30 %, hasta el domingo."

Tres razones:

1. Es el patrón de **Cakes Body**: su "20% OFF" está sobre el pack, no sobre la unidad suelta.
   Descuento visible, margen protegido.
2. Con 2 ventas totales hasta hoy, regalar 30 % de cada unidad sobre $29 duele mucho más que
   ganar una segunda unidad.
3. La fecha de corte da urgencia de verdad y se puede repetir sin quemar la marca.

Si querés el camino simple igual, **A** funciona y es honesto. Es una decisión de margen, y el
precio lo decide el cliente: eso hay que pasárselo antes.

### Una cosa que no se puede hacer

Poner la etiqueta de **−30 % sin descuento real** — o sea, cargar un "precio de comparación" de
$41,43 para que Shopify muestre el tachado, dejando el cobro en $29. El short nunca se vendió a
$41,43, así que es un precio de referencia inventado. En México la PROFECO lo trata como publicidad
engañosa, y rompe dos reglas del propio proyecto (no tocar el precio sin el cliente, no inventar
señales).

El riesgo acá no es teórico: **Meta es el canal que está vendiendo**. Un rechazo por precios
engañosos pausa justo la campaña que hace las ventas.

### Si no se quiere resignar margen

La alternativa de Popflex es urgencia **por stock**, no por rebaja: la etiqueta "Low Stock".
**Hoy no se puede usar**: el inventario está cargado en 999–1000 por variante, así que decir
"quedan pocos" sería tan inventado como el descuento falso. Serviría recién cuando el inventario
refleje lo que hay de verdad.

Queda una tercera vía honesta y gratis: **"Envío gratis solo esta semana"**. Es verdad si se pone
una fecha y se cumple, y no toca el precio.

---

## 3. La home

### Qué hay hoy (leído de `templates/index.json`)

```
mm_hero → mm_garantias → mm_fichas → mm_colores → mm_cierre
```

- **Héroe**: título "Sin costuras, sin transparencias", bajada "Cintura alta que no se enrolla.
  Ocho colores para elegir.", botón **"Comprar el short"**.
- **mm_garantias**: la franja rosa con 4 íconos, sin botón.
- **mm_fichas**: 4 fichas temáticas.
- **mm_colores**: "Elige tu color" — **solo muestra 4 de los 8 colores** (Rosa, Café, Púrpura,
  Gris claro).
- **mm_cierre**: "Hecho para el cuerpo que lo usa" + botón con el precio adentro.

### Por qué el primer botón no termina de cerrar

Creo que el problema no es el botón: es **lo que hay arriba del botón**.

El aprendizaje más fuerte del proyecto es que **el mensaje que vende es la garantía**
("si no te queda, te devolvemos tu dinero"), y que le gana al precio y al envío gratis por mucho.
El anuncio que hizo las 2 ventas es justamente "Garantía 7 días".

Pero la clienta toca ese anuncio y aterriza en un título sobre **costuras**. La garantía aparece
recién en la franja de abajo, sin botón. **La home no continúa la frase que la convenció.**
El botón dice "Comprar el short" sin haberle dado todavía un motivo para creer.

### Tres formas de arreglarlo

Las tres son de menos a más trabajo. Se pueden combinar.

---

**Opción 1 — El héroe repite lo del anuncio** *(patrón Cakes Body)*

Cakes Body usa título + bajada + **un solo botón que nombra lo que te llevás** ("SHOP THE BUNDLE",
no "comprar"). Acá sería:

| | Hoy | Propuesta |
|---|---|---|
| Título | Sin costuras, sin transparencias | *(igual)* |
| Bajada | Cintura alta que no se enrolla. Ocho colores para elegir. | **Si no te queda, te devolvemos tu dinero. 7 días.** |
| Botón | Comprar el short | **Comprar el short — $498** |
| Debajo | — | *Envío gratis · Pago seguro* (letra chica) |

- **Trabajo:** ninguno de código. Son tres campos del editor (`titulo`, `bajada`, `boton_texto`).
- **Por qué:** quien llega del anuncio encuentra la misma promesa arriba de todo, y el precio en el
  botón le saca una duda antes de hacer clic.
- **Es lo que yo haría primero**, esta misma tarde.

---

**Opción 2 — El precio adentro del botón, como ya lo hace el cierre**

`mm_cierre` ya tiene `boton_texto: "Comprar por"` con `mostrar_precio: true`. O sea que **el tema
ya sabe hacer botones con el precio adentro**: solo hay que subir ese patrón al héroe.

- **Trabajo:** chico. Copiar el ajuste `mostrar_precio` de `sections/mm-cierre.liquid` a
  `sections/mm-hero.liquid`.
- **Ventaja sobre escribir "$498" a mano:** si algún día cambia el precio o se activa el descuento,
  el botón se actualiza solo. Con el texto escrito a mano quedaría mintiendo.
- **Va junto con la opción 1**, no en vez de.

---

**Opción 3 — Elegir el color desde el héroe** *(patrón Oner Active / Gymshark)*

En vez de un botón, los 8 colores como círculos abajo de la bajada. Se toca un color y se cae en la
ficha **con ese color ya elegido** (`?variant=`).

- **Trabajo:** el más grande de los tres. Sección nueva o bloque dentro de `mm-hero.liquid`.
- **Por qué puede ganarle a un botón:** el clic deja de ser "comprar" y pasa a ser "elegir".
  Para una tienda de un solo producto en 8 colores, es la decisión que la clienta quiere tomar
  primero. Es lo que hacen las tiendas grandes del rubro con sus productos estrella.
- **Riesgo:** si los colores se comen el lugar del botón en celular, se pierde el llamado claro.
  Habría que dejar el botón abajo de los círculos, no sacarlo.

---

### Lo que va abajo del héroe

**Cambiar `mm_garantias` por el banner con botón** (es el cambio 3 de `05-proximos-cambios.md`, que
quedó pendiente de decidir el mensaje). Con lo de arriba, el mensaje ya está decidido:

- Título: **"Si no te queda, te devolvemos tu dinero"**
- Texto: "7 días para probarlo. Sin devolver el short."
- Botón: **"Comprar el short"** → la ficha
- Cuando exista la promo del segundo al 30 %, este es el lugar donde se anuncia.

Las 4 garantías no se tiran: bajan como una línea chica debajo del botón.

### Dos arreglos concretos que encontré de paso

1. **`mm_cierre` usa la foto vieja del café** (`maison-short-leopardo-cafe-modelo.jpg`, de
   1600×2000). Ya está subida la nueva en 3277×4096, sin el sello "Ai". Es cambiar la imagen en el
   editor: la sección más abajo de la home hoy muestra la foto de peor calidad de la tienda.
2. **`mm_colores` muestra solo 4 de los 8 colores**, y con las fotos limpias. Ahora hay foto de
   modelo en 5 colores (café, rosa, púrpura, cian y gris negro). Poner ahí las de modelo en vez de
   las limpias, aunque sigan siendo 4, cambia bastante cómo se ve la home.

---

## 4. Sacar las punteadas de abajo

Las 5 punteadas de la ficha están verificadas contra el CSS servido. Las **de abajo** son las de los
acordeones:

| Regla | Dónde se ve |
|---|---|
| `.mm-acc { border-bottom: 1px dashed }` | Debajo de cada acordeón |
| `.mm-acc:first-of-type { border-top: 1px dashed }` | Arriba del primero |

**Hay una trampa:** además de las punteadas, los acordeones tienen **dos líneas sólidas** que vienen
de antes en el mismo archivo (`.mm-acc { border-top: 1px solid }` y
`.mm-acc:last-of-type { border-bottom: 1px solid }`). Si se borran solo las punteadas, **quedan las
sólidas** y el resultado se ve casi igual, pero peor: líneas enteras en vez de cortadas.

El bloque que las saca todas está en `marca/mm-punteadas-off.css`. Va **al final** de
`assets/mm-custom.css` para que le gane a las reglas de más arriba.

Con las líneas fuera, los acordeones se pegan entre sí. El mismo bloque le suma un poco de aire
(`padding` en el `summary`) para que se sigan leyendo como una lista.

**Lo que dejaría:** la punteada de arriba de la descripción (`.product__description`). Es la única
que separa "comprar" de "informarse", y sacarla mezcla las dos cosas.
En `05-proximos-cambios.md` ya estaba propuesto sacar además las de `variant-selects` y
`.mm-shipline`; si se quiere hacer todo de una, el archivo también las trae comentadas.

---

## 5. Dónde va el video de la M

El video que subiste (`0920.mp4`, rama `video-pag`) es el redondo con la M sobre una foto de la
modelo, 3 segundos. Venía en 2160×2700 y **8,75 MB**, que para web es imposible. Quedaron dos
versiones en `marca/`:

| Archivo | Qué es | Peso |
|---|---|---|
| `video-pag-crema-1080.mp4` | El redondo sobre el crema de la tienda (`#fdf9f8`), 1080×1080, sin audio | **91 KB** |
| `video-pag-1080.mp4` | El original sobre negro, 1080×1350, para redes | 54 KB |

El fondo negro del original no pega con la tienda, que es crema. Por eso la versión de arriba
recorta el redondo y lo apoya sobre el crema exacto de la marca.

**Dónde lo pondría:** una franja chica entre `mm_colores` y `mm_cierre`, con el video a unos 120 px
y una línea al lado. 91 KB no le mueve la aguja a la velocidad.

**Dónde no:** en el héroe. Vale el mismo argumento de `06-logo-redondo.md` — la página carga en
0,55–0,82 s y eso es parte de por qué vende.

---

## Orden que propongo

1. **Hoy, sin código y sin riesgo:** los 3 mensajes de la barra con rotación automática (sin el del
   descuento todavía), el texto del héroe de la opción 1, la foto nueva en `mm_cierre`.
2. **Decidir el descuento** con el cliente (A, B o C) y recién ahí sumar el mensaje 1 a la barra.
3. **Una tarde de código:** las punteadas, el CSS de la barra, el precio en el botón del héroe.
4. **Después:** el banner de la garantía con botón, y la franja del video.
5. **Al final:** los colores en el héroe (opción 3), que es lo más grande.

Después de cada paso: revisar en un celular real y anotar la fecha, para poder cruzarla con los
números de Meta.

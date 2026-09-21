# Etiquetas sobre la galería y descuento por cantidad

Pedido de Jony del 21/9: las dos pastillas de la captura (una "New" blanca y una verde oliva con
el importe descontado) arriba del carrusel, con el ahorro **en pesos y atado al precio**; y los
botones de "compra más, paga menos" con 10 / 20 / 30 % según cuántos shorts se lleven.

**Lienzo con los cinco diseños:** `Maison — etiquetas y descuento por cantidad`
→ https://claude.ai/artifact/MwqCfZy4A3pbrw2UoPYAo9

---

## 1. Los números de hoy

El precio que ve un cliente en México lo devuelve la propia tienda:

```
curl -s https://maisonmeszarics.com/products/<handle>.js  →  "price": 50800
```

Son **$508.00 MXN** por el short de **29 USD**. El tipo de cambio que aplica Shopify hoy da
≈ 17,52 MXN por dólar. Hace una semana el mismo short daba $498. **Por eso el importe de la
etiqueta no se escribe a mano.**

| Cantidad | Descuento | Total | Por unidad | Ahorro |
|---|---|---|---|---|
| 1 | — | $508.00 | $508.00 | — |
| 2 | 10 % | $914.40 | $457.20 | $101.60 |
| 3 | 20 % | $1,219.20 | $406.40 | $304.80 |
| 4 | 30 % | $1,422.40 | $355.60 | $609.60 |

## 2. Cómo se mantiene sincronizado el importe

En Liquid **nunca se escribe el número**. Se hace la cuenta en centavos sobre `product.price` y se
imprime con el filtro `money`, que respeta la moneda que Shopify le está mostrando a esa persona:

```liquid
{%- assign tope_pct = 30 -%}
{%- assign tope_unidades = 4 -%}
{%- assign ahorro = product.price | times: tope_unidades | times: tope_pct | divided_by: 100 -%}
<span class="mm-etiqueta mm-etiqueta--oferta">
  Hasta {{ tope_pct }}% · {{ ahorro | money_without_trailing_zeros }}
</span>
```

Si el dólar sube y el short pasa a $520, la etiqueta pasa sola a $624. Si mañana se vende en otra
moneda, también. **Lo único que hay que tocar si cambian los tramos son las dos primeras líneas.**

## 3. El mecanismo del descuento — lo que sí se puede

Corrijo lo que había anotado antes: **los tres tramos se pueden hacer sin app y sin Shopify
Functions.** Se crean **tres descuentos automáticos** de producto, cada uno con su cantidad
mínima, y **sin permiso de combinarse entre ellos**:

| Descuento | Mínimo | Valor |
|---|---|---|
| "Llevando 2" | 2 unidades | 10 % |
| "Llevando 3" | 3 unidades | 20 % |
| "Llevando 4 o más" | 4 unidades | 30 % |

La documentación de Shopify dice, textual: *"If two or more discounts are applied, but can't be
combined due to the discount combination setting or the content of the cart, then the best discount
for the customer's cart is always applied."*
(https://help.shopify.com/en/manual/discounts/discount-combinations)

O sea: con 4 en el carrito los tres califican, no se suman, y Shopify aplica el mejor → 30 %. Con 3
califican dos y aplica 20 %. Con 2, 10 %. Exactamente la escalera que se pidió, con tres descuentos
nativos. El tope de la tienda son 25 descuentos automáticos activos; se usan 3.

**Lo que esto no hace:** no muestra la escalera en la ficha. Eso lo dibuja el tema (los diseños C,
D y E del lienzo) y el descuento se ve recién en el carrito. Por eso los tres diseños lo dicen con
todas las letras: *"el descuento se aplica al pagar, el precio de la ficha no cambia"*.

## 4. Dos cosas para decidir antes de crearlos

- **El margen.** 30 % sobre $508 deja el short en $355.60. Eso es una decisión de Jony, no mía: no
  sé el costo. Los porcentajes 10/20/30 los puso él, pero conviene mirar el número final antes de
  prenderlo.
- **"NUEVO" hoy es falso.** El producto se creó el **11/8/2026** y viene vendiendo desde entonces:
  no es nuevo. Si la pastilla se deja fija, es una afirmación falsa en la ficha. Las salidas
  honestas son dos: atarla a `product.created_at` (aparece sola los primeros 30 días y después se
  apaga sola), o cambiar el texto por algo que sí sea cierto — SIN COSTURAS, 8 COLORES.

## 5. La línea de las pestañas

Confirmado: la línea fina que separa las características de la descripción **ya está** en el
borrador, en el bloque 4 de `assets/mm-cambios.css`:

```css
--mm-linea: rgba(23, 17, 15, .09);
.product__description li { padding: 1.1rem 0; border-top: 1px solid var(--mm-linea); }
```

Los cinco diseños del lienzo la reutilizan tal cual en los renglones de totales y en las pestañas.

## 6. Qué hay en el lienzo

| Tablero | Qué muestra |
|---|---|
| **A** | Las pastillas con los colores de la captura: blanca + verde oliva `#454e37`. |
| **B** | Las mismas, en la paleta de la tienda, con el texto atado a los tramos ("HASTA 30%"). |
| **C** | Cantidad en tarjetas apiladas: 72 px por fila, con "4 o más" y un −/+ para meter 5, 6, 10. |
| **D** | Cantidad en una fila de cuatro columnas de 82 px. Ocupa 104 px en vez de 318. |
| **E** | La ficha entera a 390 px con todo junto y funcionando: se toca la cantidad y se mueven a la vez la etiqueta de arriba, el total y el botón. |

Paleta y texto son decisiones separadas: el oliva de A se puede usar con el texto de B y al revés.

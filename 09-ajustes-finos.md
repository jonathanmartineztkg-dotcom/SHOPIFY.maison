# Ajustes finos del 21/9 — segunda tanda

Pedidos de Jony después de publicar la primera tanda. Todo verificado sobre la vista previa.

## Estado

**Ojo con la secuencia:** el tema "Jonathan Martinez — cambios 21/9" (`153534988378`)
**ya está publicado**. Estos ajustes van en una copia nueva, porque Shopify bloquea escribir sobre
el tema en vivo.

| | |
|---|---|
| Tema a publicar | **"Maison — ajustes 21/9 (2)"**, ID `153536299098`, sin publicar |
| Vista previa | `https://maisonmeszarics.com/?preview_theme_id=153536299098` |
| En vivo ahora | `Jonathan Martinez — cambios 21/9` (`153534988378`) |
| Guardado por si acaso | `Jonathan Martinez` (`152283250778`), el de antes de todo |

Publicar desde **Tienda online → Temas**. Si algo no gusta, se vuelve publicando el anterior.

---

## 1. El título: Barlow Condensed **se sacó**

Se probó primero en 700 y después en 500, y Jony la descartó. **Los títulos volvieron a Figtree
800, exactamente como estaban.**

Se quitó de los dos lugares donde vivía: el bloque de tipografía de `assets/mm-cambios.css` —
incluidos los tamaños de 3,9 y 6,6 rem, que solo existían para compensar que una condensada se ve
más chica— y la familia en la URL de Google Fonts de `layout/theme.liquid`. La tienda vuelve a
cargar solo Figtree y Cormorant.

Queda un comentario en el CSS avisando que, si algún día se retoma, hay que tocar **los dos lugares
a la vez**: si el peso del CSS y el de la URL no coinciden, el navegador falsea el grosor y se ve
sucio.

Las tres direcciones tipográficas que quedaron sobre la mesa están en el lienzo
`Maison — tres tipografías para la home`.

## 2. Las fotos de la home, con modelo

Las 8 fotos de las dos secciones de abajo pasan de short suelto a modelo. Ya no queda ninguna foto
de producto solo en la home.

| Sección | Antes | Ahora |
|---|---|---|
| Ficha "Los ocho colores" | cian suelto | cian con modelo |
| Ficha "¿Cuál es tu talla?" | gris negro suelto | gris negro con modelo |
| Ficha "De qué está hecho" | gris oscuro suelto | café de espaldas con modelo |
| Ficha "Envío y garantía" | azul suelto | púrpura con modelo |
| Color Rosa | rosa suelto | rosa con modelo |
| Color Café | café suelto | café de frente con modelo |
| Color Púrpura | púrpura suelto | púrpura con modelo |
| Color **Gris claro → Gris Negro** | gris claro suelto | gris negro con modelo |

**Dos decisiones que conviene saber:**

- **El cuarto color cambió de Gris claro a Gris Negro.** Gris claro no tiene foto de modelo, así que
  o quedaba el único con short suelto, o se cambiaba por un color que sí la tiene. Se cambió.
  Cuando existan las fotos de azul, gris claro y gris oscuro esto se puede volver atrás.
- Hay **6 fotos de modelo para 8 lugares**, así que púrpura y gris negro aparecen dos veces, en
  secciones distintas. Es lo mínimo posible hasta tener las 3 que faltan.

También se cambió la foto de `mm_cierre`: usaba la vieja de 1600×2000 y ahora usa la nueva de
3277×4096. Era la foto de peor calidad de toda la tienda.

## 3. El redondeo, más sutil

De **8 px a 4 px**. A 8 px sobre un botón de 50 px de alto se leía como pastilla; a 4 px apenas se
insinúa. Sigue siendo un solo número, `--mm-radio`, arriba del CSS.

Se sumó el **botón de consultar por WhatsApp** de la ficha (`.mm-wa-inline`) para que no quede
desparejo con el de comprar. **El flotante no se tocó**, por la regla del proyecto de no moverlo sin
que lo pida Jony — y además una pastilla flotante conviene que siga siendo pastilla.

## 4. El botón del héroe, menos ancho

En celular dejaba de ir de borde a borde: ahora **28 rem centrado**, con 46 px de alto en vez de 50.

El diagnóstico era que el bloque es mucho más grande que su contenido (50 px de alto para un texto
de 14,5 px), y por eso se leía como una barra blanca. Meterlo para adentro y bajarle el alto lo
devuelve a proporción de botón. En escritorio no cambia: ya tenía un tope de 32 rem.

## 5. Líneas finas en la descripción

Dos cosas, las dos con líneas muy claras:

- **Marco**: una línea arriba y otra abajo del bloque de la descripción, en `--mm-hair` (`#e8dcde`).
- **Separadores**: las 4 características del listado ("Diseño de cintura alta", "Tecnología sin
  costuras", etc.) pasan de viñetas a estar separadas por una línea, en `rgba(23,17,15,.09)`.

Es lo que los acordeones perdieron cuando se les sacaron las líneas: estructura de lista.
Si las viñetas se extrañan, se borra el bloque 4 del CSS y vuelven.

---

## Cómo se revisó

Sobre la vista previa del tema nuevo, no supuesto:

- Los **8 colores** uno por uno: cada uno sigue mostrando solo sus fotos, modelo primero y producto
  al final. Azul, gris claro y gris oscuro con una sola foto y sin flechas.
- La home **no carga ninguna foto de short suelto**: las 6 que trae son todas de modelo.
- La página ya no menciona Barlow por ningún lado, y el CSS servido no trae ninguna regla de
  tipografía. La URL de Google Fonts volvió a pedir solo Figtree y Cormorant.
- Las 6 reglas nuevas llegaron al CSS servido, que Shopify minifica.
- La descripción del producto tiene sus 4 `<li>`, que son los que reciben los separadores.

# Resumen general — qué se hizo y dónde estamos

## Estado hoy (21 de septiembre de 2026)

- **2 ventas** desde los anuncios: $58,68 (16/9) y $29,34 (19/9) → **$88,02 USD**.
- **$68,55 USD invertidos** en Meta en la campaña actual.
- Campaña activa, **solo el grupo de estáticos**, hasta el **27 de septiembre**.
- Tienda con fotos nuevas en alta calidad y la ficha rediseñada.

## Línea de tiempo

### Agosto — primera prueba y diagnóstico
- Primera campaña (25–31/8): $69,72 invertidos, 143 visitas, 5 carritos, 0 ventas.
- Google Analytics mostró que **el 89 % de las visitas no bajaba en la ficha del producto**.
  La ficha no era larga, era **vacía**: no había motivos para creer arriba del botón de compra.
- Meta le dio el 95 % del presupuesto a un solo anuncio; los otros nunca se probaron.
- Se arreglaron cosas de base: velocidad (de 4,1 s a 0,8 s), políticas, envío gratis,
  textos en inglés que habían quedado de la plantilla.

### 31/8 al 3/9 — rediseño de la tienda
- **Ficha de producto** rediseñada tomando como referencia la estructura de Popflex:
  garantía donde otras tiendas ponen estrellas, ayuda de talla por WhatsApp arriba del botón,
  envío gratis en una línea, foto 4:5 a sangre, colores como círculos con el color real.
- **Home** reconstruida siguiendo la estructura de Cakes Body, con la identidad de Maison:
  héroe → garantías → 4 fichas temáticas → elige tu color → cierre con botón de compra.
- **Pie de página** nuevo siguiendo la estructura de teveo.com, pensado primero para celular.
- Auditoría completa de la tienda: errores de enlaces, voseo, páginas vacías.

### 1–2/9 — propuesta al cliente y accesos
- Reporte de la semana 1 en PDF, propuesta de 3 planes, guía visual para dar acceso a Instagram.

### 8–10/9 — campaña "Video vs Estáticos"
- Dos grupos de $5/día: estáticos (3 anuncios) y video (1 anuncio).
- CTR altísimo (4–5 %; el rubro anda en 1–2 %), visita a menos de 5 centavos de dólar.
- Pero **0,4 % de las visitas agregaba al carrito**. El problema seguía estando en la tienda.
- Diagnóstico: **las fotos**. Ninguna mostraba el short puesto en un color que se vendiera;
  la mitad eran fotos de catálogo del proveedor (piso sucio, un palo de madera en la esquina).
- **Se pausó la campaña el 10/9** para no gastar en una página que no convertía.

### 11–15/9 — fotos nuevas
- 8 fotos de producto (una por color) + 2 de modelo, generadas con IA y retocadas.
- Primero se subieron en 2048 px y se veían borrosas. Causa real: **el tema pedía versiones
  demasiado chicas** para el recorte 4:5. Se corrigió el tema y se re-subieron en 4096 px.
- Galería final: modelo café (portada), modelo rosa, y los 8 colores. Cada color muestra su foto.
- Home actualizada con las fotos nuevas.

### 14/9 en adelante — reactivación
- Reactivada el 14 a las 18:38 hora de México.
- Después del cambio de fotos, las visitas que agregan al carrito pasaron de **0,4 % a ~1,3 %**
  en promedio (2,5 % los dos primeros días).
- **Primera venta el 16/9** ($58,68), del anuncio "Garantía 7 días".
- 17/9: se pausó el grupo de video (171 visitas sin un carrito) y se extendió la campaña al 27/9.
- **Segunda venta el 19/9** ($29,34).

### 20/9 — fotos de modelo nuevas y el redondo de la M
- Llegaron **6 fotos de modelo** (café de frente y de espaldas, rosa, púrpura, cian y gris negro).
  Traían el sello **"Ai"** en la esquina: se les quitó, se recortaron a 4:5 y quedaron en el tamaño
  que acepta Shopify (las originales, de 38,5 MP, no se podían subir). Están en `fotos-tienda/`.
  Los colores se confirmaron cruzándolos con las fotos limpias que ya están en la tienda.
- Todavía faltan tres colores con modelo: **azul, gris claro y gris oscuro**.
- Se cerró el punto que estaba abierto del **logo animado**: va como SVG en el encabezado (1,9 KB,
  no un video) y el video queda para el Reel y la portada de Facebook. Todo en `marca/` y
  explicado en `06-logo-redondo.md`.

### 21/9 — las fotos entraron a la tienda
- Las 6 fotos de modelo **ya están subidas** al producto, con su texto alternativo cargado.
- Se les asignó la foto de modelo a las **20 variantes** de los 5 colores que la tienen
  (café, rosa, púrpura, cian y gris negro). Azul, gris claro y gris oscuro siguen con la foto limpia.
- Se cargó el texto alternativo también en las **10 fotos que ya estaban** (venían todas vacías).
  Con eso queda destrabado el filtro de galería por color del cambio 1.
- La galería del producto pasó de 10 a **16 fotos**. Se van a ver todas hasta que se programe el
  filtro por color.
- Propuestas para la home, la barra de arriba con carrusel y el descuento: `07-home-y-banner.md`.

### 21/9, segunda vuelta — la ficha
- **Se encontró por qué la galería mezclaba colores**: el ajuste `hide_variants` del tema muestra
  siempre las fotos que no están asignadas a ninguna variante. Al pasar las variantes a las fotos
  nuevas, las dos de modelo viejas quedaron sueltas y aparecían en todos los colores. Por eso,
  eligiendo café, salía una modelo de rosa.
- Escrito el filtro de galería por color (`marca/product-media-gallery.liquid`): primero las fotos
  de modelo de ese color, después la limpia, y sin deslizar cuando hay una sola.
- Más cambios de CSS listos para pegar: botón del héroe redondeado, garantías en una sola fila en
  celular, fuera las líneas de los acordeones.
- Tipografía nueva para los títulos grandes, medida contra el título real: **Barlow Condensed 700**,
  un 20 % más angosta que Figtree. Comparación en `marca/comparacion-tipografias.png`.
- Todo explicado en `08-ficha-y-tipografia.md`.

## Lo que se aprendió (vale para lo que venga)

1. **El mensaje que vende es la garantía**: "si no te queda, te devolvemos tu dinero".
   Le gana al precio y al envío gratis por mucho.
2. **El freno estaba en la tienda, no en el anuncio.** El tráfico siempre fue barato y abundante.
3. **Las fotos del producto puesto, en colores reales, cambian la conversión.**
4. En Meta, **tocar un anuncio o un presupuesto reinicia el aprendizaje**. Cambiar la tienda no.

## Pendientes abiertos

- Despachar los pedidos y conseguir seguimiento (la proveedora es Abby, de Commercive).
- Abby tiene que confirmar si tiene **línea DDP a México** (ellos resuelven la aduana).
  De eso depende si hace falta pedir RFC/CURP en el checkout.
- Voseo que quedó en la guía de tallas, envíos, devoluciones y rastreo (13 casos).
- 4 páginas heredadas vacías publicadas (`/pages/the-maison` dice "Editorial copy pending").
- El botón flotante de WhatsApp dice "Escribinos" (voseo). **No se toca** hasta que lo diga Jony.
- Cambios de diseño nuevos: ver `05-proximos-cambios.md`.
- Instalar el redondo de la M en el tema: ver `06-logo-redondo.md`.
- Decidir el descuento (A, B o C de `07-home-y-banner.md`) **con el cliente**: toca el margen.
- Programar el filtro de galería por color: ya están los textos alternativos, faltan las 3 fotos
  de modelo de azul, gris claro y gris oscuro.

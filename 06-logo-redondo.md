# El redondo de la M — plan y piezas listas

Cierra el punto 5 de `05-proximos-cambios.md` ("video corto con la M o el nombre"), que había
quedado abierto porque no estaba definido dónde iba.

**Lo pedido:** un redondo con la **M de la marca en blanco**, **chico**, con movimiento, para que la
tienda se vea de más calidad.

---

## La decisión de fondo: en la tienda no va un video

Un video de 1–2 s arriba de todo cuesta entre 300 KB y 1 MB, tarda en decodificar y el navegador lo
pinta después del primer cuadro. La página hoy carga en **0,55–0,82 s** y eso es parte de por qué
convierte. Un video en el encabezado se lleva puesto ese número.

**El mismo efecto se consigue con SVG + CSS: 1,9 KB, sin pedir nada al servidor.** La M se dibuja
sola en poco más de un segundo y queda fija. Eso es lo que está armado en `marca/`.

El **video sí existe**, pero para donde hace falta un archivo de video: el Reel de Instagram y la
portada de la página de Facebook. Misma animación, exportada.

Recordatorio de `05-proximos-cambios.md`: **Instagram y las páginas de Facebook no aceptan video
como foto de perfil.** Para perfil va la M fija, sacada del mismo dibujo, así todo queda igual.

---

## Qué hay en `marca/`

| Archivo | Para qué |
|---|---|
| `mm-logo-m.svg` | La M fija sobre disco negro `#17110f`. El original de todo |
| `mm-logo-m-rosa.svg` | La misma sobre disco rosa `#b97c8c` (alternativa) |
| `mm-logo-m-animado.svg` | Se anima sola, sirve hasta metida en un `<img>` |
| `mm-logo-m.liquid` | El snippet para el tema (es el que va al encabezado) |
| `mm-logo-m.css` | El bloque de estilos que acompaña al snippet |
| `mm-logo-m-1024/512/180.png` | La M con fondo transparente fuera del disco |
| `mm-perfil-1024.png`, `mm-perfil-320.png` | **Foto de perfil** de Instagram y Facebook (cuadrado lleno) |
| `mm-perfil-rosa-1024.png` | La misma en rosa |
| `mm-logo-animacion-1080.mp4` | 1080×1080, 2,6 s, 45 KB — Reel de Instagram y portada de Facebook |
| `vista-previa.html` | Se abre en el navegador y muestra el redondo en todos sus tamaños |

El dibujo es el mismo en las tres formas (SVG, PNG, video): mismo trazo, mismas proporciones, mismo
blanco `#fdf9f8`. La foto de perfil es literalmente el primer cuadro de la animación.

---

## Cómo se ve y cómo se comporta

- **Disco negro casi café `#17110f`**, el mismo de los botones; M en blanco crema `#fdf9f8`.
- Aro fino al 16 % de opacidad, apenas insinuado. Es lo que le da el aire de sello.
- **Trazo de 5,2 sobre 100**: fino, con las puntas en ángulo (no redondeadas), como los botones
  cuadrados de la tienda. Se lee bien hasta en 46 px — está probado.
- **Tamaño**: 46 px en celular, 56 px en escritorio. Chico, como se pidió.
- **La animación:** el disco entra (0,45 s) y la M se dibuja de un trazo (1,05 s). Total ~1,5 s.
- **Se dibuja una vez por visita**, no en cada página: la segunda página ya la muestra quieta.
  Se guarda en `sessionStorage`. Un logo que baila en cada clic cansa y se ve barato.
- **Respeta "reducir movimiento"** del teléfono: quien lo tiene activado ve la M terminada.
- **Si el JavaScript no corre, se ve la M terminada.** Nunca queda a medias ni invisible.
- No mueve nada de la página al entrar (no hay salto de diseño): el espacio ya está reservado.

---

## Cómo se instala en el tema

```bash
cd C:\Users\acer\maison-trabajo
shopify theme pull --store an7i08-cf.myshopify.com --theme 152283250778
```

1. Copiar `marca/mm-logo-m.liquid` a `snippets/mm-logo-m.liquid`.
2. Pegar el contenido de `marca/mm-logo-m.css` **al final** de `assets/mm-custom.css`.
3. En `sections/header.liquid`, donde hoy se imprime el logo del encabezado, poner:

   ```liquid
   {% render 'mm-logo-m', size: 46 %}
   ```

4. Subir **completo**, nunca con `--only`:

   ```bash
   shopify theme push --store an7i08-cf.myshopify.com --theme 152283250778 --allow-live
   ```

5. Revisar en un celular real (ver "Trampas" en `03-tienda-diseno.md`, punto 8).

Cosas del tema a tener en cuenta:

- Shopify **minifica el CSS** al servirlo. Para confirmar que la subida llegó, buscar
  `mm-logo-primera-vez` en el CSS servido, no los comentarios.
- El snippet imprime su propio `<script>`. Si se lo renderiza dos veces en la misma página
  (encabezado y pie), el script corre dos veces: es inofensivo, pero conviene pasar
  `animar: false` en el segundo.

---

## Fuera de la tienda

| Dónde | Qué archivo | Nota |
|---|---|---|
| Foto de perfil de Instagram | `mm-perfil-1024.png` | Instagram recorta en círculo; el aro queda adentro |
| Foto de perfil de Facebook | `mm-perfil-1024.png` | El mismo, para que se vean iguales |
| Portada de la página de Facebook | `mm-logo-animacion-1080.mp4` | Facebook sí acepta video de portada |
| Reel o historia destacada de Instagram | `mm-logo-animacion-1080.mp4` | Se le puede sumar música y una foto del short al final |
| Favicon de la tienda | `mm-perfil-320.png` | Configuración → Marca, en el admin de Shopify |
| Correos de Shopify | `mm-logo-m-512.png` | Configuración → Notificaciones |

El MP4 tiene fondo crema opaco, que es lo que piden Instagram y Facebook. Si alguna vez hace falta
la animación **sobre una foto** (el redondo encima de la modelo, por ejemplo), hay que exportarla
con transparencia desde `mm-logo-m-animado.svg`: no está hecha porque hoy no se usa en ningún lado.

---

## Lo que falta decidir

1. **¿El redondo reemplaza al logo de texto del encabezado, o va al lado?**
   Recomendación: en celular **solo el redondo** (gana lugar arriba, que es donde se decide la
   compra); en escritorio el redondo **más** "MAISON MESZARICS" al lado, en Figtree con
   `letter-spacing` amplio, como la barra de anuncio.
2. **¿Disco negro o rosa?** Negro `#17110f` es más rotundo y pega con los botones. El rosa
   `#b97c8c` es más suave pero compite con la barra de anuncio, que ya usa ese rosa.
   Recomendación: **negro**.
3. **¿La M así o con la itálica de Cormorant?** La M dibujada tiene el trazo parejo y fino, se lee
   en 46 px y no depende de que cargue ninguna fuente. Una M de Cormorant itálica sería más "voz de
   marca", pero a 46 px la itálica serif se ensucia. Recomendación: **dejar esta**.
4. **¿Va también en el pie de página?** Queda bien, quieto y en 40 px, arriba del correo.

---

## Lo que no se va a hacer

- **Pantalla de carga con la animación.** Ya estaba descartado en `05-proximos-cambios.md` y sigue
  descartado: frena la entrada y baja las ventas.
- **Video en el encabezado.** Por lo del principio: el peso no se justifica.

---

## Cómo saber si sirvió

El redondo no se mide con ventas: es identidad, el efecto es lento y chico.
Lo único que sí hay que medir es que **no haya costado velocidad**: tomar el tiempo de carga antes
y después de subirlo. Tiene que seguir entre **0,55 y 0,82 s**. Si subió, algo se instaló mal.

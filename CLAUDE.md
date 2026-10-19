# CLAUDE.md — solucloud-theme-monokai

> Repo **público**. No escribir aquí contraseñas, IP, NIT, nombres de clientes
> ni datos internos.

## Variables (PROTOCOLO-ENTREGAS)
| Variable | Valor |
|---|---|
| `<REPO>` | `/opt/odoo-docker/addons/solucloud-theme-monokai` |
| `<BASE>` | `tienda_odoo` (pruebas) |
| `<DOMINIO>` | `iaguatemala.click` |
| `<MODULOS>` | `website_solucloud_market` |
| `<TAGS>` | `/website_solucloud_market` |
| Rama estable / de pruebas | `18.0` / `test` |

## Qué es
Módulo `website_solucloud_market`: apariencia tipo marketplace (referencias:
GuatemalaDigital, Pacifiko, Cemaco, Kemik, Amazon; inspiración, no copia) sobre
la tienda **nativa** de Odoo 18 (`website_sale`). Identidad **"Atardecer"**
(docs/MARCA.md), **solo modo claro**.

## Decisiones
- **Sin tema de terceros.** Theme Boec se descartó (oct-2026): lento al cambiar
  de página, encabezado imposible de rehacer limpiamente, JS duplicado. El repo
  espejo `castellanosi/theme_boec` queda solo como referencia.
- Módulo normal de Website (categoría `Website/Website`, no `Theme`).
- El encabezado **hereda de `website.template_header_default`** (priority 99) y
  reemplaza `div#o_main_nav`. Si alguien elige otro encabezado en el editor,
  el nuestro deja de aplicarse sin romper nada.
- 3 filas en escritorio: barra oscura (mensaje + menú del sitio) · logo +
  buscador grande (productos, va a `/shop`) + cuenta + carrito · barra con las
  12 primeras categorías raíz de la tienda.
- Móvil: buscador de productos siempre visible bajo el logo.
- Activa la opción estándar `website_sale.products_add_to_cart` (botón de
  carrito en cada tarjeta). Se puede apagar desde el editor.
- Colores solo en `static/src/scss/market_tokens.scss`, documentados en
  `docs/MARCA.md` (mantener ambos sincronizados).
- Dos degradados: **Vivo** (decorativo, sin texto pequeño) y **UI/Compra**
  (texto blanco, todos sus tonos pasan AA ≥ 4.5). Botón primario `#E11D48` (4.7).
- Una sola fuente (Inter) por velocidad. No agregar fuentes ni librerías JS.
- Carruseles y banners = bloques NATIVOS del editor (Carrusel, Productos),
  solo se estilizan con CSS. Clases utilitarias: `mk-bg-gradient`, `mk-banner`.
- Categorías en círculos = tira nativa de `/shop` (`o_wsale_filmstip`) con CSS.

## Trampas
- **No cambiar el encabezado desde el editor** (Tema → Encabezado): eso
  desactiva `template_header_default` y con él nuestro diseño.
- Tras `chown -R 100:101` git dice "dubious ownership": usar
  `git config --global --add safe.directory <REPO>` (una vez por servidor).
  No devolver los permisos a root.
- Odoo pinta algunos detalles con su color primario (morado por defecto). Lo
  correcto es fijar la paleta en el editor: Tema → Colores (ver README); el
  SCSS solo corrige los puntos visibles más comunes.
- El logo se cambia en el editor (clic en el logo) o en Ajustes del sitio.
- Las categorías de la barra son las **raíz** (sin padre) publicadas en el sitio.

## Estado
- 18.0.1.0.0: primera versión. Pruebas en `tests/test_market.py` (4):
  filas del encabezado, buscador a `/shop`, barra de categorías, botón de carrito.
- 18.0.1.1.0: solo CSS. Logo más grande, botón "Todas las categorías" legible,
  un solo buscador (se oculta el interno de /shop y de la ficha), filtros sin
  caja vacía, paginación y +/- en naranja, íconos sociales visibles en el pie.
- 18.0.1.2.0: identidad Atardecer (reemplaza la paleta Monokai), una sola
  fuente, categorías en círculos, estilos de carruseles/banners, íconos sociales
  corregidos (el círculo es el `<i>`), logo 64/44 px, manual de marca en docs/.
  Prueba nueva: solo se carga Inter (5 pruebas).
- Antes hubo `website_boec_monokai` (capa sobre Boec): nunca se fusionó; se
  desinstaló junto con Boec.

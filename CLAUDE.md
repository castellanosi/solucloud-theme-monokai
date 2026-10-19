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
GuatemalaDigital, Pacifiko, Cemaco, Kemik, Amazon) sobre la tienda **nativa**
de Odoo 18 (`website_sale`). Paleta Monokai Pro Light, **solo modo claro**.

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
- Colores solo en `static/src/scss/market_tokens.scss`. Contraste AA verificado:
  botón naranja 4.65, precio verde 5.1, enlaces azul 5.2.

## Trampas
- **No cambiar el encabezado desde el editor** (Tema → Encabezado): eso
  desactiva `template_header_default` y con él nuestro diseño.
- El logo se cambia en el editor (clic en el logo) o en Ajustes del sitio.
- Las categorías de la barra son las **raíz** (sin padre) publicadas en el sitio.

## Estado
- 18.0.1.0.0: primera versión. Pruebas en `tests/test_market.py` (4):
  filas del encabezado, buscador a `/shop`, barra de categorías, botón de carrito.
- Antes hubo `website_boec_monokai` (capa sobre Boec): nunca se fusionó; se
  desinstaló junto con Boec.

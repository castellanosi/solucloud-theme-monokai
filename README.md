# solucloud-theme-monokai

Apariencia **tipo marketplace** para una tienda Odoo 18 Community, sobre la tienda
nativa (`website_sale`), sin temas de terceros. Paleta inspirada en **Monokai Pro Light**.

| Módulo | Qué hace |
|---|---|
| `website_solucloud_market` | Encabezado de 3 filas (barra superior con el menú · logo + buscador grande de productos + cuenta + carrito · barra de categorías), buscador visible en móvil, tarjetas de producto con botón de carrito, precios en verde monoespaciados, pie oscuro con la franja de colores Monokai. |

## Requisitos
- Odoo 18.0 Community con `website_sale`.
- Encabezado del sitio en la opción estándar (*Tema → Encabezado → Predeterminado*).

## Personalizar colores
Editar solo `website_solucloud_market/static/src/scss/market_tokens.scss`.

## Créditos y licencia
- Paleta inspirada en Monokai Pro (monokai.pro); no incluye código de Monokai Pro.
- AGPL-3.

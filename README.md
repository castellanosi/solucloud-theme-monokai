# solucloud-theme-monokai

Apariencia **tipo marketplace** para una tienda Odoo 18 Community, sobre la tienda
nativa (`website_sale`), sin temas de terceros. Identidad visual **"Atardecer"**: ver [docs/MARCA.md](docs/MARCA.md).

| Módulo | Qué hace |
|---|---|
| `website_solucloud_market` | Encabezado de 3 filas (barra superior con el menú · logo + buscador grande de productos + cuenta + carrito · barra de categorías), buscador visible en móvil, tarjetas de producto con botón de carrito, categorías en círculos, estilos para banners y carruseles nativos, precios destacados y pie oscuro con franja de degradado. |

## Requisitos
- Odoo 18.0 Community con `website_sale`.
- Encabezado del sitio en la opción estándar (*Tema → Encabezado → Predeterminado*).

## Paleta de Odoo (hacer una vez en el editor)
Sitio web → Editar → **Tema** → **Colores**:
| Color | Valor |
|---|---|
| Color 1 (primario) | `#E11D48` |
| Color 2 (secundario) | `#6B3FE0` |
| Color 3 (claro) | `#F6F4FB` |
| Color 4 (blanco) | `#FFFFFF` |
| Color 5 (oscuro) | `#1B1530` |

## Marca
Colores, degradados, tipografía, formas, logo, medidas de banners e imágenes:
**[docs/MARCA.md](docs/MARCA.md)** · tablero: `docs/marca/tablero-marca.png`.

## Personalizar colores
Editar solo `website_solucloud_market/static/src/scss/market_tokens.scss`.

## Créditos y licencia
- AGPL-3.

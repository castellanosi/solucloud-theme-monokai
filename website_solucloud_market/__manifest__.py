# -*- coding: utf-8 -*-
# Apariencia tipo marketplace para la tienda SoluCloud (Odoo 18 CE nativo).
# No depende de ningún tema: hereda las plantillas estándar de website y
# website_sale. Identidad visual "Atardecer" (ver docs/MARCA.md).
{
    "name": "SoluCloud Marketplace",
    "version": "18.0.1.2.0",
    # Categoría normal (no "Theme") a propósito: se instala desde Apps o por
    # comando y sus vistas aplican a todos los sitios.
    "category": "Website/Website",
    "summary": "Encabezado tipo marketplace con buscador grande, barra de "
    "categorías y tarjetas de producto (identidad Atardecer)",
    "author": "SoluCloud",
    "depends": ["website_sale"],
    "data": [
        "views/header_templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "website_solucloud_market/static/src/scss/market_tokens.scss",
            "website_solucloud_market/static/src/scss/market_skin.scss",
        ],
    },
    "license": "AGPL-3",
    "installable": True,
    "application": False,
    "auto_install": False,
}

from odoo.tests import HttpCase, tagged


@tagged("post_install", "-at_install")
class TestMarketHeader(HttpCase):
    """El encabezado marketplace debe verse en la tienda."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.categ = cls.env["product.public.category"].create(
            {"name": "Categoria Prueba MK"}
        )

    def _shop_html(self):
        response = self.url_open("/shop")
        self.assertEqual(response.status_code, 200)
        return response.text

    def test_header_rows_present(self):
        html = self._shop_html()
        for css in ("mk-topbar", "mk-mainbar", "mk-catbar", "mk-mobile-search"):
            self.assertIn(css, html, "Falta %s en el encabezado" % css)

    def test_search_goes_to_shop(self):
        html = self._shop_html()
        self.assertIn('data-search-type="products"', html)
        self.assertIn('action="/shop"', html)

    def test_category_bar_lists_root_categories(self):
        html = self._shop_html()
        self.assertIn("Categoria Prueba MK", html)
        self.assertIn("/shop/category/", html)

    def test_add_to_cart_option_active(self):
        view = self.env.ref("website_sale.products_add_to_cart")
        self.assertTrue(view.active)

    def test_single_brand_font(self):
        html = self._shop_html()
        self.assertIn("family=Inter", html)
        self.assertNotIn("JetBrains", html, "Solo debe cargarse la fuente Inter")

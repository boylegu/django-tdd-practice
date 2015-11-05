from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')        # resolve 判断这个url的对应的视图是否存在
        self.assertEqual(found.func, home_page)

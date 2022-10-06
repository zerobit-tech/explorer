from django.test import TestCase, override_settings
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from django.conf import settings

from django.test.utils import override_settings    
@override_settings(  BATCH_TRANSATION_POSTING=False)
class TestCsrfCookieName(TestCase):
    def test_csrf_cookie_name_in_context(self):
        self.user = User.objects.create_superuser('admin', 'admin@admin-fake.com', 'pwd')
        self.client.login(username='admin', password='pwd')
        resp = self.client.get(reverse('explorer_index'))
        self.assertTrue('csrf_cookie_name' in resp.context)
        self.assertEqual(resp.context['csrf_cookie_name'], settings.CSRF_COOKIE_NAME)

    @override_settings(CSRF_COOKIE_NAME='TEST_CSRF_COOKIE_NAME')
    def test_custom_csrf_cookie_name(self):
        self.user = User.objects.create_superuser('admin', 'admin@admin-fake.com', 'pwd')
        self.client.login(username='admin', password='pwd')
        resp = self.client.get(reverse('explorer_index'))
        self.assertTrue('csrf_cookie_name' in resp.context)
        self.assertEqual(resp.context['csrf_cookie_name'], 'TEST_CSRF_COOKIE_NAME')

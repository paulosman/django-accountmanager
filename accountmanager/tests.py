from django.contrib.auth.models import User
from django.test import TestCase, Client

class AccountManagerTests(TestCase):

    test_username = 'testuser'
    test_password = 'testpassword'
    test_email = 'test@mozillafoundation.org'

    header_name = 'X-Account-Management-Status'

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(self.test_username,
                                             self.test_email,
                                             self.test_password)

    def _authorized_request(self, path, method='get'):
        self.client.login(username=self.test_username,
                          password=self.test_password)
        method = getattr(self.client, method)
        return method(path)
            
    def test_unauthorized_status_header(self):
        response = self.client.get('/')
        self.assertEqual('none', response[self.header_name])

    def test_authorized_status_header_no_fullname(self):
        response = self._authorized_request('/')
        header = response[self.header_name]
        status, id, name = header.split(';')
        self.assertEqual('active', status.strip())
        self.assertEqual('id="%s"' % (self.test_username,), id.strip())
        self.assertEqual('name=""', name.strip())

    def test_authorized_status_header_fullname(self):
        self.user.first_name = 'Test'
        self.user.last_name = 'User'
        self.user.save()
        response = self._authorized_request('/')
        header = response[self.header_name]
        status, id, name = header.split(';')
        self.assertEqual('active', status.strip())
        self.assertEqual('id="%s"' % (self.test_username,), id.strip())
        self.assertEqual('name="Test User"', name.strip())

    def test_host_meta_file_exists(self):
        response = self.client.get('/.well-known/host-meta')
        self.assertEqual('application/xrd+xml', response['Content-Type'])
        self.assertTrue(len(str(response)) > 0)
        self.assertTrue('rel="http://services.mozilla.com/amcd/0.1"'
                        in str(response))

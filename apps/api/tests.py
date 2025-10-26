from django.test import TestCase

class PingTestCase(TestCase):
    def test_ping_endpoint(self):
        response = self.client.get('/api/v1/ping/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'SIQNet API is alive!'})

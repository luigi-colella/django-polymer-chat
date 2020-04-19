from django.test import Client, TestCase


class ChatTests(TestCase):
    
    def test_homepage_is_rendered_correctly(self):
        """
        Check that homepage is rendered correctly.
        """
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

from django.test import TestCase

# Create your tests here.
class TestViews(TestCase):
    
    def test_get_home_page(self):
        page = self.client.get("/home/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "home.html")
    
    
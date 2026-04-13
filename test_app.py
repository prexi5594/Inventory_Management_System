import unittest
from app import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)

    def test_get_items(self):
        res = self.client.get("/items")
        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()
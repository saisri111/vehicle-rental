
import unittest
from app import app


class TestVehicleRental(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "healthy")

    def test_booking_form_has_vehicle_options(self):
        response = self.client.get("/")
        self.assertIn(b"Luxury Car", response.data)


if __name__ == "__main__":
    unittest.main()

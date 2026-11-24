import unittest

from app import app


class ServiceRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_only_three_route_paths_are_registered(self):
        paths = {rule.rule for rule in app.url_map.iter_rules()}

        self.assertEqual(paths, {"/", "/health", "/api/v1/message"})

    def test_root_serves_the_dashboard(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response.content_type)
        self.assertIn(b"Service health", response.data)
        self.assertIn(b"Message API", response.data)

    def test_health_route_reports_healthy(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "healthy"})

    def test_message_route_returns_a_message(self):
        response = self.client.get("/api/v1/message")

        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.get_json())


if __name__ == "__main__":
    unittest.main()

from django.test import TestCase
from django.test import AsyncClient

class TestApiWithClient(TestCase):
    async def test_api_with_async_client(self):
        client = AsyncClient()
        response = await client.get("/async/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["responses"][0]["location"]["city"], "Portland")
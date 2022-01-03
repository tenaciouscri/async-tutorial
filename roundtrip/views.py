import asyncio
import time
import httpx

from django.http import JsonResponse

BASE_URL = "https://weather.talkpython.fm/api/weather"
cities = ["portland", "berlin", "chicago", "madrid", "sidney"]

def weather_sync(request):
    responses = []
    for city in cities:
        res = http_call_sync(f"{BASE_URL}?city={city}")
        responses.append(res)
    
    result = {"responses": responses}
    return JsonResponse(result)

async def weather_async(request):
    tasks = []
    for city in cities:
        res = http_call_async(f"{BASE_URL}?city={city}")
        tasks.append(res)
    
    responses = await asyncio.gather(*tasks)
    result = {"responses": responses}
    return JsonResponse(result)

def http_call_sync(url):
    print(f"sync call to {url}...")
    time.sleep(1)
    r = httpx.get(url)
    return r.json()

async def http_call_async(url):
    print(f"async call to {url}...")
    async with httpx.AsyncClient() as client:
        await asyncio.sleep(1)
        r = await client.get(url)
        return r.json()
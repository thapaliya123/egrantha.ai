"""
Asynchronous fetch from multiple websites
"""
import asyncio
import aiohttp
import time

URLS = [
    "https://www.example.com",
    "https://www.google.com",
    "https://openai.com",
    "https://github.com"
]

async def fetch_data(url):
    print(url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
        

async def fetch_multiple_websites(urls):

    tasks = [fetch_data(url) for url in urls]

    responses = await asyncio.gather(*tasks)

    for url, response in zip(urls, responses):
        print(f"Data from {url}: {len(response)} characters")

async def main(urls):
    start_time = time.time()
    await fetch_multiple_websites(urls)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")


if __name__ == '__main__':
    asyncio.run(main(URLS))

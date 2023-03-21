import httpx
# import asyncio


class HttpClient(httpx.AsyncClient):
    def __init__(self):
        super().__init__()


# async def hello():
#     async with HttpClient() as client:
#         r = await client.get('https://httpbin.org/json')
#         print(r.text)

    
# if __name__=='__main__':
#     asyncio.run(hello())
from fastapi import FastAPI
from routers import router, request_client


app = FastAPI()
app.requests_client = request_client
app.include_router(router)

# Initialize in startup event
from fastapi_simple_cache import FastAPISimpleCache
from fastapi_simple_cache.backends.inmemory import InMemoryBackend

@app.on_event("startup")
async def startup_event():
    backend = InMemoryBackend()
    FastAPISimpleCache.init(backend)

    
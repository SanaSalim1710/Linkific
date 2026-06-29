from fastapi import FastAPI, BackgroundTasks, HTTPException, status, Request
import asyncio
import httpx
from fastapi import Depends 
from fastapi.middleware.cors import CORSMiddleware
import logging
import time

app = FastAPI()

origins = ["http://localhost:5000",
        "http://localhost:8000",
        "https://localhost:5000"
       ]
app.add_middleware(
    CORSMiddleware,
    # list of origins that should be allowed to make cross-origin requests
    allow_origins=origins, 
    # cookies are supported
    allow_credentials=True,
    # allow all standard HTTP methods
    allow_methods=["*"], 
    # all HTTP request headers are supported
    allow_headers=["*"], 
)

logger = logging.getLogger("logger")

@app.get("/")
async def hello_world():
    await asyncio.sleep(2)
    return {"message":"Hello World"}

'''@app.get("/todo")
async def get_todo():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/todos/1")
    return response.json()'''

'''@app.get("/todo")
async def get_todo(client: httpx.AsyncClient = Depends(get_http_client)):
    response = await client.get("https://jsonplaceholder.typicode.com/todos/1")
    return response.json()'''

async def fetch_data(client, url):
    try:
        response = await client.get(url, timeout=5.0)
        response.raise_for_status()
    except (httpx.HTTPStatusError, httpx.RequestError) as exc:
        return {"error": f"Failed to fetch data from {url}: {exc}"}
    return response.json()

@app.get("/todos")
async def get_todos():
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(
            fetch_data(client, "https://jsonplaceholder.typicode.com/todos/1"),
            fetch_data(client, "https://jsonplaceholder.typicode.com/todos/2"),
            fetch_data(client, "https://jsonplaceholder.typicode.com/todos/3")
        )
    return {"todo 1": results[0], "todo 2": results[1], "todo 3": results[2]}

def register_log(message):
    with open("log.txt","a") as f:
        f.write(f"{message}\n")

@app.post("/register")
async def register(background_tasks: BackgroundTasks):
    background_tasks.add_task(register_log,"New User Registered")
    return {"message":"Status: Successful Registration"}


@app.middleware("http")
async def log_request(request: Request, call_next):
    start = time.perf_counter()
    try:
        response = await call_next(request)
    except Exception as e:
        duration = (time.perf_counter() - start) * 1000
        logger.error(f"{request.url.path} crashed after {duration:.2f}ms | Error: {e}")
        raise e
    duration = (time.perf_counter()-start)*1000
    print(f"{request.url} took {duration:.2f} seconds")
    logger.info(f"{request.method} {request.url.path} completed in {duration:.2f}ms | Status: {response.status_code}")
    return response

async def verify_auth_token(api_key: str):
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing API Key"
        )
    if api_key != "secret-api-key":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )
    return {"user": "authenticated_user"}

@app.get("/secure-data")
async def get_secure_data(user: dict = Depends(verify_auth_token)):
    return {"message": f"Hello {user['user']}!"}


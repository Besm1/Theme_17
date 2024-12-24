from fastapi import FastAPI

from routers import tasks, users


app = FastAPI()

@app.get('/')
async def main():
    return {'message': 'Welcome to TaskManager'}

app.include_router(tasks.router)
app.include_router(users.router)
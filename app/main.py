from fastapi import FastAPI

from .app import create_application

app: FastAPI = create_application()

@app.on_event('startup')
async def startup():
    pass

@app.on_event('shutdown')
async def shutdown():
    pass
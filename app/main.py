from fastapi import FastAPI

from .app import create_application

app: FastAPI = create_application()

@app.on_event('startup')
async def startup():
    print('Application startup')

@app.on_event('shutdown')
async def shutdown():
    print('Application shutdown')
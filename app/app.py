from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def create_application():
    
    _app = FastAPI(
        debug=True,
        title="O'Mall Authorization Server",
        description="""
            Authorization server used for grant access for requests clients,
            sign up and log in users.
        """,
        version='0.0.0',
    )
    
    """
        El siguiente codigo habilita las solicitudes CORS a las peticiones entrantes,
        y acepta todos los metodos, cabeceras y determina que cabeceras se verán expuestas
        por el servidor
    """
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
        expose_headers=['']
    )
    
    return _app
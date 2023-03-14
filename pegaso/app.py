"""
Citas V2 Admin API OAuth2
"""
from fastapi import FastAPI

from config.settings import get_settings

#from .v2.autoridades.paths import autoridades

settings = get_settings()


# FastAPI
app = FastAPI(
    title="Pegaos V1",
    description="API de consulta de la BD SIBED para brindar información de los documentos encontrados a otros sistemas.",
)

# CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins.split(","),
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Paths
#app.include_router(autoridades)



@app.get("/")
async def root():
    """Mensaje de Bienvenida"""
    return {"message": "Bienvenido a Pegaso API de consulta de BD de SIBED del Poder Judicial del Estado de Coahuila de Zaragoza."}

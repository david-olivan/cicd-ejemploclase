"""
API Demo de CI/CD
"""
from fastapi import FastAPI

app = FastAPI(
    title="API Demo CI/CD",
    description="Una API para explicar conceptos de CI/CD",
    version="1.0.0"
)

@app.get("/")
def read_root():
    """Endpoint raíz - nos da la bienvenida"""
    return {"message": "Bienvenido a la API Demo de CI/CD con FastAPI"}

@app.get("/health")
def health_check():
    """Endpoint de salud - será utilizado para verificar el estado del servicio"""
    return{"status": "healthy"}

@app.get("/suma/{a}/{b}")
def suma(a: int, b: int):
    """Este endpoint suma dos números enteros"""
    return{"resultado": a * b}

@app.get("/info")
def get_info():
    """Este endpoint devuelve información de la API"""
    return{
        "nombre": "API Demo CI/CD",
        "version": "1.0.0",
        "framework": "FastAPI"
    }
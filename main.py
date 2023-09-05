from fastapi import FastAPI   # framework para crear API's
from fastapi import Response  # Clase que se usa para enviar respuestas desde los endpoints
import pandas as pd
import json
import numpy as np
import ast
from model import modelo_predict

app = FastAPI()

@app.get('/genero/{Año}')  
def genero(Anio: str):
    return 'Hola mundo'
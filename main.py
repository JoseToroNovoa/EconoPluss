from fastapi import  HTTPException
from fastapi import  FastAPI
import db


app = FastAPI()

@app.get("/registros/consultar/")
async def consultar_registros():
    registro = db.consultar_registro()
    return registro

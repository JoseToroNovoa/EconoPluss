from fastapi import  HTTPException
from fastapi import  FastAPI
import db

app = FastAPI()


from fastapi.middleware.cors import CORSMiddleware

origins = [
 "http://localhost.tiangolo.com",
"https://localhost.tiangolo.com",
"http://localhost",
"http://localhost:8080",
"https://ekonoapp01.herokuapp.com"
]
app.add_middleware(
CORSMiddleware, allow_origins=origins,
allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)


@app.get("/registros/consultar/")
async def consultar_registros():
    registro = db.consultar_registro()
    return registro


@app.post("/registros/crear/")
async def crear_registro(dato: db.registro):
    registro_creado= db.crear_registro(dato)

    if registro_creado:
        return {"mensaje": "Registro creado"}
    else:
        raise HTTPException(status_code= 400, detail= "Orden ya existe")
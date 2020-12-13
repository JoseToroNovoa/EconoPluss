from pydantic import BaseModel

class registro(BaseModel):
    id_r: int
    valor: int 
    tipo_registro: str
    clase_registro: str
    fecha: str
    nota: str


registros = {
    1: registro(id_r=1, valor=50000, tipo_registro="Gasto", clase_registro="Comida", fecha="22-11-2020", nota="Comida restaurante"),
    2: registro(id_r=2, valor=90000, tipo_registro="Gasto", clase_registro="Entrtenimiento", fecha="23-11-2020", nota="Salida a la playa")
    
}

lista_registros= []
def consultar_registro():

    for e in registros:
        lista_registros.append(registros[e])
    return lista_registros

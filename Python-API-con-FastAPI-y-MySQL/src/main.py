from fastapi import FastAPI
from typing import Optional
from database import db as connection
from database import User

app = FastAPI(title='Easy_Template',
            description='Template builder',
            version='1.0.0')



@app.on_event("shutdown")
def shutdown():
    if not connection.is_closed():
        connection.close()

@app.on_event("startup")
def startup():
    if connection.is_closed():
        connection.connect()
    connection.create_tables([User])
    #User.create_table()
    #rec1=User(name="Rajesh", age=21)
    #rec1.save()

@app.get("/")
async def main():
    return {"Hello": "Angel"}

# http://localhost:8000/user?nombre=Angel&apellido=Rodriguez
@app.get("/user")
async def usuarios(nombre: Optional[str] = None, apellido: Optional[str] = None):
    return {"nombre": nombre,"apellido": apellido}



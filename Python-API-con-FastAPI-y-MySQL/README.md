# Easy-Template
Un generador de codigo o texto para tareas repetitivas
en las que se repiten patrones o estructuras
que dependen de unos datos concretos


# Instalar entorno

## Instalar FastAPI

1. Instalar Python3 con el comando **brew install python3 --verbose**

2. Probarlo 
   - **python3 --version**
   - Creando un holamundo.py con **print("Hola mundo!")**
   - Ejecutarlo con python3 holamundo.py
2. Crear un ambiente virtual 
   - **virtualenv env -p python3**
   activar el entorno virtual
   **source env/bin/activate**


3. Crear proyecto Github usando token
   - Github -> Menu Derecha Setting -> Menu Izquierda Developer Settings 
     -> Personal Access tokens -> Generate new Token -> copiar token
   - En una carpeta del ordenador -> git clone <url https de repositorio>
   - Poner el usuario y password del token

4. Crear archivo main.py con esto
~~~
from fastapi import FastAPI
from typing import Optional
app = FastAPI()
@app.get("/")
def main():
    return {"Say": "Hello World !!"}
@app.get("/user")
def usuarios(nombre: Optional[str] = None, apellido: Optional[str] = None):
    return {"nombre": nombre,"apellido": apellido}
~~~

5. Iniciar FastAPI en blanco
   - pip3 install fastapi
   - pip3 install uvicorn
   - pip3 freeze > requirements.txt

6. Ejecutar servidor ASGI **uvicorn main:app --reload** 
reload es para cargar lo cambios en caliente
main en el nombre del archivo main.py 
y app es la variable de FastAPI

7. Testear
http://127.0.0.1:8000/
devuelve {"Hello":"World"}
http://127.0.0.1:8000/user?nombre=Ram%C3%B3n&apellido=Rodriguez
devuelve {"nombre":"Ramón","apellido":"Rodriguez"}

8. Crear docker
cd ruta/proyecto
**docker build --tag fastapi .**
**docker run -p 8000:8000 --name mi-api fastapi**

9. Comprobar el servidor
las rutas http://0.0.0.0:8000/ http://127.0.0.1:8000/ usando curl <url> 
Ejecutar la shell iteractiva del container
**docker run -it <NombreContainer> /bin/sh**
y **python --version** en la consola del container

-------------------

## Comandos docker:
**docker ps -a**
**docker container ls** 
**docker stop <container_name>**
**docker start <container_name>**
**docker stop $(docker ps -a -q)**
**docker rm -f $(docker ps -a -q)**
**docker volume prune**  
**docker image prune**
**docker volume ls**
**docker image ls**
**docker run -it <NombreImaagen> /bin/sh**
**docker  restart mysql-server**
**docker logs mysql-server**
**docker compose up -d (detach)**
**docker compose down -v (volume)**
**docker compose stop**
**docker compose start**
**docker-compose restart**
**docker-compose rm**
**docker compose logs**
**docker exec -it <container-id> /bin/bash**

----------------------

## Instalar MySQL

0. creamos docker compose 
descripcion de adminer y mysql

1. Crear las carpetas para los bind mounts de MySQL
Crear mysql/data mysql/log mysql/script
**mkdir -p ./{config,data,log}**
**chmod -R 777 ./mysql**

2. Levantar compose
La primera vez descargar las imagenes **docker compose pull**
y **docker compose up -d**  para levantar el contenedor
**-d** es detach o usar **ctrl+c**, **ctrl+d** para salir
 y **docker compose down -v**  para eliminar **-v** es el volumen


3. Carga inicial de datos

4. Comprobar carga inicial
desde linea de comandos
docker exec -it mysql /bin/bash
mysql -u root -p
show databases;

5. Comprobar carga inicial
url de adminer




## Configurar FAST API


1. variable de entorno

2. archivo deploy 


3. docuemntacion 
http://localhost:8000/docs

4. conectar a BBDD peewe


documentacion api


apt-get update && apt-get install -y mysql*
telnet mysql 3306
mysqladmin -h mysql -u root -p
mysqladmin -h mysql -u root -p ping
mysqladmin -h mysql -u root -p processlist




-----------------------

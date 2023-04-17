# Pytool
Script de escritorio para automatizar tareas reptitivas.

Buscar archivos con los siguiente filtros:
- comiencen
- terminen 
- contengan 
- por tamaño 
- encoding 
- por extension

# Iniciar APP (de forma rápida)

En Windows 
1. instalar python 3
2. ejecutar init.bat 

# Iniciar APP (paso a paso)

1. Comprobar que tenemos python 3
```
#En windows
python --version
#En Mac y Linux
python3 --version 
```

2. Iniciar entorno virtual
```
#En windows
python -m venv venv
#En Mac y Linux
python3 -m venv venv
```

3. Activar entorno virtual
```
#En windows
venv\Scripts\activate
#En Mac y Linux
source venv/bin/activate
```
Ahora, la consola comienza por (venv)
indicando que estamos en el entorno virtual


4. Instalar librería para ver el codec de los archivos ([charset-normalizer](https://charset-normalizer.readthedocs.io/en/latest/user/getstarted.html))
```
#Sin proxy
pip3 install charset-normalizer
#Usando el proxy proxy:8080
pip3 install --proxy=http://proxy:8080 charset-normalizer
```

6. Ejecutar main.py
```
#En Mac y Linux
venv/bin/python src/main.py
#En windows
python src/main.py
```


# Configurar entorno de desarrollo con VS Code

Activar el interperte de VS Code
Para que el interprete sea el del entorno virtual
y no el python del sistema
VSCode -> View -> Command palette -> Python Select Interpreter 
Ahora al iniciar un archivo con la extersion .py 
en la esquina inferior derecha pondra ver el interprete de venv


------------
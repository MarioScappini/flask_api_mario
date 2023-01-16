Instalacion
compilar aplicacion:
    docker build -t flask_api .

para correr la app
    docker run -p 5000:5000 flask_api

url de swagger
    http://127.0.0.1:5000/apidocs/
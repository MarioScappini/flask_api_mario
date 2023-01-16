Instalacion
compilar aplicacion:
    docker build -t flask_api .

para correr la app
    docker run -p 5000:5000 flask_api

url de swagger
    http://127.0.0.1:5000/apidocs/

La app es un sistema donde tenemos usuarios que poseen posts estos posts se pueden crear, modificar, eliminar y leer. Para acceder a los posts el usuario tiene que logearse con /auth/login este genera un token encriptado que se guarda en el dispositivo del usuario, cada vez que se realize una llamada relacionadas con los posts se utililza este token como parte de los parametros. para mas ejemplos visitar

https://api.postman.com/collections/17024383-0d491abc-f94e-44fa-bea9-ec216d245452?access_key=PMAT-01GPVZ04WANMXJ71EDDKGSYJS0
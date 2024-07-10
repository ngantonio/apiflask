# Apiflask - saludos

Descripción:

Se presenta una sencilla API-REST construida bajo *Flask*, utilizando como base de datos local a *SQLite*.

Se ha construido con un enfoque sencillo, dockerizando la api y exponiendo un C.R.U.D para un único Modelo llamado "Greeting", el cual permite agregar, modificar, eliminar, obtener uno o varios saludos,

Se exponen los siguientes Endpoints :


* GET **http://localhost:5000/saludos**: Obtiene todos los saludos almacenados en base de datos.

* GET **http://localhost:5000/saludos/id**: Obtiene el saludo almacenado en base de datos que corresponda con el id enviado, si no existe, regresa un 404.

* POST **http://localhost:5000/saludos/**: Crea un saludo con el siguiente body:
```
{
    "message":"Buenos dias",
    "language":"Español"
}
```
* PUT **http://localhost:5000/saludos/id**: Modifica el saludo almacenado en base de datos que corresponda con el id enviado, si no existe el registro, regresa un 404.

```
{
    "message":"Good Morning",
    "language":"Ingles"
}
```
* DELETE **http://localhost:5000/saludos/id**: Elimina el saludo almacenado en base de datos que corresponda con el id enviado, si no existe el registro, regresa un 404.



** Notas: 
1. El autributo "language" es un atributo opcional.
2. Se ha hecho uso de Flask-SQLAlchemy requerida en el documento de definición de la prueba y todas las librerias necesarias para desarrollar una api en Flask.
3. Se ha hecho uso de SQLite en lugar de PostgreSQL o MySQL debido a que solo se ha implementado un único modelo bajo el cual se hacen todas las operaciones, sin embargo utilizar alguno de los gestores mencionados anteriormente no representaría mayor dificultad mas que agregar un paso adicional en el docker-compose.
4. Para correr el proyecto es necesario tener instalado Docker.


## Corriendo la app

```bash
$ docker-compose up

```
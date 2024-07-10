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


** El autributo "lenguage" es un atributo opcional

## Corriendo la app

```bash
$ docker-compose up

```
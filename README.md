# capgemini-prueba-tecnica-2

- Autor: Adrián Celada
- Fecha: 01/07/2025

## Implementación de Arquitectura Pub/Sub
Se requiere implementar una pequeña prueba basada en el patrón Publicador/Suscriptor (Pub/Sub) que cumpla con los siguientes requisitos:

## Consideraciones
1.	Generación de Datos:
a.	Debe existir un Publisher que genere números aleatorios de manera periódica.
b.	Debe existir un Subscriber que recabe dichos datos eleve al cuadrado el resultado leído.

2.	Almacenamiento de Datos:
a.	El Subscriber debe almacenar los resultados en una base de datos.
b.	El tipo de base de datos queda a criterio del candidato.

3. El código debe estar dockerizado.

# Resolución
## Entorno de la solución

La aplicación se ha desarrollado en el siguiente entorno:
- Windows 10 Pro
- VSCode 1.101.2
- Docker 28.2.2
- Docker Compose: v2.37.1-desktop.1
- PostgreSQL 17.5
- mosquitto 2.0.14

## Ejecución

Para lanzar la solución hay que seguir estos pasos:
- Descargar el contenido del repositorio en tu local (git clone / download zip).

- Desde CMD/SHELL, navegar hasta la carpeta raíz del repositorio.

- Previamente, tener instalado Docker y el plug-in de Docker Compose en tu PC, en las versiones mencionadas arriba.

- Lanzar el comando:
    `docker compose up --build`

- Docker Compose comenzará a generar las imágenes de los contenedores, así como la creación de redes y volúmenes definidos en los dockerfile. Al usar ese comando, también se inicia la ejecución de cada contenedor.

## Evidencias

Una vez lanzados los contededores, se puede evidenciar el funcionamiento de la aplicación de varias maneras:

- Lanzar el siguiente comando para ver los contenedores en ejecución:
    `docker ps`

- Ver los logs en terminal o en una interfaz gráfica como Docker Desktop (Windows).

- Entrar en el container de PostgreSQL para ver si la tabla existe y los datos llegan realmente. Desde CMD:
    - `docker ps` -> para obtener el ID del container de PostgreSQL.
    - `docker exec -it <CONTAINER_ID> bash` -> lanzamos una terminal de bash dentro del container.
    - `psql -U postgres -d postgres` -> nos conectamos al servicio de PSQL del container.
    - `\dt` -> comprobamos que la tabla "results" existe.
    - `SELECT * FROM results;` -> si queremos ver todas las entradas de la tabla.
    - `SELECT * FROM results ORDER BY id DESC LIMIT 1;` -> si queremos ver la última.
    - `SELECT * FROM results ORDER BY id DESC LIMIT 1; \watch 5` -> si queremos ver la última en tiempo real (tasa de refresco de 5 segundos).

## Comentarios adicionales

El alcance de esta prueba es el de de un PoC para demostrar las capacidades de desplegar una aplicación multicontenedor. En consecuencia, la solución no contempla estas acciones:

- Testing.
- Creación de perfiles de usuario y cambio de contraseñas por defecto.
- Gestión de los puertos de las aplicaciones.
- Control de ciertos errores en las aplicaciones de publicación y suscripción.



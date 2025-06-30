# capgemini-prueba-tecnica-2

Autor: Adrián Celada
Fecha: 01/07/2025

# Enunciado:
## Implementación de Arquitectura Pub/Sub
Se requiere implementar una pequeña prueba basada en el patrón Publicador/Suscriptor (Pub/Sub) que cumpla con los siguientes requisitos:

### 1.	Generación de Datos:
a.	Debe existir un Publisher que genere números aleatorios de manera periódica.
b.	Debe existir un Subscriber que recabe dichos datos eleve al cuadrado el resultado leído.

### 2.	Almacenamiento de Datos:
a.	El Subscriber debe almacenar los resultados en una base de datos.
b.	El tipo de base de datos queda a criterio del candidato.

### 3. El código debe estar dockerizado.

# Resolución
## Entorno de la solución

- Se ha desarrollado la aplicación en SO Windows 10 Pro
- Se ha usado Docker Desktop como servicio de contenedores
- Docker Compose: versión recomendada ≥ 1.29.

- Conexión de red local: que no haya otro servicio ocupando los puertos TCP 1883 (MQTT) ni 5432 (PostgreSQL).

- Sistema operativo: cualquiera que soporte Docker Desktop (Windows 10/11 Pro, macOS ≥ 10.15, o distribuciones Linux compatibles con Docker Engine).

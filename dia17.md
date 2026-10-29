# Día 17: peticiones HTTP con Postman

## GET: parámetros en la URL
Envié una petición a:
https://postman-echo.com/get?fecha=2026-11-02&servicio=alisado

Los parámetros fecha y servicio viajaron en la URL.
El servidor los devolvió dentro de "args".
La respuesta fue 200 OK.

## POST: datos en el Body
Envié una petición a:
https://postman-echo.com/post

Configuré Body → raw → JSON con cliente, servicio, fecha y hora.
El servidor devolvió esos datos dentro de "json".
Probé cambiar la hora y el cliente y comprobé la respuesta.

## Encabezados
- Content-Type: application/json indica que el cuerpo enviado tiene formato JSON.
- Accept: application/json indica que aceptamos recibir una respuesta JSON.

## Recordatorio
Postman es el cliente que envía la petición.
Postman Echo devuelve lo recibido para practicar.
Esta prueba no reserva turnos reales.
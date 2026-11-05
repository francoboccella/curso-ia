# Día 20: polling y webhooks

## Polling
La automatización consulta periódicamente si hay novedades.
Cada cinco minutos equivale a 12 consultas por hora.
Puede consultar aunque no haya datos nuevos.

## Webhook
El sistema de origen envía una petición cuando ocurre un evento.
La automatización recibe el aviso en una URL configurada.

## Práctica realizada
Creé un Custom webhook en Make.
Envié desde Postman una petición POST con Body en formato JSON.

Primero recibí un error 400 porque faltaban comas.
Corregí el JSON y recibí código 200 con el texto Accepted.

Make detectó los campos id, cliente y servicio.
Después probé con Run once y comprobé estos datos:
- id: SOL-002
- cliente: Alan
- servicio: trenzas

Postman actuó como cliente HTTP y Make como servidor.
El escenario quedó inactivo; la prueba se ejecutó con Run once.

## Evitar duplicados
Guardar el identificador de un evento procesado ayuda a reconocer
reenvíos y evitar repetir la misma acción.
Agregar un campo id no implementa ese control automáticamente.
En esta práctica todavía no configuré un control de duplicados.

## Guardado
Guardé el escenario en Make y la petición en Postman.
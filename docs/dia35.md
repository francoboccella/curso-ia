# Día 35: comparación entre Make y n8n

## Objetivo

Documentar cómo reconstruí en n8n la recepción del formulario
de solicitudes que antes enviaba datos a Make.

## Funcionamiento en n8n

1. El formulario envía cliente y servicio mediante una petición POST.
2. Webhook recibe los datos dentro de body.
3. El primer Edit Fields extrae cliente y servicio.
4. El segundo Edit Fields conserva esos campos y agrega un mensaje.

## Equivalencias

| Función | Make | n8n |
|---|---|---|
| Organizar la automatización | Escenario | Workflow |
| Representar un paso | Módulo | Nodo |
| Recibir una petición | Custom Webhook | Webhook |
| Usar datos recibidos | Mapeo de campos | Expresiones y mapeo |
| Revisar los datos procesados | Inspección de la ejecución | Output de los nodos |

## Pruebas realizadas

- Franco y trenzas: Solicitud de Franco para trenzas.
- Dayana y alisado: Solicitud de Dayana para alisado.

Los resultados se comprobaron en la salida del último nodo.

## Alcance

El flujo procesa una solicitud de prueba.
No comprueba disponibilidad ni reserva un turno.
## Cómo revisar un problema

1. Comprobar que la URL coincida con la del Webhook.
2. Si uso Test URL, activar Listen for test event.
3. Revisar el Output del Webhook para confirmar la recepción.
4. Revisar los nodos siguientes en orden y leer cualquier error.
5. Comprobar la estructura de los datos antes de escribir expresiones.

En este flujo, Webhook entrega cliente dentro de body.
El primer Edit Fields lo coloca en la raíz del registro.
Por eso cambia de $json.body.cliente a $json.cliente.

Con Respond: Immediately, una respuesta HTTP 200 no confirma
que todos los nodos hayan terminado correctamente.
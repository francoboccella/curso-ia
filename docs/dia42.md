# Día 42: repaso y documentación del flujo de turnos

## Qué hace el flujo

1. Lee un correo de prueba en Gmail.
2. Extrae el cliente, el servicio, la fecha, la hora y la duración.
3. Consulta la disponibilidad en Google Calendar.
4. Si el horario está libre, crea el turno y actualiza el estado en Sheets.

## Qué comprobé el día 41

Probé el flujo por etapas. Primero registré la solicitud como `pendiente` en
Sheets. Después confirmé que el horario del 23/11/2026, de 15:00 a 16:00,
estaba libre y que el turno se creó en Calendar. Por último, verifiqué
que la misma fila pasó a `confirmado`, sin duplicarse.

`Update Row` usa `id_correo` para encontrar la fila y cambia la columna `estado`.

## Límite de la versión exportada

El nodo `Append Row` quedó desconectado para evitar duplicar la fila durante
la prueba. Con un correo nuevo, el flujo puede crear el turno en Calendar,
pero `Update Row` no encontrará una fila para ese `id_correo`.

## Mejora propuesta

Después de extraer los datos y antes de consultar Calendar, buscar el
`id_correo` en Sheets. Si no existe, registrar la solicitud como `pendiente`.
Si ya existe, revisar su estado antes de continuar y evitar insertar otra fila.
Marcar la solicitud como `confirmado` solo después de crear el evento.

Esta mejora quedó documentada y todavía no se implementó.

## Archivo de la práctica

[Workflow del día 41](dia41.json)
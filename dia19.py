import os
import requests
token = os.getenv("SALON_API_TOKEN")

if token:
    encabezados = {
        "Authorization": "Bearer " + token
    }
    print("Encabezado preparado")
    respuesta = requests.get(
        "https://postman-echo.com/get",
        headers=encabezados,
        timeout=10
    )
    print("Código recibido:", respuesta.status_code)
    datos = respuesta.json()
    recibido = datos["headers"].get("authorization")
    print("Encabezado recibido:", recibido == encabezados["Authorization"])
else:
    print("Falta configurar SALON_API_TOKEN en CMD")
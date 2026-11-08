import requests
parametros = {
    "fecha": "2026-11-02",
    "servicio": "trenzas"
}
try:
    respuesta = requests.get(
        "https://postman-echo.com/get",
        params=parametros,
        timeout=10
    )
    print(respuesta.status_code)
    print(respuesta.text)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        print(datos["url"])
        print(datos["args"]["servicio"])
        print(datos["args"]["fecha"])
    else:
        print("Código recibido:", respuesta.status_code)
except requests.exceptions.Timeout:
    print("Se agotó el tiempo de espera.")
except requests.exceptions.ConnectionError:
    print("No se pudo conectar con el servidor.")
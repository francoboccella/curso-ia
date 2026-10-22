import json

solicitud = {
    "cliente": {
        "nombre": "Dayana",
        "ciudad": "Rosario"},
    "correo": None,
    "urgente": True,
    "servicios": ["consulta general", "actualizar datos"],
    "cantidad": 3
}
texto_json = json.dumps(solicitud)
print(texto_json)
datos = json.loads(texto_json)
print(datos["cliente"]["ciudad"])
print(datos["urgente"])
print(datos["servicios"][1])
print(datos["cantidad"])
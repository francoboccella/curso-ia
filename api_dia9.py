import json
respuesta = {
    "estado": "ok",
    "solicitud":{
        "cliente": "Alan",
        "tipo": "consulta general"
    } 
}
with open("respuesta_api.json", "w", encoding="utf-8")as archivo:
    json.dump(respuesta, archivo, indent=4, 
ensure_ascii=False)
with open("respuesta_api.json", "r", encoding="utf-8")as archivo:
    datos= json.load(archivo)
print(datos["estado"])
print(datos["solicitud"]["cliente"])
print(datos["solicitud"]["tipo"])
import json
solicitud = {
    "cliente": "Franco",
    "tipo": "consulta general"
}
with open("solicitud.json", "w", encoding="utf-8")as archivo:
    json.dump(solicitud, archivo, indent=4, 
ensure_ascii=False)
with open("solicitud.json", "r", encoding= "utf-8")as archivo:
    datos = json.load(archivo)
print(datos["cliente"])

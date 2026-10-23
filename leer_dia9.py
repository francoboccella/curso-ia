import json
with open("solicitud.json", "r", encoding="utf-8")as archivo:
    datos = json.load(archivo)
print(datos["cliente"])
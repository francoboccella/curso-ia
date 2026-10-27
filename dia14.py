import json
solicitudes = [
    {"cliente": "Alan", "prioridad": "revisar" }
]
with open("repaso_dia14.json", "w", encoding="utf-8") as archivo:
    json.dump(solicitudes, archivo)
with open("repaso_dia14.json", "r", encoding="utf-8") as archivo:
        recuperadas = json.load(archivo)

print(recuperadas)
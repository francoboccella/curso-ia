import pandas as pd
import json
datos = pd.read_csv("solicitudes_sucias.csv")
print("DATOS ORIGINALES")
print(datos)
datos["cliente"] = datos["cliente"].str.strip().str.title()
datos["tipo"] = datos["tipo"].str.strip().str.lower()
datos["prioridad"] = datos["prioridad"].str.strip().str.lower()

print("DATOS NORMALIZADOS")
print(datos)
datos["prioridad"] = datos["prioridad"].fillna("revisar")
datos = datos.drop_duplicates()

print("SIN FALTANTES NI DUPLICADOS")
print(datos)
permitidas = ["alta", "media", "baja", "revisar"]

datos.loc[
    ~datos["prioridad"].isin(permitidas),
    "prioridad"
] = "revisar"

print("PRIORIDADES VALIDADAS")
print(datos)
acciones = {
    "alta": "atender primero",
    "media": "atender después",
    "baja": "atención habitual",
    "revisar": "revisión manual"
}

datos["accion"] = datos["prioridad"].map(acciones)

print("SOLICITUDES CLASIFICADAS")
print(datos)
solicitudes = datos.to_dict(orient="records")

print("LISTA DE SOLICITUDES")
print(solicitudes)
with open("solicitudes_procesadas.json", "w", encoding="utf-8") as archivo:
    json.dump(solicitudes, archivo, indent=4, ensure_ascii=False)

print("JSON GUARDADO")
with open("solicitudes_procesadas.json", "r", encoding="utf-8") as archivo:
    comprobacion = json.load(archivo)

print("SOLICITUDES RECUPERADAS:", len(comprobacion))
print(comprobacion[2]["cliente"])
print(comprobacion[2]["accion"])
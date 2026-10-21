def obtener_prioridad(tipo):
    if tipo == "pago vencido":
        return "alta"
    elif tipo == "actualizar datos":
        return "media"
    elif tipo == "consulta general":
        return "baja"
    else:
        return "revisar"
solicitud = {
    "cliente": "Dayana", 
     "tipo": "consulta general"
     }
prioridad = obtener_prioridad(solicitud["tipo"])
print(solicitud["cliente"] + ": " + prioridad)
bajas = 0
for prioridad in ["baja", "alta" "media", "baja"]:
    if prioridad == "baja":
        bajas= bajas + 1
print("total de bajas", bajas)
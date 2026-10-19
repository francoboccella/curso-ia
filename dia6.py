def obtener_prioridad(tipo):
    if tipo == "pago vencido":
        return "alta"
    elif tipo == "actualizar datos":
        return "media"
    elif tipo == "consulta general":
        return "baja"
    else:
        return "revisar"
solicitudes = [
    {"cliente": "Franco", "tipo": "pago vencido"},
    {"cliente": "Dayana", "tipo": "actualizar datos"},
    {"cliente": "Alan", "tipo": "consulta general"},
    {"cliente": "Lucia", "tipo": "otro"}
]
altas = 0
medias = 0
bajas = 0
revisar = 0
for solicitud in solicitudes:
    prioridad = obtener_prioridad(solicitud["tipo"])
    if prioridad == "alta":
        altas = altas + 1
    elif prioridad == "media":
        medias = medias + 1
    elif prioridad == "baja":
        bajas = bajas + 1
    else:
        propiedad = "revisar"
        revisar = revisar + 1
    print(solicitud["cliente"] + ": " + prioridad)
print("solicitudes de prioridad alta:", altas)
print("solicitudes de prioridad media:", medias)
print("solicitudes de prioridad baja:", bajas)
print("solicitudes de prioridad revisar:", revisar)
print("total de solicitudes:", len(solicitudes))
print("total contado:", altas + medias + bajas + revisar)
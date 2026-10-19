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
        {"cliente": "Dayana", "tipo": "consulta general"},
        {"cliente": "Alan", "tipo": "actualizar datos"},
        {"cliente": "Marcos", "tipo": "actualizar datos"},
        {"cliente": "Lucia", "tipo": "otro"}
    ]
for solicitud in solicitudes:
        prioridad = obtener_prioridad(solicitud["tipo"])
        print(solicitud["cliente"] + ": " + prioridad)
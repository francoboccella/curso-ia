solicitudes = [
    {"cliente": "Franco", "tipo": "pago vencido"},
    {"cliente": "Dayana", "tipo": "consulta general"},
    {"cliente": "Alan", "tipo": "actualizar datos"},
    {"cliente": "lucia", "tipo": "otro"}
    ]
for solicitud in solicitudes:
    if solicitud["tipo"] == "pago vencido":
        print(solicitud["cliente"] + ": prioridad alta")
    elif solicitud["tipo"] == "actualizar datos":
        print(solicitud["cliente"] + ": prioridad media")
    elif solicitud["tipo"] == "consulta general":
        print(solicitud["cliente"] + ": prioridad baja")
    else:
        print(solicitud["cliente"] + ": revisar solucion")
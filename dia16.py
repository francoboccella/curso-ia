codigo_estado = 400
if codigo_estado == 201:
    print("Recurso creado")
elif codigo_estado == 401:
    print("Faltan credenciales validas")
elif codigo_estado == 404:
    print("Recurso no encontrado")
elif codigo_estado == 500:
    print("Error interno del servidor")
elif codigo_estado == 204:
    print("Operacion completa sin cuerpo de respuesta")
elif codigo_estado == 400:
    print("Revisar los datos de la petición")
else:
    print("otro resultado")
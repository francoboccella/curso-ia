import json
respuesta_texto = '''
{
    "servicios": ["corte", "alisado", "trenzas"]
}
'''
datos = json.loads(respuesta_texto)
print(datos["servicios"][1])
peticion = {
    "endpoint": "https://api.salon.example/horarios",
    "fecha": "2026-10-30"
}

print("PETICIÓN SIMULADA")
print(peticion)
respuesta_horarios = '''
{
    "fecha": "2026-10-30",
    "horarios_disponibles": ["10:00", "15:00"]
}
'''

horarios = json.loads(respuesta_horarios)

print("RESPUESTA SIMULADA")
print(horarios ["horarios_disponibles"] [1])

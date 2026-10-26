nombre = " dayana "
nombre = nombre.strip().title()
print(nombre)
correo = "FRANCO@GMAIL.COM"
correo = correo.strip().lower()
print(correo)
import pandas as pd
datos = pd.DataFrame({
    "cliente": [" franco ", " DAYANA ", "Alan"],
    "prioridad": [" ALTA ", "Media ", "baja"],
    "correo": [" FRANCO@GMAIL.COM ", " DAYANA@GMAIL.COM ", "ALAN@GMAIL.COM"],
    "servicio": [" CONSULTA GENERAL ", " Actualizar Datos ", "CUNSULTA GENERAL"],
    "fecha": ["26/10/2026", "05/11/2026", "08/12/2026"]
})
datos["cliente"] = datos["cliente"].str.strip().str.title()
datos["prioridad"] = datos["prioridad"].str.strip().str.lower()
datos["correo"] = datos["correo"].str.strip().str.lower()
datos["servicio"] = datos["servicio"].str.strip().str.lower()
datos["fecha"] = pd.to_datetime(
    datos["fecha"], format="%d/%m/%Y"
).dt.strftime("%Y-%m-%d")
print(datos)
datos.to_csv("solicitudes_normalizadas.csv", index=False)
comprobacion = pd.read_csv("solicitudes_normalizadas.csv")
print("ARCHIVO GUARDADO")
print(comprobacion)
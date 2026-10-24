import pandas as pd 
datos = pd.read_csv("solicitudes_sucias.csv")
print(datos)
print("DATOS FALTANTES")
print(datos.isna())
sin_prioridad = datos[datos["prioridad"].isna()]
print("SOLICITUDES SIN PRIORIDAD")
print(sin_prioridad)
datos["prioridad"] = datos["prioridad"].fillna("revisar")
print("TABLA CON FALTANTES COMPLETADO")
print(datos)
print("FILAS REPETIDAS")
print(datos.duplicated())
sin_duplicados = datos.drop_duplicates()
print("TABLA SIN DUPLICADOS")
print(sin_duplicados)
permitidas = ["alta", "media", "baja", "revisar"]
print("PRIORIDAD PERMITIDA")
print(sin_duplicados["prioridad"].isin(permitidas))
invalidas = sin_duplicados[
    ~sin_duplicados["prioridad"].isin(permitidas)]
print("SOLICITUDES CON PRIORIDAD INVALIDA")
print(invalidas)
limpios = sin_duplicados.copy()

limpios.loc[
    ~limpios["prioridad"].isin(permitidas),
    "prioridad"
] = "revisar"

print("DATOS LIMPIOS")
print(limpios)
limpios.to_csv("solicitudes_limpias.csv", index=False)
comprobacion = pd.read_csv("solicitudes_limpias.csv")

print("ARCHIVO GUARDADO")
print(comprobacion)
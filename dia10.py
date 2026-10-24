import pandas as pd 
datos = pd.read_csv("solicitudes.csv")
bajas = datos[datos["prioridad"] == "baja"]
print(bajas)
bajas.to_csv("solicitudes_bajas.csv",index=False)

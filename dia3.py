tipo = input("pago vencido, actualizar datos o consulta general")
if tipo == "pago vencido":
    print("prioridad alta")
elif tipo == "actualizar datos":
    print("prioridad media")
elif tipo == "consulta general":
    print("prioridad baja")
else:
    print("Tipo de consulta no reconocido")
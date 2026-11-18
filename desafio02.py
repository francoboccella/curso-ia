cliente = input("¿nombre y apellido?")
solicitud = input("¿que tipo de solicitud?").lower().strip()
palabras = solicitud.split()
solicitud = " ".join(palabras)
print("cliente:", cliente)
print("solicitud:", solicitud)
if solicitud == ("pago vencido"):
    print("prioridad:", "alta")
elif solicitud == ("actualizar datos"):
    print("prioridad:", "media")
elif solicitud == ("consulta general"):
    print("prioridad:", "baja")
else:
    print("prioridad:", "otro")






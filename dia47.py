import sqlite3

conexion = sqlite3.connect(":memory:")

conexion.execute("""
    CREATE TABLE clientes (
        id_cliente INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL
    );
""")
conexion.execute("PRAGMA foreign_keys = ON;")
conexion.execute("""
    CREATE TABLE solicitudes (
        id_solicitud INTEGER PRIMARY KEY,
        id_cliente INTEGER NOT NULL,
        servicio TEXT NOT NULL,
        importe INTEGER NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
    );
""")
conexion.execute("INSERT INTO clientes VALUES (1, 'Dayana');")
conexion.execute("INSERT INTO clientes VALUES (2, 'Franco');")
conexion.execute("INSERT INTO clientes VALUES (3, 'Luca');")
conexion.execute("INSERT INTO clientes VALUES (4, 'Ana');")

conexion.execute("INSERT INTO solicitudes VALUES (101, 1, 'trenzas', 18000);")
conexion.execute("INSERT INTO solicitudes VALUES (102, 2, 'alisado', 25000);")
conexion.execute("INSERT INTO solicitudes VALUES (103, 1, 'baño de crema', 12000);")
conexion.execute("INSERT INTO solicitudes VALUES (104, 3, 'alisado', 25000);")

print(conexion.execute("SELECT * FROM clientes;").fetchall())
print(conexion.execute("SELECT * FROM solicitudes;").fetchall())

print(conexion.execute("""

SELECT clientes.nombre, COUNT(solicitudes.id_solicitud), 
SUM(solicitudes.importe)
FROM clientes
LEFT JOIN solicitudes
ON clientes.id_cliente = solicitudes.id_cliente
GROUP BY clientes.id_cliente
ORDER BY SUM(solicitudes.importe) DESC;

""").fetchall())
conexion.close()
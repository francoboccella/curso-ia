import sqlite3
from pathlib import Path

conexion = sqlite3.connect(":memory:")

conexion.executescript(Path("docs/dia45.sql").read_text(encoding="utf-8"))

print(conexion.execute("SELECT * FROM solicitudes;").fetchall())

conexion.execute("INSERT INTO solicitudes VALUES ('Maria', 'trenzas', 18000);")
conexion.execute("INSERT INTO solicitudes VALUES ('Lucia', 'alisado', 25000);")
conexion.execute("INSERT INTO solicitudes VALUES ('Ana', 'trenzas', 18000);")

print(conexion.execute("""SELECT servicio, COUNT(*), SUM(importe), AVG(importe) FROM solicitudes GROUP BY servicio ORDER BY SUM(importe) DESC""").fetchall())
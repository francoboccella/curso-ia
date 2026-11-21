-- Datos de prueba
CREATE TABLE solicitudes (
    cliente TEXT,
    servicio TEXT,
    estado TEXT
);

INSERT INTO solicitudes (cliente, servicio, estado)
VALUES ('Dayana', 'trenzas', 'pendiente');

-- Consultas practicadas
SELECT cliente, servicio, estado FROM solicitudes;
SELECT servicio, cliente FROM solicitudes;
SELECT * FROM solicitudes;
SELECT estado, cliente FROM solicitudes;
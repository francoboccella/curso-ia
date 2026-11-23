-- Día 45: ordenar, limitar y resumir solicitudes.
-- Ejecutar en una base nueva.

CREATE TABLE solicitudes (
    cliente TEXT,
    servicio TEXT,
    importe INTEGER
);

INSERT INTO solicitudes (cliente, servicio, importe)
VALUES
    ('Dayana', 'trenzas', 18000),
    ('Franco', 'alisado', 25000),
    ('Luca', 'baño de crema', 12000);

SELECT cliente, importe FROM solicitudes ORDER BY importe DESC;
SELECT cliente, importe FROM solicitudes ORDER BY importe DESC LIMIT 2;

SELECT COUNT(*) FROM solicitudes;
SELECT SUM(importe) FROM solicitudes;
SELECT AVG(importe) FROM solicitudes;

SELECT COUNT(*) FROM solicitudes WHERE importe > 15000;
SELECT AVG(importe) FROM solicitudes WHERE importe > 15000;
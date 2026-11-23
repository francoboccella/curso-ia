-- Día 44: filtrar solicitudes con WHERE.
-- Primero ejecutar dia43.sql en una base nueva.

INSERT INTO solicitudes (cliente, servicio, estado)
VALUES ('Franco', 'alisado', 'confirmada');

SELECT cliente, servicio, estado
FROM solicitudes
WHERE estado = 'pendiente';

SELECT cliente, servicio
FROM solicitudes
WHERE estado = 'confirmada';

SELECT cliente
FROM solicitudes
WHERE servicio = 'trenzas';
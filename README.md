# curso de ia y automatizacion 

## dia 1
prepare el entorno y cree mi primer programa en python
registre dos verciones con git y las subi a github
## como ejecutar el programa 
desde CMD, dentro de la carpeta curso-ia:
python hola.py
## Procesamiento de solicitudes: día 13

El programa `dia13.py`:
- Lee solicitudes desde un CSV.
- Normaliza espacios y mayúsculas.
- Completa prioridades faltantes con `revisar`.
- Elimina filas duplicadas.
- Cambia prioridades no permitidas por `revisar`.
- Asigna una acción según la prioridad.
- Guarda las solicitudes procesadas en JSON.

### Requisitos

Python y pandas instalados.

El archivo `solicitudes_sucias.csv` debe estar en la carpeta
desde la que se ejecuta el programa, con estas columnas:
`cliente`, `tipo` y `prioridad`.

### Cómo ejecutarlo

Desde CMD, dentro de `curso-ia`:

```bat
python dia13.py
```

### Resultado

Se genera `solicitudes_procesadas.json`.
Contiene una lista de solicitudes con los campos:
`cliente`, `tipo`, `prioridad` y `accion`.

El programa vuelve a leer el JSON para comprobar su contenido.
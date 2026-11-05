# Curso de IA y automatización

Repositorio de mis prácticas de formación en Python, procesamiento de datos, APIs y automatización.

## Herramientas utilizadas

- Python.
- pandas.
- requests.
- Flask.
- Git y GitHub.
- Postman y Make para las pruebas de integración.

## Primer programa: día 1

Preparé el entorno y creé mi primer programa en Python.
Registré versiones con Git y las subí a GitHub.

### Cómo ejecutarlo

Desde CMD, dentro de la carpeta `curso-ia`:

```bat
python hola.py
```

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

Para instalar pandas:

```bat
python -m pip install pandas
```

El archivo `solicitudes_sucias.csv` debe estar en la carpeta
desde la que se ejecuta el programa, con estas columnas:

- `cliente`.
- `tipo`.
- `prioridad`.

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

## Consultar una API desde Python: día 18

El programa `dia18.py` envía una petición GET a Postman Echo
con los parámetros `fecha` y `servicio` en la URL.

Postman Echo devuelve los datos recibidos para comprobar el envío.

### Requisitos

Python y la biblioteca requests instalados.

Para instalar requests, ejecutar en CMD:

```bat
python -m pip install requests
```

### Cómo ejecutarlo

Desde CMD, dentro de la carpeta `curso-ia`:

```bat
python dia18.py
```

### Resultado esperado

El programa muestra el código de estado y el contenido de la respuesta.

Si recibe el código 200, también muestra:

- La URL con los parámetros enviados.
- El servicio: `trenzas`.
- La fecha: `2026-11-02`.

Si recibe otro código, muestra `Código recibido:` y su valor.

La petición tiene un tiempo de espera configurado de 10 segundos.

## Integración con una API: día 21

El programa `dia21.py` utiliza Flask para recibir solicitudes
mediante un POST a la ruta `/validar`.

Comprueba que estén presentes las claves `id`, `cliente` y `servicio`.

- Si están las tres claves, responde con estado 200 y `{"ok": true}`.
- Si falta una clave, responde con estado 400 y un mensaje de error.

### Requisitos

Python y Flask instalados.

Para instalar Flask:

```bat
python -m pip install Flask
```

### Cómo iniciar la API

Desde CMD, dentro de `curso-ia`:

```bat
python dia21.py
```

Dejar esa ventana abierta mientras se realizan las pruebas.

En Postman, enviar un POST a:

```text
http://127.0.0.1:5000/validar
```

En Body, seleccionar raw y JSON. Ejemplo de solicitud:

```json
{
  "id": "SOL-004",
  "cliente": "Alan",
  "servicio": "trenzas"
}
```

La integración con Make se probó mediante un túnel temporal.
Para repetirla, es necesario iniciar el túnel y configurar
su dirección vigente en el módulo HTTP de Make.

## Documentación

Los apuntes se organizan en la carpeta `docs`.

- [Día 22: Git fundamental](docs/dia22.md)

## Estado del repositorio

Proyecto de aprendizaje en desarrollo, con datos ficticios
y ejemplos de práctica.

No incluir tokens, credenciales ni URLs operativas de webhooks
en los archivos publicados.
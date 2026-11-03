from flask import Flask, request, jsonify
app = Flask(__name__)
def validar_solicitud(solicitud):
    if "id" not in solicitud:
        return {"ok": False, "error": "Falta el campo id"}
    if "cliente" not in solicitud:
        return {"ok": False, "error": "Falta el campo cliente"}
    if "servicio" not in solicitud:
        return {"ok": False, "error": "Falta el campo servicio"}
    return {"ok": True}
@app.post("/validar")
def recibir_solicitud():
    solicitud = request.get_json(silent=True)
    if not isinstance(solicitud, dict):
        return jsonify({"ok": False, "error": "Enviá un objeto JSON"}), 400
    resultado = validar_solicitud(solicitud)
    if resultado["ok"]:
        return jsonify(resultado), 200
    return jsonify(resultado), 400
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
from flask import jsonify

def v1_index():
    return jsonify({
        "ok": True,
        "data": {
            "message": "healthy",
            "service_name": "gargantuan::api",
            "service_version": "0.0.1",
        }
    })
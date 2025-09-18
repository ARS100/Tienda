from flask import Blueprint, jsonify
from db import get_connection # type: ignore

distribuidores_bp = Blueprint("distribuidores", __name__)

@distribuidores_bp.route("/", methods=["GET"])
def listar_distribuidores():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Distribuidores")
        distribuidores = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(distribuidores)
    except Exception as e:
        return jsonify({"error": str(e)})

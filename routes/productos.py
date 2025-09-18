from flask import Blueprint, jsonify
from db import get_connection # type: ignore

productos_bp = Blueprint("productos", __name__)

@productos_bp.route("/", methods=["GET"])
def listar_productos():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Productos")
        productos = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(productos)
    except Exception as e:
        return jsonify({"error": str(e)})

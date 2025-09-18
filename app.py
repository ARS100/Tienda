from flask import Flask
from routes.distribuidores import distribuidores_bp # type: ignore
from routes.productos import productos_bp # type: ignore

app = Flask(__name__)

app.register_blueprint(distribuidores_bp, url_prefix="/distribuidores")
app.register_blueprint(productos_bp, url_prefix="/productos")

@app.route("/")
def home():
    return "🚀 Backend de Tienda Web corriendo..."

if __name__ == "__main__":
    app.run(debug=True)

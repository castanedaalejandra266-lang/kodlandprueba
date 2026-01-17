from flask import Flask, redirect, url_for
from routes.auth import auth_bp
from routes.main import main_bp
from routes.rewards import rewards_bp

app = Flask(__name__)
app.secret_key = "clave_super_secreta"

# Registro de rutas
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)
app.register_blueprint(rewards_bp)

@app.route("/")
def home():
    return redirect(url_for("main.dashboard"))

if __name__ == "__main__":
    app.run(debug=True)

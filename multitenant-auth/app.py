# app.py
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from flask_cors import CORS
from routes.auth_routes import bp as auth_bp

load_dotenv()
DEV_MODE = True

app = Flask(__name__, template_folder="templates", static_folder="static")

# ✅ This allows Flask to parse subdomains on localhost
app.config["SERVER_NAME"] = "localhost:5000"

CORS(app, origins=["*"], supports_credentials=True)
app.register_blueprint(auth_bp)

# ------------------------
# ROUTES
# ------------------------

@app.route("/", subdomain="<tenant>")
@app.route("/", defaults={"tenant": None})
def index(tenant):
    # 👇 Fallback: if Flask can't extract subdomain, parse manually
    if DEV_MODE and not tenant:
        tenant = request.host.split('.')[0]
    print(f"[DEBUG] Tenant: {tenant}")
    return render_template("login.html") if tenant else ("Please access using subdomain like client1.localhost", 400)

@app.route("/dashboard", subdomain="<tenant>")
@app.route("/dashboard", defaults={"tenant": None})
def dashboard_page(tenant):
    if DEV_MODE and not tenant:
        tenant = request.host.split('.')[0]
    return render_template("dashboard.html")

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")

# ------------------------
# APP START
# ------------------------

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    print(f"[INFO] Running app on http://client1.localhost:{port} and http://client2.localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)

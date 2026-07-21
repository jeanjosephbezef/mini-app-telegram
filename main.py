from flask import Flask, send_from_directory
import os

app = Flask(__name__)

DOSSIER_WEBAPP = os.path.join(os.path.dirname(__file__), "webapp")

@app.route("/")
def accueil():
    return send_from_directory(DOSSIER_WEBAPP, "index.html")

@app.route("/<path:fichier>")
def fichiers(fichier):
    return send_from_directory(DOSSIER_WEBAPP, fichier)

if __name__ == "__main__":
    app.run(debug=True)
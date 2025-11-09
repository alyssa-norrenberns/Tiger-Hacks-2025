from flask import Flask
from routes.planet import planet_bp
from flask_cors import CORS
import os


app = Flask(__name__)
# Enable CORS for demo so the Live Server front-end (different origin) can call the API
CORS(app)

# Register blueprints
app.register_blueprint(planet_bp, url_prefix="/planet")

if __name__ == "__main__":
    app.run(debug=True, port=5050)
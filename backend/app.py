# Small, non-invasive additions to help debug 404s when starting the server
from flask import Flask, jsonify
from routes.planet import planet_bp
from flask_cors import CORS
import os


app = Flask(__name__)
# Enable CORS for demo so the Live Server front-end (different origin) can call the API
CORS(app)

# Register blueprints
app.register_blueprint(planet_bp, url_prefix="/planet")

# Diagnostic root route so visiting http://localhost:5050/ returns a helpful message
@app.route("/", methods=["GET"])
def root_index():
    return jsonify({
        "status": "running",
        "message": "API is running. Use /planet/calendar?planet=earth or POST /planet/calendar {\"planet\": \"earth\"}",
    })

# Print registered routes at startup to help debug Not Found errors
def _print_routes():
    print("Registered routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule}")


if __name__ == "__main__":
    app.run(debug=True, port=5050)
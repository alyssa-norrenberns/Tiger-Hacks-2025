from routes.test import planet_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(planet_bp, url_prefix="/planet")

if __name__ == "__main__":
    app.run(debug=True)
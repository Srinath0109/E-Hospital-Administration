from flask import Flask
from routes import hospital_routes
from database import init_db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hospital.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database
init_db(app)

# Register API routes
app.register_blueprint(hospital_routes, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)

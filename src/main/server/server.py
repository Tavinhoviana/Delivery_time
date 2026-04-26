from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connection_handler

# importar blueprints
from src.main.routes.hubs_routes import hubs_routes_bp
from src.main.routes.orders_routes import orders_routes_bp
from src.main.routes.riders_routes import riders_routes_bp

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(hubs_routes_bp)
app.register_blueprint(orders_routes_bp)
app.register_blueprint(riders_routes_bp)

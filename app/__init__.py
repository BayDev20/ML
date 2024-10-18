from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    """
    Create and configure an instance of the Flask application.
    
    :return: Configured Flask app instance
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the database with the app
    db.init_app(app)

    with app.app_context():
        from app import models  # Import models here
        db.create_all()  # This line creates the tables

        # Import data
        from app.import_data import import_data, get_db_stats
        import_data()
        print(get_db_stats())

    # Register the main blueprint
    from app import routes
    app.register_blueprint(routes.main)

    return app





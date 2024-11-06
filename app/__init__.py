from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='../templates')

    # Import and register the routes
    from .routes import home_bp
    app.register_blueprint(home_bp)

    return app

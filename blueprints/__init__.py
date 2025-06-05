from flask import Flask
from .views import views_bp

def create_app():
    app = Flask(__name__, static_folder='../static', template_folder='../templates')  # Initialize flask app with static and template directories
    
    # Register Blueprints
    app.register_blueprint(views_bp)

    return app
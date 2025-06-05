from flask import Blueprint, render_template

views_bp = Blueprint('views', __name__) #initialize blueprint

# Responsible for routing and connecting backend and frontend.
@views_bp.route('/') 
def home():
    return render_template('home.html')
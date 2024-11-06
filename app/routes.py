from flask import Blueprint, render_template
from app.db import query_db  # Import the query_db function from db.py

# Define the Blueprint for home routes
home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return render_template('home.html')


@home_bp.route('/database')
def database():
    # Query all entries from the 'reactions' table
    data = query_db('SELECT * FROM metat')

    # Pass the queried data to the 'database.html' template
    return render_template('database.html', data=data)

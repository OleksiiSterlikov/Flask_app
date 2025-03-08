"""Modul main routes"""

from flask import render_template
from app import app



@app.route('/')
def main():
    """Main function"""

    return render_template('index.html')

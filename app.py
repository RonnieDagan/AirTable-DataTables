from flask import Flask, render_template, jsonify
from format import format_data
from main import create_table
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Load the JSON data
    create_table()
    data = format_data('output.json')
    
    # Render the table
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

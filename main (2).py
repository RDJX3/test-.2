from flask import Flask, render_template, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/files')
def list_files():
    files = os.listdir('static/sheets')
    text_files = [f for f in files if f.endswith('.txt')]
    return jsonify(text_files)

@app.route('/sheets/<filename>')
def get_file(filename):
    return send_from_directory('static/sheets', filename)

if __name__ == '__main__':
    app.run(debug=True)

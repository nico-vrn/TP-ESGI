import os
from flask import Flask, render_template, request, jsonify
import sqlite3
import threading

app = Flask(__name__)
DATABASE = os.path.join(os.path.dirname(__file__), 'siem_logs.db')

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp TEXT,
                        source TEXT,
                        message TEXT
                      )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logs', methods=['GET'])
def get_logs():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs ORDER BY timestamp DESC")
    logs = cursor.fetchall()
    conn.close()
    return jsonify(logs)

@app.route('/log', methods=['POST'])
def log():
    data = request.get_json()
    timestamp = data.get('timestamp')
    source = data.get('source')
    message = data.get('message')
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (timestamp, source, message) VALUES (?, ?, ?)",
                   (timestamp, source, message))
    conn.commit()
    conn.close()
    
    return jsonify({"status": "success"}), 200

@app.route('/analyse_forensique', methods=['POST'])
def analyse_forensique():
    from scripts.analyse_forensique import analyser_journaux
    log_file_path = request.form['log_file_path']
    analyser_journaux(log_file_path)
    return jsonify({"status": "Forensic analysis completed"}), 200

@app.route('/gestion_fichiers', methods=['POST'])
def gestion_fichiers():
    from scripts.gestion_fichiers import lister_fichiers
    directory_path = request.form['directory_path']
    lister_fichiers(directory_path)
    return jsonify({"status": "File management completed"}), 200

def run_scripts():
    from scripts.detection_connexions import detecter_connexions_suspectes
    from scripts.surveillance_reseau import main as surveiller_reseau

    detection_thread = threading.Thread(target=detecter_connexions_suspectes)
    surveillance_thread = threading.Thread(target=surveiller_reseau)

    detection_thread.start()
    surveillance_thread.start()

if __name__ == '__main__':
    init_db()  # Initialiser la base de données avant de démarrer les scripts
    run_scripts()  # Démarrer les scripts de surveillance après l'initialisation de la DB
    app.run(debug=True)

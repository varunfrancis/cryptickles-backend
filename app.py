from flask import Flask, jsonify
from flask_cors import CORS
import _sqlite3

app = Flask(__name__)
CORS(app)

def get_clue():
    conn = _sqlite3.connect('clues.db')
    cursor = conn.cursor()
    cursor.execute("SELECT date, clue, answer, hint FROM clues")
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            'date': row[0],
            'clue': row[1],
            'answer': row[2],
            'hint': row[3]
        }
        for row in rows
    ]

@app.route("/clues", methods=["GET"])
def fetch_clues():
    return jsonify(get_clue())

if __name__ == "__main__":
    app.run(debug=True)
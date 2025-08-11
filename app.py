from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
from datetime import date

app = Flask(__name__)
CORS(app)

def init_db():
    """Initialize database and add setter_name column if it doesn't exist"""
    conn = sqlite3.connect('clues.db')
    cursor = conn.cursor()
    
    # Check if setter_name column exists
    cursor.execute("PRAGMA table_info(clues)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'setter_name' not in columns:
        cursor.execute("ALTER TABLE clues ADD COLUMN setter_name TEXT")
        print("Added setter_name column to clues table")
    
    conn.commit()
    conn.close()

def get_clue_by_date(requested_date):
    conn = sqlite3.connect('clues.db')
    cursor = conn.cursor()
    cursor.execute("SELECT date, clue, answer, hint, answer_length, setter_name FROM clues WHERE date = ?", (requested_date,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "date": row[0], 
            "clue": row[1], 
            "answer": row[2], 
            "hint": row[3], 
            "answer_length": row[4],
            "setter_name": row[5]
        }
    return None

@app.route("/clue", methods=["GET"])
def fetch_clue():
    requested_date = request.args.get("date", date.today().strftime("%Y-%m-%d"))
    clue = get_clue_by_date(requested_date)
    if clue:
        return jsonify(clue)
    else:
        return jsonify({"error": "Clue missing for this date"}), 404

if __name__ == "__main__":
    init_db()  # Initialize database and add setter_name column if needed
    app.run(debug=True, port=8000)
from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
from datetime import date

app = Flask(__name__)
CORS(app)

def get_clue_by_date(requested_date):
    conn = sqlite3.connect('clues.db')
    cursor = conn.cursor()
    cursor.execute("SELECT date, clue, answer, hint FROM clues WHERE date = ?", (requested_date,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"date": row[0], "clue": row[1], "answer": row[2], "hint": row[3]}
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
    app.run(debug=True)
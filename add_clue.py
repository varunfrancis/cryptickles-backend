#!/usr/bin/env python3
import sqlite3
import sys
from datetime import datetime

def add_clue(date, clue, answer, hint=None):
    """Add a new clue to the database with automatic answer length calculation"""
    conn = sqlite3.connect('clues.db')
    cursor = conn.cursor()
    
    # Calculate answer length
    answer_length = len(answer)
    
    try:
        cursor.execute(
            "INSERT INTO clues (date, clue, answer, hint, answer_length) VALUES (?, ?, ?, ?, ?)",
            (date, clue, answer, hint, answer_length)
        )
        conn.commit()
        print(f"✅ Clue added successfully!")
        print(f"   Date: {date}")
        print(f"   Answer: {answer}")
        print(f"   Answer Length: {answer_length}")
    except sqlite3.IntegrityError:
        print(f"❌ Error: A clue already exists for date {date}")
    except Exception as e:
        print(f"❌ Error adding clue: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python add_clue.py <date> <clue> <answer> [hint]")
        print("Example: python add_clue.py 2025-01-15 'What is 2+2?' '4' 'Basic math'")
        sys.exit(1)
    
    date = sys.argv[1]
    clue = sys.argv[2]
    answer = sys.argv[3]
    hint = sys.argv[4] if len(sys.argv) > 4 else None
    
    add_clue(date, clue, answer, hint) 
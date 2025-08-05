#!/usr/bin/env python3
import sqlite3

def update_answer_lengths():
    """Update answer_length for all clues that don't have it set"""
    conn = sqlite3.connect('clues.db')
    cursor = conn.cursor()
    
    try:
        # Update all clues where answer_length is NULL
        cursor.execute("""
            UPDATE clues 
            SET answer_length = LENGTH(answer) 
            WHERE answer_length IS NULL
        """)
        
        updated_count = cursor.rowcount
        conn.commit()
        
        print(f"✅ Updated {updated_count} clues with answer lengths")
        
        # Show a few examples
        cursor.execute("SELECT date, answer, answer_length FROM clues ORDER BY date DESC LIMIT 5")
        rows = cursor.fetchall()
        
        print("\nRecent clues with answer lengths:")
        for row in rows:
            print(f"  {row[0]}: '{row[1]}' (length: {row[2]})")
            
    except Exception as e:
        print(f"❌ Error updating answer lengths: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    update_answer_lengths() 
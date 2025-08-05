#!/usr/bin/env python3
import sqlite3
import requests
import json

def test_database():
    """Test the database changes"""
    print("🔍 Testing database changes...")
    
    conn = sqlite3.connect('clues.db')
    cursor = conn.cursor()
    
    # Test that answer_length field exists and has data
    cursor.execute("SELECT date, answer, answer_length FROM clues LIMIT 3")
    rows = cursor.fetchall()
    
    print("✅ Database schema updated successfully!")
    print("Sample data with answer_length:")
    for row in rows:
        print(f"  {row[0]}: '{row[1]}' (length: {row[2]})")
    
    conn.close()

def test_api_local():
    """Test the local API"""
    print("\n🔍 Testing local API...")
    
    try:
        # Start the server in background (if not already running)
        import subprocess
        import time
        
        # Try to make a request to the API
        response = requests.get("http://127.0.0.1:8000/clue?date=2025-07-31", timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Local API is working!")
            print(f"Response includes answer_length: {'answer_length' in data}")
            if 'answer_length' in data:
                print(f"Answer length for 'paris': {data['answer_length']}")
            print(f"Full response: {json.dumps(data, indent=2)}")
        else:
            print(f"❌ API returned status code: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to local API. Make sure to run: python app.py")
    except Exception as e:
        print(f"❌ Error testing API: {e}")

def test_helper_script():
    """Test the helper script"""
    print("\n🔍 Testing helper script...")
    
    try:
        import subprocess
        result = subprocess.run([
            'python', 'add_clue.py', 
            '2025-01-30', 
            'Test question?', 
            'test', 
            'Test hint'
        ], capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            print("✅ Helper script works!")
            print(result.stdout)
        else:
            print("❌ Helper script failed:")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ Error testing helper script: {e}")

if __name__ == "__main__":
    print("🧪 Testing local changes for answer_length field...\n")
    
    test_database()
    test_api_local()
    test_helper_script()
    
    print("\n🎉 Testing complete!")
    print("\nTo test the API manually:")
    print("1. Start the server: python app.py")
    print("2. In another terminal: curl 'http://127.0.0.1:8000/clue?date=2025-07-31'") 
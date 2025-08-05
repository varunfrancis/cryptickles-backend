#!/usr/bin/env python3
import requests
import json

def test_api():
    """Test the local API and verify answer_length field"""
    print("🔍 Testing local API for answer_length field...")
    
    try:
        # Test the API
        response = requests.get("http://127.0.0.1:8000/clue?date=2025-07-31", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print("✅ API is working!")
            print(f"Response includes answer_length: {'answer_length' in data}")
            
            if 'answer_length' in data:
                print(f"✅ answer_length field is present: {data['answer_length']}")
                print(f"Answer: '{data['answer']}' (length: {data['answer_length']})")
            else:
                print("❌ answer_length field is missing")
            
            print("\nFull API response:")
            print(json.dumps(data, indent=2))
            
        else:
            print(f"❌ API returned status code: {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to local API.")
        print("Make sure to run: python app.py")
    except Exception as e:
        print(f"❌ Error testing API: {e}")

if __name__ == "__main__":
    test_api() 
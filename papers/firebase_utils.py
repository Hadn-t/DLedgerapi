import os
import json
import firebase_admin
from firebase_admin import credentials, auth

# Load Firebase credentials from environment variable
firebase_credentials = os.getenv("FIREBASE_CREDENTIALS")

if firebase_credentials:
    cred = credentials.Certificate(json.loads(firebase_credentials))
    firebase_admin.initialize_app(cred)
else:
    raise ValueError("Firebase credentials not found. Make sure to set the environment variable.")

def fetch_firebase_users():
    """Fetch users from Firebase Authentication"""
    users = []
    try:
        # Fetch all users from Firebase Auth
        page = auth.list_users()
        while page:
            for user in page.users:
                users.append({'uid': user.uid, 'email': user.email})
            page = page.get_next_page()
    except Exception as e:
        print(f"Error fetching Firebase users: {str(e)}")
    return users

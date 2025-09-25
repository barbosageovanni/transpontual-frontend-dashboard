#!/usr/bin/env python3
"""
Debug script para identificar problemas no Railway
"""
import os
import sys
import traceback

print("=== RAILWAY DEBUG STARTUP ===")
print(f"Python version: {sys.version}")
print(f"Current working directory: {os.getcwd()}")
print(f"Python path: {sys.path}")
print(f"Environment variables:")
for key, value in sorted(os.environ.items()):
    if 'SECRET' not in key and 'PASSWORD' not in key:
        print(f"  {key}={value}")

print("\n=== TESTING IMPORTS ===")
try:
    print("Testing app.dashboard import...")
    from app.dashboard import create_app
    print("✅ app.dashboard imported successfully")

    print("Testing create_app()...")
    app = create_app()
    print(f"✅ Flask app created: {app}")

    print("Testing wsgi import...")
    from wsgi import application
    print(f"✅ WSGI application: {application}")

    print("\n=== STARTING GUNICORN ===")
    # This would be the actual gunicorn command
    port = os.getenv('PORT', '8000')
    print(f"Would start gunicorn on port {port}")

except Exception as e:
    print(f"❌ ERROR: {e}")
    print("Full traceback:")
    traceback.print_exc()
    sys.exit(1)

print("✅ All tests passed - ready for production!")
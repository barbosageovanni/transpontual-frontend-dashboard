"""
WSGI entry point for production deployment
"""
import os
import sys

# Add current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

try:
    from run import app

    # Ensure app is configured for production
    if os.getenv('FLASK_ENV') == 'production':
        app.config['DEBUG'] = False
        app.config['TESTING'] = False

    # Export for Gunicorn
    application = app

except Exception as e:
    print(f"Error importing Flask app: {e}")
    import traceback
    traceback.print_exc()
    raise

if __name__ == "__main__":
    # For testing
    application.run(host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
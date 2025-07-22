#!/usr/bin/env python3
import os
import sys

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    
    # Try gunicorn first
    try:
        import gunicorn.app.wsgiapp
        sys.argv = [
            'gunicorn',
            '--bind', f'0.0.0.0:{port}',
            '--workers', '2',
            '--timeout', '60',
            'MAIN_APP:app'
        ]
        gunicorn.app.wsgiapp.run()
    except ImportError:
        # Fallback to Flask dev server
        from MAIN_APP import app
        app.run(host='0.0.0.0', port=port, debug=False)

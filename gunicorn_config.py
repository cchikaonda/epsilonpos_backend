# gunicorn_config.py

import multiprocessing

bind = "127.0.0.1:8000"  # Bind to the specified address and port

# Number of worker processes (adjust based on your server's resources)
workers = multiprocessing.cpu_count() * 2 + 1

# Daemonize the Gunicorn process (run in the background)
daemon = True

# Specify the path to the Django WSGI application
# Replace 'your_project' and 'wsgi' with your actual project and WSGI module names

# Assuming your project is named 'epsilonpos_backend'
pythonpath = '/var/www/epsilonposv2/epsilonpos_backend'
wsgi_app = 'config.wsgi.application'

import os

# Bind to 0.0.0.0 and use PORT environment variable
bind = f"0.0.0.0:{os.environ.get('PORT', 10000)}"

# Worker configuration
workers = 1
worker_class = "uvicorn.workers.UvicornWorker"

# Logging
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Preload app for better performance
preload_app = True

print(f"Gunicorn configured to bind to: {bind}")
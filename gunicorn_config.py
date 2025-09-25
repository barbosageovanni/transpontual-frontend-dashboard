"""
Configuração do Gunicorn para produção no Railway
"""
import os

# Configurações do servidor
bind = f"0.0.0.0:{os.getenv('PORT', '8000')}"
workers = int(os.getenv("GUNICORN_WORKERS", "2"))
worker_class = "sync"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 100

# Timeouts (mais generosos para Railway)
timeout = 120
keepalive = 5

# Logging (verbose para debug)
accesslog = "-"
errorlog = "-"
loglevel = "debug"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
capture_output = True

# Processo
preload_app = True
daemon = False
pidfile = None
user = None
group = None
tmp_upload_dir = None

# Performance
worker_tmp_dir = "/dev/shm" if os.path.exists("/dev/shm") else "/tmp"
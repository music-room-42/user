import multiprocessing
from os import getenv


bind = getenv('GUNICORN_BIND', '0.0.0.0:8082')
forwarded_allow_ips = '*'
limit_request_line = 8190
reload = True
accesslog = '-'
errorlog = '-'
loglevel = 'info'
timeout = 600
workers = multiprocessing.cpu_count() * 2 + 1

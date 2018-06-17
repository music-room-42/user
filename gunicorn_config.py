import multiprocessing
from gunicorn.http import wsgi


bind = '0.0.0.0:8082'
forwarded_allow_ips = '*'
limit_request_line = 8190
reload = True
accesslog = '-'
errorlog = '-'
loglevel = 'info'
timeout = 600
workers = multiprocessing.cpu_count() * 2 + 1

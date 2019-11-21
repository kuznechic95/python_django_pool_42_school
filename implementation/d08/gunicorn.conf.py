bind = "127.0.0.1:9000"                   # Don't use port 80 becaue nginx occupied it already.
errorlog = '/Users/okuzniet/logs/gunicorn-error.log'  # Make sure you have the log folder create
accesslog = '/Users/okuzniet/logs/gunicorn-access.log'
loglevel = 'debug'
workers = 1
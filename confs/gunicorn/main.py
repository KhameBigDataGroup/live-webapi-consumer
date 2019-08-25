from os.path import abspath, dirname, realpath


pythonpath = abspath(dirname(dirname(dirname(realpath(__file__)))))
django_settings = 'liveapi.settings'
bind = '0.0.0.0:8000'

workers = 2
timeout = 30

max_requests = 1500
max_requests_jitter = int(max_requests * 0.1)

preload = True
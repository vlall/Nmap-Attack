import socket
import json

class Nmapper:
    def __init__(self, site):
        self.url = 'shodanhq.com/%s' % (site)


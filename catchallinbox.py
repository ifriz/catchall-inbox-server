###
# catch all inbox
###

from pycnic.core import WSGI
from email_handler import EmailHandler 

class app(WSGI):
    routes = [
        ('/', EmailHandler()),
        (r'/email/([\w]+)', EmailHandler())
    ]

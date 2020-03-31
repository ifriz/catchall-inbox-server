###
# catch all inbox
###
import logging
from pycnic.core import WSGI
from email_handler import EmailHandler


class app(WSGI):
    logger = logging.Logger("catchall_inbox_servera")

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    ch.setFormatter(formatter)

    logger.addHandler(ch)

    logger.info("setting up routing")

    routes = [
        ('/', EmailHandler()),
        (r'/email', EmailHandler())
    ]

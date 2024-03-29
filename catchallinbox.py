###
# catch all inbox
###
import logging
from pycnic.core import WSGI
from email_handler import EmailHandler


class app(WSGI):
    logger = logging.Logger("catchall_inbox_server")

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    ch.setFormatter(formatter)

    logger.addHandler(ch)

    logger.info("setting up routing")

    # This allows * on all Handlers
    headers = [("Access-Control-Allow-Origin", "*"),
               ("Access-Control-Allow-Headers", "*")]


    routes = [
        ('/', EmailHandler()),
        (r'/email', EmailHandler())
        (r'/email/([\d]+)', EmailHandler())
    ]

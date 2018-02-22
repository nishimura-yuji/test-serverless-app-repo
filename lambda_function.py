""" This is test app. """

import logging
import os
import sys

LOGGER = logging.getLogger()
for h in LOGGER.handlers:
    LOGGER.removeHandler(h)

HANDLER = logging.StreamHandler(sys.stdout)
FORMAT = '%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s'
HANDLER.setFormatter(logging.Formatter(FORMAT))
LOGGER.addHandler(HANDLER)
LOGGER.setLevel(logging.INFO)


SET_WORD = os.getenv('SET_WORD', 'NOT GET Variable')

def handler(event, context):
    """
    main function
    """
    try:
        print(SET_WORD)
        return SET_WORD
    except Exception as error:
        LOGGER.exception(error)

import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('etl_application')
logger.setLevel(logging.INFO)

# INFO-level handler
fh = RotatingFileHandler('logs/etl_logs.log')
formatter = logging.Formatter('%(asctime)s %(levelname)-4s [%(filename)s:%(lineno)s]  %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

# ERROR-level handler
fh_error = RotatingFileHandler('logs/etl_errors.log')
formatter_error = logging.Formatter('%(asctime)s %(levelname)-4s [%(filename)s:%(lineno)s]  %(message)s')
fh_error.setFormatter(formatter_error)
fh_error.setLevel(logging.ERROR)
logger.addHandler(fh_error)
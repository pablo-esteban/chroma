import logging
import sys

LOG_FORMAT = "%(asctime)s,%(msecs)d %(levelname)s [%(pathname)s:%(funcName)s:%(lineno)d] %(message)s"
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"
log = logging.getLogger()
log.setLevel(logging.NOTSET)
handler = logging.StreamHandler(sys.stderr)
handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT))
log.addHandler(handler)
log.debug("Logging configured")

import logging

logging.Formatter
logging.basicConfig(level=logging.DEBUG, filename="sys.log", format='%(lineno)d-%(levelname)s-%(asctime)s')
logging.error("errorinfo:404")
logging.info("info:message")
logging.warning("warning:9999")
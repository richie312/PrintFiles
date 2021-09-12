import logging
from logging.handlers import RotatingFileHandler
# create logger
logger = logging.getLogger("py4j").setLevel(logging.ERROR)
logger = logging.getLogger('pyspark').setLevel(logging.ERROR)
logger = logging.getLogger("Asia_Asset_Logs")

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# handler = RotatingFileHandler('asia_asset.log', maxBytes=10000000, backupCount=100)
# logger.addHandler(handler)
# create formatter
formatter = logging.basicConfig(level=logging.DEBUG,
                    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
                    datefmt='%Y-%m-%dT%H:%M:%S')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)


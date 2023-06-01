import logging
import sys

logger = logging.getLogger("code-qa")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)

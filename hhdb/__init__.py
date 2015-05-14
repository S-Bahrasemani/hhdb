import rootpy
import logging
import os

rootpy.log.basic_config_colorized()

log = logging.getLogger('hhdb')
if not os.environ.get("DEBUG", False):
    log.setLevel(logging.INFO)

if hasattr(logging, 'captureWarnings'):
    logging.captureWarnings(True)

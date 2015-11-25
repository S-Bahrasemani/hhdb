import logging
import os

try:
    import rootpy
    rootpy.log.basic_config_colorized()
except ImportError:
    pass

log = logging.getLogger('hhdb')
if not os.environ.get("DEBUG", False):
    log.setLevel(logging.INFO)

if hasattr(logging, 'captureWarnings'):
    logging.captureWarnings(True)

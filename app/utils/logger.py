import logging
from datetime import datetime 
from config import settings
#from logging.handlers import RotatingFileHandler
import os
LOG_DIR="logs"
# os.makedirs(LOG_DIR,exist_ok=True)


#------------------------ Customer logger over basic logger -----------
logger =logging.getLogger("hackathon_logger")
logger.setLevel(logging.DEBUG if settings.debug else logging.INFO)



#------------Logger handlers ~~~~~~~~~Learn to prevent multiple handlers many time when --relaod 

console_log_handler=logging.StreamHandler()
file_handler = logging.FileHandler(os.path.join(LOG_DIR, "app.log"))
#file_handler = logging.FileHandler(f"{LOG_DIR}/app.log")


#           ~~~~~~~Learn -> to handle infinite logs production grade 
# file_handler = RotatingFileHandler(
#         log_file_path, maxBytes=5 * 1024 * 1024, backupCount=3
#     )

#---------------formatters for handlers
formatter = logging.Formatter(
    "[%(asctime)s - %(levelname)s - %(name)s- %(message)s]"
)
console_log_handler.setFormatter(formatter)

logger.addHandler(console_log_handler)
logger.addHandler(file_handler)
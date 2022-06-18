import imp
import logging
import datetime
import os

LOG_DIR = "housing_logs"  # within this directory, we will store all the logs

CURRENT_TIMESTAMP  = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

LOG_FILE_NAME = f"log_{CURRENT_TIMESTAMP}"


os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
filemode='w',
format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
level=logging.INFO)



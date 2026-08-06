"""
Application-wide constants.
"""

# -------------------------------
# API Configuration
# -------------------------------

BASE_URL = "https://api.adzuna.com/v1/api/jobs"

DEFAULT_COUNTRY = "gb"

RESULTS_PER_PAGE = 50

REQUEST_TIMEOUT = 30

MAX_RETRIES = 3

RETRY_DELAY_SECONDS = 5


# -------------------------------
# Logging
# -------------------------------

LOG_FILE_NAME = "pipeline.log"

LOG_LEVEL = "INFO"


# -------------------------------
# File Naming
# -------------------------------

RAW_FILE_PREFIX = "jobs"

DATE_TIME_FORMAT = "%Y%m%d_%H%M%S"


# -------------------------------
# Directories
# -------------------------------

RAW_DATA_FOLDER = "data/raw"

PROCESSED_DATA_FOLDER = "data/processed"

LOG_FOLDER = "logs"
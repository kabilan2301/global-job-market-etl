"""
Application configuration.
"""

from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

# Root directory of project
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Environment Variables
ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY")

COUNTRY = os.getenv("COUNTRY", "gb")
RESULTS_PER_PAGE = int(os.getenv("RESULTS_PER_PAGE", "50"))

# Paths
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"

PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed"

LOG_PATH = PROJECT_ROOT / "logs"
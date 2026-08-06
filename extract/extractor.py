import json
from datetime import datetime

from config.config import RAW_DATA_PATH

from config.constants import (
    DATE_TIME_FORMAT,
    RAW_FILE_PREFIX,
)

from config.logger import get_logger

from extract.adzuna_client import AdzunaClient


logger = get_logger(__name__)


class JobExtractor:

    def __init__(self):

        self.client = AdzunaClient()

    def extract(self):

        logger.info("Starting extraction")

        data = self.client.fetch_jobs()

        timestamp = datetime.now().strftime(
            DATE_TIME_FORMAT
        )

        filename = (
            f"{RAW_FILE_PREFIX}_{timestamp}.json"
        )

        file_path = RAW_DATA_PATH / filename

        with open(
            file_path,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
            )

        logger.info(
            f"Saved raw JSON to {file_path}"
        )

        return data
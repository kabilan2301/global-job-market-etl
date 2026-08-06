"""
Extraction service.
"""

from config.config import RAW_DATA_PATH

from config.logger import get_logger

from extract.adzuna_client import AdzunaClient

from utils.file_utils import save_json

logger = get_logger(__name__)


class JobExtractor:
    """Extracts jobs and saves raw JSON."""

    def __init__(self):

        self.client = AdzunaClient()

    def run(self) -> dict:

        logger.info("Starting extraction")

        data = self.client.fetch_jobs()

        saved_file = save_json(
            data=data,
            directory=RAW_DATA_PATH,
        )

        logger.info(
            "Raw JSON saved to %s",
            saved_file,
        )

        return data, saved_file
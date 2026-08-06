import requests

from config.config import (
    ADZUNA_APP_ID,
    ADZUNA_APP_KEY,
    COUNTRY,
    RESULTS_PER_PAGE,
)

from config.constants import (
    BASE_URL,
    REQUEST_TIMEOUT,
)

from config.logger import get_logger

from extract.base_client import BaseJobClient


logger = get_logger(__name__)


class AdzunaClient(BaseJobClient):

    def fetch_jobs(self):

        url = (
            f"{BASE_URL}/{COUNTRY}/search/1"
            f"?app_id={ADZUNA_APP_ID}"
            f"&app_key={ADZUNA_APP_KEY}"
            f"&results_per_page={RESULTS_PER_PAGE}"
        )

        logger.info("Connecting to Adzuna API")

        response = requests.get(
            url,
            timeout=REQUEST_TIMEOUT,
        )

        response.raise_for_status()

        logger.info("Successfully retrieved response")

        return response.json()
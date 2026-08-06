"""
Adzuna API client.
"""

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

from utils.exceptions import (
    APIConnectionError,
    InvalidAPIResponseError,
)

logger = get_logger(__name__)


class AdzunaClient(BaseJobClient):
    """Client for interacting with the Adzuna API."""

    def fetch_jobs(self) -> dict:

        url = (
            f"{BASE_URL}/{COUNTRY}/search/1"
            f"?app_id={ADZUNA_APP_ID}"
            f"&app_key={ADZUNA_APP_KEY}"
            f"&results_per_page={RESULTS_PER_PAGE}"
        )

        logger.info("Connecting to Adzuna API")

        try:

            response = requests.get(
                url,
                timeout=REQUEST_TIMEOUT,
            )

            response.raise_for_status()

        except requests.RequestException as exc:

            logger.exception("Unable to connect to Adzuna API")

            raise APIConnectionError(str(exc)) from exc

        data = response.json()

        if "results" not in data:

            raise InvalidAPIResponseError(
                "Response does not contain 'results'."
            )

        logger.info(
            "Successfully retrieved %s jobs",
            len(data["results"]),
        )

        return data
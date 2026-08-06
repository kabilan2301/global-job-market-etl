import requests


class AdzunaClient:
    BASE_URL = "https://api.adzuna.com/v1/api/jobs"

    def __init__(self, app_id: str, app_key: str) -> None:
        self.app_id = app_id
        self.app_key = app_key

    def search_jobs(self, country: str, params: dict) -> dict:
        url = f"{self.BASE_URL}/{country}/search/1"
        auth = {"app_id": self.app_id, "app_key": self.app_key}
        response = requests.get(url, params={**params, **auth})
        response.raise_for_status()
        return response.json()

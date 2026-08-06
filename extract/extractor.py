from .adzuna_client import AdzunaClient


class Extractor:
    def __init__(self, client: AdzunaClient) -> None:
        self.client = client

    def extract(self, country: str, query_params: dict) -> dict:
        return self.client.search_jobs(country, query_params)

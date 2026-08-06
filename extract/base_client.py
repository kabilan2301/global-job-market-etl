"""
Abstract base class for all job API clients.
"""

from abc import ABC, abstractmethod


class BaseJobClient(ABC):
    """Base interface for job API providers."""

    @abstractmethod
    def fetch_jobs(self) -> dict:
        """
        Fetch raw jobs from the provider.

        Returns
        -------
        dict
            Raw JSON response.
        """
        raise NotImplementedError
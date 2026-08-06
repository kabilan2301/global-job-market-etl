"""
Base interface for all job API clients.
"""

from abc import ABC, abstractmethod


class BaseJobClient(ABC):
    """
    Abstract base class for all job providers.
    """

    @abstractmethod
    def fetch_jobs(self):
        """
        Fetch job postings from a provider.

        Returns
        -------
        dict
            Raw JSON response.
        """
        pass
"""
Custom exceptions used throughout the ETL pipeline.
"""


class ETLPipelineException(Exception):
    """Base exception for all pipeline errors."""


class APIConnectionError(ETLPipelineException):
    """Raised when the job API cannot be reached."""


class InvalidAPIResponseError(ETLPipelineException):
    """Raised when the API response is malformed or missing required fields."""


class FileWriteError(ETLPipelineException):
    """Raised when a file cannot be written to disk."""
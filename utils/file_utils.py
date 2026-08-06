"""
Utility functions for file operations.
"""

import json
from datetime import datetime
from pathlib import Path

from config.constants import (
    DATE_TIME_FORMAT,
    RAW_FILE_PREFIX,
)

from utils.exceptions import FileWriteError


def generate_filename() -> str:
    """
    Generate a timestamped filename.

    Returns
    -------
    str
        Example:
        jobs_20260806_134512.json
    """

    timestamp = datetime.now().strftime(DATE_TIME_FORMAT)

    return f"{RAW_FILE_PREFIX}_{timestamp}.json"


def save_json(data: dict, directory: Path) -> Path:
    """
    Save JSON to disk.

    Parameters
    ----------
    data
        JSON object

    directory
        Destination folder

    Returns
    -------
    Path
        Saved file path
    """

    directory.mkdir(parents=True, exist_ok=True)

    filename = generate_filename()

    file_path = directory / filename

    try:

        with open(file_path, "w", encoding="utf-8") as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )

    except Exception as exc:

        raise FileWriteError(str(exc)) from exc

    return file_path
"""
Google Cloud Storage loader.
"""

from pathlib import Path

from google.cloud import storage

from config.config import GCS_BUCKET_NAME
from config.logger import get_logger

logger = get_logger(__name__)


class GCSLoader:
    """
    Upload files to Google Cloud Storage.
    """

    def __init__(self):

        self.client = storage.Client()

        self.bucket = self.client.bucket(GCS_BUCKET_NAME)

    def upload_file(self, file_path: Path) -> str:
        """
        Upload a file to Cloud Storage.

        Parameters
        ----------
        file_path : Path
            Local file path.

        Returns
        -------
        str
            GCS object name.
        """

        blob = self.bucket.blob(file_path.name)

        logger.info(
            "Uploading %s to bucket %s",
            file_path.name,
            GCS_BUCKET_NAME,
        )

        blob.upload_from_filename(str(file_path))

        logger.info(
            "Upload completed successfully."
        )

        return blob.name
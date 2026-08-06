"""
Application entry point.
"""

from config.logger import get_logger

from extract.extractor import JobExtractor
from load.gcs_loader import GCSLoader

logger = get_logger(__name__)


def main():

    logger.info("=" * 60)

    logger.info("Pipeline Started")

    extractor = JobExtractor()

    data, raw_file = extractor.run()

    gcs_loader = GCSLoader()

    object_name = gcs_loader.upload_file(raw_file)

    logger.info(
        "Uploaded object: %s",
        object_name,
    )

    logger.info(
        "Jobs extracted: %s",
        len(data["results"]),
    )

    logger.info("Pipeline Finished")

    logger.info("=" * 60)


if __name__ == "__main__":
    main()
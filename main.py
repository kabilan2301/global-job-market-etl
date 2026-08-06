"""
Application entry point.
"""

from config.logger import get_logger

from extract.extractor import JobExtractor

logger = get_logger(__name__)


def main():

    logger.info("=" * 60)

    logger.info("Global Job Market ETL Pipeline Started")

    extractor = JobExtractor()

    data = extractor.run()

    logger.info(
        "Pipeline completed successfully."
    )

    logger.info(
        "Jobs extracted: %s",
        len(data["results"]),
    )

    logger.info("=" * 60)


if __name__ == "__main__":
    main()
from config.logger import get_logger

from extract.extractor import JobExtractor


logger = get_logger(__name__)


def main():

    logger.info("Pipeline Started")

    extractor = JobExtractor()

    data = extractor.extract()

    logger.info(
        f"Retrieved {len(data['results'])} jobs"
    )

    logger.info("Pipeline Finished")


if __name__ == "__main__":
    main()
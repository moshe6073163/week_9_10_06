import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s",
    handlers = [
        logging.StreamHandler(),
        logging.FileHandler("app.log")
    ]
)

logger = logging.getLogger(__name__)
import logging
import subprocess
from config.config import Config


logger = logging.getLogger(__name__)


def start_rq_worker():
    logger.info("starting redis queue worker")
    subprocess.run(["rq", "worker", Config.QUEUE_NAME])
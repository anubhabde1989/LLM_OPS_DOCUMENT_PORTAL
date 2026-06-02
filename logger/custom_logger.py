import logging
import sys
import os
from datetime import datetime
import structlog

class CustomLogger:
    def __init__(self, log_dir="logs"):
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)

        #Create timestamped log file name
        self.log_file = f"{datetime.now().strftime('%m-%d-%Y-%H-%M-%S')}.log"
        self.log_file_path = os.path.join(self.logs_dir, self.log_file)

        #Configure Logging
        logging.basicConfig(
                            filename = self.log_file_path,
                            format="[%(asctime)s] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s",
                            level = logging.INFO,)

    def get_logger(self, name = __file__):
        logger_name = os.path.basename(name)
        # Configure logging for both console + file (JSON format)
        file_handler = logging.FileHandler(self.log_file_path)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter("%(message)s")) #Raw Json lines

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter("%(message)s"))

        logging.basicConfig(level=logging.INFO, format="%(message)s", handlers=[console_handler, file_handler], force=True)

        structlog.configure(
            processors=[
                structlog.processors.TimeStamper(fmt="iso", utc=True, key="timestamp"),
                structlog.processors.add_log_level,
                structlog.processors.EventRenamer(to="event"),
                structlog.processors.JSONRenderer()
            ],
            logger_factory=structlog.stdlib.LoggerFactory(),
            cache_logger_on_first_use=True,
        )   

        return structlog.getLogger(logger_name)
    
if __name__ == "__main__":
    logger = CustomLogger()
    logger=logger.get_logger(__file__)
    logger.info("Custom logger initialized successfully.")
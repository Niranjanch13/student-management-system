import logging
from pathlib import Path

# Store logs in a file inside the project directory
LOG_FILE = Path(__file__).resolve().parent / "app.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)


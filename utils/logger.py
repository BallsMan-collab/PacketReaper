# utils/logger.py

import logging
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = f"packetreaper_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Create the logs directory if it doesn't exist
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Configure the logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=LOG_PATH,
    filemode='w'  # 'w' to overwrite each run, use 'a' to append
)

# Get the logger instance
logger = logging.getLogger(__name__)

def log(level, message):
    """
    Logs a message with the specified level.

    Args:
        level (str): The logging level (e.g., 'info', 'warning', 'error').
        message (str): The message to log.
    """
    level = level.lower()
    if level == 'info':
        logger.info(message)
    elif level == 'warning':
        logger.warning(message)
    elif level == 'error':
        logger.error(message)
    elif level == 'debug':
        logger.debug(message)
    else:
        logger.info(f"[{level.upper()}] {message}") # Default to info with custom level


def info(message):
    """Logs an informational message."""
    log('info', message)

def warning(message):
    """Logs a warning message."""
    log('warning', message)

def error(message):
    """Logs an error message."""
    log('error', message)

def debug(message):
    """Logs a debug message."""
    log('debug', message)

if __name__ == "__main__":
    # Example usage (for testing the module directly)
    info("This is an informational message.")
    warning("This is a warning message.")
    error("This is an error message.")
    debug("This is a debug message (will only show if logging level is set to DEBUG).")
    print(f"Logs are being written to: {LOG_PATH}")

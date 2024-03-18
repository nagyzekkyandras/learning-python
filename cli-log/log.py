import logging
import os
import sys

# Get log level from environment variable, defaulting to DEBUG
log_level = os.environ.get('LOG_LEVEL', 'DEBUG').upper()

# Configure logging
logging.basicConfig(level=log_level,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    stream=sys.stdout) # or specific file

# Create a logger
logger = logging.getLogger()

# Log messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

def main() -> None:
    logger.info("This script is running: " + os.path.basename(__file__))

if __name__ == '__main__':
    main()
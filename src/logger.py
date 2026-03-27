import logging

logging.basicConfig(
    filename="reports/log.txt",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def log(message):
    print(message)
    logging.info(message)
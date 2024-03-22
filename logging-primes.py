import logging
from pythonjsonlogger import jsonlogger
from datetime import datetime
import time
import sympy

class JsonFormatter(jsonlogger.JsonFormatter):
  def add_fields(self, log_record, record, message_dict):
    super(JsonFormatter, self).add_fields(log_record, record, message_dict)
    if not log_record.get("timestamp"):
      now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
      log_record["timestamp"] = now
    if log_record.get("level"):
      log_record["level"] = log_record["level"].upper()
    else:
      log_record["level"] = record.levelname

logger = logging.getLogger()

logHandler = logging.StreamHandler()
formatter = JsonFormatter("%(timestamp)s %(level)s %(name)s %(message)s")
logHandler.setFormatter(formatter)

logger.setLevel(logging.DEBUG)
logger.addHandler(logHandler)

number = 0

while True:
  level = number % 4
  if level == 0:
    logger.info("New number", extra={"Number": number})
  elif level == 1:
    logger.debug("New number", extra={"Number": number})
  elif level == 2:
    logger.error("New number", extra={"Number": number})
  elif level == 3:
    logger.warning("New number", extra={"Number": number})

  time.sleep(1)
  if sympy.isprime(number):
    logger.critical("Prime found!", extra={"Prime Number": number})
    time.sleep(3)
  number += 1

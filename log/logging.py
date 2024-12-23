from logging import basicConfig, getLogger
import logfire
import logging

class Logging():

  def __init__(self):
    logfire.configure()
    basicConfig(handlers=[logfire.LogfireLoggingHandler()])
    self.logger = getLogger(__name__)
    self.logger.setLevel(logging.INFO)
    logfire.instrument_requests()
    logfire.instrument_sqlalchemy()

  def get_logger(self):
    return self.logger
  
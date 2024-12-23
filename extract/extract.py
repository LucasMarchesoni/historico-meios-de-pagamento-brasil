import requests
from log.logging import Logging

class Extract:
  
  def __init__(self, url:str):
    self.url = url
    self.log = Logging()

  def response(self) -> requests.Response:
    data = requests.get(self.url)

    if data.status_code != 200:
      return self.log.get_logger().error("Error on collecting data")

    return data.json()
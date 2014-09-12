import sys, glob
sys.path.append('gen-py')

from livetex.authentication_private.ttypes import *
from livetex.endpoint.ttypes import *

class AuthenticationPrivateHandler:
  def removeToken(self, token):
    pass

  def checkToken(self, token):
    result = CheckTokenResult()
    result.result = True
    result.options = { 'optName': 'optVal' }
    return result

  def addEndpoints(self, service, environment, endpoints):
    pass

  def removeEndpoints(self, service, environment, endpoints):
    pass

  def getEndpoints(self, service, environment):
    endpoint1 = Endpoint('chat1.livetex.ru', 80, 'http', '/');
    endpoint2 = Endpoint('chat2.livetex.ru', 443, 'https', '/');
    return [endpoint1, endpoint2]

  def changeEnvironment(self, client, environment):
    pass
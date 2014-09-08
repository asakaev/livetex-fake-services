import sys, glob
sys.path.append('gen-py')
sys.path.insert(0, glob.glob('build/thrift/build/lib.*')[0])

from authentication.ttypes import *
from authentication import AuthenticationPrivate

class AuthenticationPrivateHandler:
  def removeToken(self, token):
    pass

  def checkToken(self, token):
    result = CheckTokenResult()
    result.result = 1
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
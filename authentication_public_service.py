import sys, glob, random
sys.path.append('gen-py')
sys.path.insert(0, glob.glob('build/thrift/build/lib.*')[0])

from authentication.ttypes import *
from authentication import AuthenticationPublic


class AuthenticationPublicHandler:
  def getToken(self, client):
    endpoint = Endpoint('chat.livetex.ru', 8080, 'http', '/');
    result = AuthenticationResult()
    result.token = hex(random.randint(pow(2, 32), pow(2, 34)))[2:]
    result.services = { 'chat': endpoint }
    result.options = { 'optName': 'optVal' }
    return result
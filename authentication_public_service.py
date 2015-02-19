import sys, glob, random
sys.path.append('gen-py')

from livetex.authentication_public.ttypes import *
from livetex.livetex_service.ttypes import *
from livetex.endpoint.ttypes import *

from livetex.authentication_public import AuthenticationPublic


class AuthenticationPublicHandler:
  def getVisitorApplicationToken(self, client):
    endpoint = Endpoint(1, 'chat.livetex.ru', 8080, 'http', '/');
    result = AuthenticationResult()
    result.token = 'some_token'
    result.services = { LivetexService.DIALOG: endpoint }
    result.options = { 'optName': 'optVal' }
    return result

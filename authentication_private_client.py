import sys, glob
sys.path.append('gen-py')

from thrift import Thrift
from thrift.transport import THttpClient
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TJSONProtocol
from thrift.server import THttpServer

from livetex.authentication_private import AuthenticationPrivate

from livetex.endpoint.ttypes import *
from livetex.livetex_service.ttypes import *
from livetex.environment.ttypes import *
from livetex.token.ttypes import *
from livetex.client_entity.ttypes import *

try:

  transport = THttpClient.THttpClient('http://localhost:10020/')
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  client = AuthenticationPrivate.Client(protocol)

  token = 'some_token'
  service = LivetexService.DIALOG
  environment = 'dev'
  endpoint1 = Endpoint('chat1.livetex.ru', 80, 'http', '/');
  endpoint2 = Endpoint('chat2.livetex.ru', 443, 'https', '/');
  endpoints = [endpoint1, endpoint2]
  application = VisitorApplication()
  application.token = 'some_token'
  application.application = 'application'
  application.key = 'api_key'
  
  transport.open()

  client.removeToken('some_token')
  print 'remove token is ok'

  print 'check token is ok: ' + str(client.checkToken('some_token'))

  client.addEndpoints(service, environment, endpoints)
  print 'add endpoint is ok'

  client.removeEndpoints(service, environment, endpoints)
  print 'remove endpoint is ok'

  print 'get endpoints is ok ' + str(client.getEndpoints(service, environment))

  client.changeVisitorApplicationEnvironment(application, environment)
  print 'change environment is ok'

  transport.close()

except Thrift.TException, tx:
  
  print '%s' % (tx.message)
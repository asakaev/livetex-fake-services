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

  transport = THttpClient.THttpClient('http://localhost:10010/')
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  client = AuthenticationPrivate.Client(protocol)

  token = 'some_token'
  service = LivetexService.DIALOG
  environment = 'default_env'
  endpoint1 = Endpoint(0, '127.0.0.1', 10040, 'http', '/');
  endpoint2 = Endpoint(0, 'chat2.livetex.ru', 443, 'https', '/');
  endpoints = [endpoint1, endpoint2]
  application = VisitorApplication()
  application.token = 'some_token'
  application.application = 'application'
  application.key = 'api_key'

  transport.open()

  # client.removeToken('account:5832:site:10005638:visitor:b7agnzxeq7ntrzfr')
  # print 'remove token is ok'

  # print 'check token is ok: ' + str(
  #     client.checkVisitorToken('account:5832:site:10005638:visitor:b7agnzxeq7ntrzfr', endpoint1))

  # client.addEndpoint(environment, endpoint1)
  # print 'add endpoint is ok'

  # client.removeEndpoint(environment, endpoint1)
  # print 'remove endpoint is ok'

  # print 'get endpoints is ok ' + str(client.getEndpoints(service, environment))

  # client.changeVisitorApplicationEnvironment(application, environment)
  # print 'change environment is ok'

  transport.close()

except Thrift.TException, tx:
  
  print '%s' % (tx.message)
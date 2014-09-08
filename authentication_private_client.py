import sys, glob
sys.path.append('gen-py')
sys.path.insert(0, glob.glob('build/thrift/build/lib.*')[0])

from thrift import Thrift
from thrift.transport import THttpClient
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TJSONProtocol
from thrift.server import THttpServer

from authentication.ttypes import *
from authentication import AuthenticationPrivate

try:

  transport = THttpClient.THttpClient('http://localhost:9091/')
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  client = AuthenticationPrivate.Client(protocol)

  token = 'some_token'
  service = 'event_service'
  environment = 'dev'
  endpoint1 = Endpoint('chat1.livetex.ru', 80, 'http', '/');
  endpoint2 = Endpoint('chat2.livetex.ru', 443, 'https', '/');
  endpoints = [endpoint1, endpoint2]
  clientEntity = ClientEntity('5468', 'visitor', { 'some_opt': 'some_val' })
  
  transport.open()

  client.removeToken('some_token')
  print 'remove token is ok'

  print 'check token is ok: ' + str(client.checkToken('some_token'))

  client.addEndpoints(service, environment, endpoints)
  print 'add endpoint is ok'

  client.removeEndpoints(service, environment, endpoints)
  print 'remove endpoint is ok'

  print 'get endpoints is ok ' + str(client.getEndpoints(service, environment))

  client.changeEnvironment(clientEntity, environment)
  print 'change environment is ok'

  transport.close()

except Thrift.TException, tx:
  
  print '%s' % (tx.message)
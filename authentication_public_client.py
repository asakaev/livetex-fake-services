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
from authentication import AuthenticationPublic

try:

  transport = THttpClient.THttpClient('http://localhost:9090/')
  #protocol = TJSONProtocol.TJSONProtocol(transport)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  client = AuthenticationPublic.Client(protocol)
  
  transport.open()

  clientEntity = ClientEntity()
  clientEntity.id = 'asd'
  clientEntity.type = 'asdasd'
  clientEntity.options = { 'ad': 'ads' }
  print client.getToken(clientEntity)

  transport.close()

except Thrift.TException, tx:
  
  print '%s' % (tx.message)
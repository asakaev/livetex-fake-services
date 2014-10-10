import sys, glob
sys.path.append('gen-py')

from thrift import Thrift
from thrift.transport import THttpClient
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TJSONProtocol
from thrift.server import THttpServer

from livetex.authentication_public.ttypes import *
from livetex.client_entity.ttypes import *
from livetex.capabilities.ttypes import *

from livetex.authentication_public import AuthenticationPublic

try:

  transport = THttpClient.THttpClient('http://localhost:10010/')
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  client = AuthenticationPublic.Client(protocol)
  
  transport.open()

  VisitorApplication = VisitorApplication()
  VisitorApplication.token = 'some_token'
  VisitorApplication.application = 'application'
  VisitorApplication.key = 'api_key'
  VisitorApplication.capabilities = [ Capabilities.CHAT, Capabilities.LEAD ]
  print client.getVisitorApplicationToken(VisitorApplication)

  transport.close()

except Thrift.TException, tx:
  
  print '%s' % (tx.message)
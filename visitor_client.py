import sys, glob
sys.path.append('gen-py')

from thrift import Thrift
from thrift.transport import THttpClient
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TJSONProtocol
from thrift.server import THttpServer

from livetex.visitor_data import Visitor

try:

  # transport = THttpClient.THttpClient('http://sdk.livetex.ru:10070/account:123445:site:89200:visitor:ggrh5reh2cutmx6r')
  # transport = THttpClient.THttpClient('http://192.168.78.14:10070/account:5832:site:10005638:visitor:edww0pjo8pno2yb9')
  transport = THttpClient.THttpClient('http://localhost:10070/account:5832:site:10005638:visitor:0arvucc7sx9u23xr')
  # protocol = TBinaryProtocol.TBinaryProtocol(transport)
  protocol = TJSONProtocol.TJSONProtocol(transport)

  client = Visitor.Client(protocol)
  
  transport.open()

  client.setName('some_name')
  print 'setName is ok'

  transport.close()


except Thrift.TException, tx:
  
  print '%s' % (tx.message)
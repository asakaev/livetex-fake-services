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

  transport = THttpClient.THttpClient('http://localhost:10060/')
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  client = Visitor.Client(protocol)
  
  transport.open()

  client.setName('some_name')
  print 'setName is ok'

  transport.close()


except Thrift.TException, tx:
  
  print '%s' % (tx.message)
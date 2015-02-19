import sys, glob, random, threading, time, BaseHTTPServer
sys.path.append('gen-py')

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TJSONProtocol
from thrift.server import THttpServer

from livetex.visitor_data import Visitor

from visitor_service import VisitorHandler

hadler = VisitorHandler()
#pfactory = TBinaryProtocol.TBinaryProtocolFactory()
pfactory = TJSONProtocol.TJSONProtocolFactory()
processor = Visitor.Processor(hadler)

server = THttpServer.THttpServer(processor, ('localhost', 10070), pfactory)
print 'Visitor 10060 serve...'
server.serve()
import sys, glob, random, threading, time
sys.path.append('gen-py')

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TJSONProtocol
from thrift.server import THttpServer

from livetex.authentication_private import AuthenticationPrivate

from authentication_private_service import AuthenticationPrivateHandler

handler = AuthenticationPrivateHandler()
pfactory = TJSONProtocol.TJSONProtocolFactory()
processor = AuthenticationPrivate.Processor(handler)

server = THttpServer.THttpServer(processor, ('localhost', 10020), pfactory)
print 'Authentication private 10020 serve...'
server.serve()
import sys, glob, random, threading, time
sys.path.append('gen-py')

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TJSONProtocol
from thrift.server import THttpServer

from livetex.authentication_public.ttypes import *
from livetex.authentication_public import AuthenticationPublic

from authentication_public_service import AuthenticationPublicHandler

authPublicHandler = AuthenticationPublicHandler()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
#pfactory = TJSONProtocol.TJSONProtocolFactory()
processor = AuthenticationPublic.Processor(authPublicHandler)

server = THttpServer.THttpServer(processor, ('0.0.0.0', 10010), pfactory)
print 'Authentication public 10010 serve...'
server.serve()

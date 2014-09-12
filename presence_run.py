import sys, glob, random, threading, time
sys.path.append('gen-py')

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TJSONProtocol
from thrift.server import THttpServer

from livetex.presence import Presence

from presence_service import PresenceHandler

hadler = PresenceHandler()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
processor = Presence.Processor(hadler)

server = THttpServer.THttpServer(processor, ('localhost', 10050), pfactory)
print 'Presence 10050 serve...'
server.serve()
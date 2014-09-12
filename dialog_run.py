import sys, glob, random, threading, time
sys.path.append('gen-py')

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TJSONProtocol
from thrift.server import THttpServer

from livetex.dialog import Dialog

from dialog_service import DialogHandler

hadler = DialogHandler()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
processor = Dialog.Processor(hadler)

server = THttpServer.THttpServer(processor, ('localhost', 10030), pfactory)
print 'Dialog 10030 serve...'
server.serve()
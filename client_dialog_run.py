import sys, glob, random, threading, time
sys.path.append('gen-py')

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TJSONProtocol
from thrift.server import THttpServer

from livetex.dialog import ClientDialog

from client_dialog_service import ClientDialogHandler

hadler = ClientDialogHandler()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
processor = ClientDialog.Processor(hadler)

server = THttpServer.THttpServer(processor, ('localhost', 10040), pfactory)
print 'Client dialog 10040 serve...'
server.serve()
import sys, glob, random, threading, time
sys.path.append('gen-py')
sys.path.insert(0, glob.glob('build/thrift/build/lib.*')[0])

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TJSONProtocol
from thrift.server import THttpServer

from authentication.ttypes import *
from authentication import AuthenticationPublic
from authentication import AuthenticationPrivate

from authentication_public_service import AuthenticationPublicHandler
from authentication_private_service import AuthenticationPrivateHandler

authPublicHandler = AuthenticationPublicHandler()
authPrivateHandler = AuthenticationPrivateHandler()

pfactory = TBinaryProtocol.TBinaryProtocolFactory()

pubProcessor = AuthenticationPublic.Processor(authPublicHandler)
privProcessor = AuthenticationPrivate.Processor(authPrivateHandler)


def runServer(processor, port, name):
  server = THttpServer.THttpServer(processor, ('localhost', port), pfactory)
  print 'Starting the ' + name + ' server...'
  server.serve()

pubThread = threading.Thread(target=runServer, args=(pubProcessor, 9090, 'public'))
pubThread.daemon = True
privThread = threading.Thread(target=runServer, args=(privProcessor, 9091, 'private'))
privThread.daemon = True

pubThread.start()
privThread.start()

while True:
    time.sleep(1)
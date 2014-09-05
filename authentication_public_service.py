import sys, glob, random
sys.path.append('gen-py')
sys.path.insert(0, glob.glob('build/thrift/build/lib.*')[0])

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TJSONProtocol
from thrift.server import THttpServer

from authentication.ttypes import *
from authentication import AuthenticationPublic

class AuthenticationPublicHandler:
	def getToken(self, client):
		endpoint = Endpoint('chat.livetex.ru', 8080, 'http', '/');
		result = AuthenticationResult()
		result.token = hex(random.randint(pow(2, 32), pow(2, 34)))[2:]
		result.services = { 'chat': endpoint }
		result.options = { 'optName': 'optVal' }
		return result

authPublicHandler = AuthenticationPublicHandler()

processor = AuthenticationPublic.Processor(authPublicHandler)
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
#pfactory = TJSONProtocol.TJSONProtocolFactory()

server = THttpServer.THttpServer(processor, ('localhost', 9090), pfactory)

print 'Starting the server...'
server.serve()
print 'done.'

# 1: required Token token;
# 2: required map<Service, Endpoint> services;
# 3: optional Options options;
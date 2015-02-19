import sys, glob
sys.path.append('gen-py')

from thrift import Thrift
from thrift.transport import THttpClient
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TJSONProtocol
from thrift.server import THttpServer

from livetex.authentication_public.ttypes import *
from livetex.client_entity.ttypes import *
from livetex.capabilities.ttypes import *
from livetex.visitor_device.ttypes import *

from livetex.authentication_public import AuthenticationPublic

try:

  transport = THttpClient.THttpClient('http://authentication-service-sdk-production-1.livetex.ru/')
  # transport = THttpClient.THttpClient('http://authentication-service-sdk-prerelease.livetex.ru/')
  # transport = THttpClient.THttpClient('http://authentication-service-sdk.livetex.ru/')
  # transport = THttpClient.THttpClient('http://authentication-service-sandbox.sandbox.livetex/')
  # transport = THttpClient.THttpClient('http://localhost:10010/')
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  client = AuthenticationPublic.Client(protocol)
  
  transport.open()

  # visitorApplication = VisitorApplication()
  # visitorApplication.application = '10005638'
  # visitorApplication.key = 'dev_key_test'
  # visitorApplication.capabilities = [ Capabilities.CHAT, Capabilities.FILES_RECEIVE ]
  # print client.getVisitorApplicationToken(visitorApplication)

  visitorApplication = VisitorApplication()
  visitorApplication.application = '91605'
  visitorApplication.key = 'release_key'
  visitorApplication.capabilities = [ Capabilities.CHAT, Capabilities.FILES_RECEIVE ]
  print client.getVisitorApplicationToken(visitorApplication)

  # visitorDevice = VisitorDevice()
  # visitorDevice.application = '91605'
  # visitorDevice.key = 'prerelease_key'
  # visitorDevice.capabilities = [ Capabilities.CHAT, Capabilities.FILES_RECEIVE ]
  # visitorDevice.deviceId = '6a313589b1df541d672a9bcf268975f717c83fe488ecb5ceab44b2765b391c73'
  # visitorDevice.deviceType = 1
  # print client.getVisitorDeviceToken(visitorDevice)

  # visitorDevice = VisitorDevice()
  # visitorDevice.application = '10005638'
  # visitorDevice.key = 'dev_key_test'
  # visitorDevice.capabilities = [ Capabilities.CHAT, Capabilities.FILES_RECEIVE ]
  # visitorDevice.deviceId = '6a313589b1df541d672a9bcf268975f717c83fe488ecb5ceab44b2765b391c73'
  # visitorDevice.deviceType = 1
  # print client.getVisitorDeviceToken(visitorDevice)


  transport.close()

except Thrift.TException, tx:
  
  print '%s' % (tx.message)



import sys, glob, time
sys.path.append('gen-py')

from thrift import Thrift
from thrift.transport import THttpClient
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TJSONProtocol
from thrift.server import THttpServer

from livetex.dialog.ttypes import *
from livetex.operator.ttypes import *

from livetex.dialog import ClientDialog

try:

  transport = THttpClient.THttpClient('http://localhost:10040/')
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  client = ClientDialog.Client(protocol)
  
  transport.open()

  operator = Operator()
  operator.id = '5745'
  operator.status = 'some_status_1'
  operator.firstname = 'Piter'
  operator.lastname = 'Parker'
  operator.avatar = 'http://billing.env-02.unstable/Images/icons/icon-no-oper.png'
  operator.phone = '545-8874-854'
  operator.email = 'example@example.example'
  operator.options = { 'opt1': 'val1' }
  message = 'some_simple_message'
  fileMessage = FileMessage()
  fileMessage.type = FileMessageType.MEMBER_FILE_MESSAGE
  fileMessage.id = '698745'
  fileMessage.text = 'take The MEGA FILE'
  fileMessage.timestamp = str(time.time())
  fileMessage.url = 'https://github.com/hobbit-vt/livetex-fake-services/blob/master/authentication_private_client.py'
  textMessage = TextMessage()
  textMessage.type = TextMessageType.MEMBER_MESSAGE
  textMessage.id = '664238'
  textMessage.text = 'some text'
  textMessage.timestamp = str(time.time())
  holdMessage = HoldMessage()
  typingMessage = TypingMessage('Typing is awesome')
  
  client.dialog()
  print 'dialog is ok'

  client.close()
  print 'close is ok'

  client.member(operator)
  print 'member is ok'

  client.receiveFileMessage(fileMessage)
  print 'receiveFileMessage is ok'
  
  client.receiveTextMessage(textMessage)
  print 'receiveTextMessage is ok'

  client.confirmTextMessage(textMessage)
  print 'confirmTextMessage is ok'

  client.receiveHoldMessage(holdMessage)
  print 'receiveHoldMessage is ok'

  client.receiveTypingMessage(typingMessage)
  print 'receiveTypingMessage is ok'

except Thrift.TException, tx:
  
  print '%s' % (tx.message)
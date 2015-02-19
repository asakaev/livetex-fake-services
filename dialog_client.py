# -*- coding: utf-8 -*-
import sys, glob
sys.path.append('gen-py')

from thrift import Thrift
from thrift.transport import THttpClient
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TJSONProtocol
from thrift.server import THttpServer

from livetex.dialog.ttypes import *
from livetex.employee.ttypes import *
from livetex.department.ttypes import *
from livetex.vote.ttypes import *
from livetex.message.ttypes import *
from livetex.abuse.ttypes import *

from livetex.dialog import Dialog

try:

  transport = THttpClient.THttpClient('http://dialog-service-0-sdk-production-2.livetex.ru/account:126927:site:91605:visitor:7i9es8zi5obhuxr')
  # transport = THttpClient.THttpClient('http://dialog-service-0-sdk-prerelease.livetex.ru/account:126927:site:91605:visitor:rulajlq9zh69a4i')
  # transport = THttpClient.THttpClient('http://dialog-service-0-sdk.livetex.ru/account:123445:site:89200:visitor:i2dhjzwep5e9udi')
  # transport = THttpClient.THttpClient('http://dialog-service-0-sandbox.sandbox.livetex/account:5832:site:10005638:visitor:21tpy9syabjfw29')
  # transport = THttpClient.THttpClient('http://localhost:10040/account:5832:site:10005638:visitor:vkbn8q5m7l6dpldi')
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  client = Dialog.Client(protocol)

  transport.open()

  dialogAttributes = DialogAttributes({'some': 'some'}, {'some1': 'some1'})
  typingMessage = TypingMessage('typing...')

  
  # print 'close is ok ' + str(client.close())
  client.request(dialogAttributes)
  print 'request is ok'

  # state = client.requestEmployee('45', dialogAttributes)
  # print  'requestOperator is ok ' + str(state)

  # state = client.requestDepartment('7116', dialogAttributes)
  # print 'requestDepartment is ok ' + str(state)

  # print 'close is ok ' + str(client.close())

  # client.vote(1)
  # print 'vote is ok'

  # client.abuse(Abuse('123345', 'asdasd'))
  # print 'abuse is ok'

  # client.typing(typingMessage)
  # print 'typing is ok'

  # textMessage = client.sendTextMessage('some text')
  # print 'sendTextMessage is ok: ' + str(textMessage)

  # client.confirmTextMessage('1809236')
  # print 'confirmTextMessage is ok'

  # history = client.messageHistory(20, 0)
  # print 'messageHistory is ok: ' + str(history)

  # print 'get state is ok ' + str(client.getState())

except Thrift.TException, tx:
  print '%s' % (tx.message)

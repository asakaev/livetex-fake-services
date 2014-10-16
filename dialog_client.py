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

from livetex.dialog import Dialog

try:

  transport = THttpClient.THttpClient('http://localhost:10030/')
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  client = Dialog.Client(protocol)
  
  transport.open()

  dialogAttributes = DialogAttributes()
  employee = Employee()
  employee.id = '5745'
  employee.status = 'some_status_1'
  employee.firstname = 'Piter'
  employee.lastname = 'Parker'
  employee.avatar = 'http://billing.env-02.unstable/Images/icons/icon-no-oper.png'
  employee.phone = '545-8874-854'
  employee.email = 'example@example.example'
  employee.options = { 'opt1': 'val1' }
  department = Department('56', 'some_name', { 'opt1': 'val1' })
  vote = Vote(VoteType.GOOD, 'some good message')
  typingMessage = TypingMessage('Typing is awesome')
  
  client.request(dialogAttributes)
  print 'request is ok'

  client.requestEmployee(employee, dialogAttributes)
  print 'requestOperator is ok'

  client.requestDepartment(department, dialogAttributes)
  print 'requestDepartment is ok'

  client.close()
  print 'close is ok'

  client.vote(vote)
  print 'vote is ok'

  client.typing(typingMessage)
  print 'typing is ok'

  textMessage = client.sendTextMessage('some text')
  print 'sendTextMessage is ok: ' + str(textMessage)

  client.confirmTextMessage(textMessage)
  print 'confirmTextMessage is ok'

  history = client.messageHistory(16, 16)
  print 'messageHistory is ok: ' + str(history)

  print client.getState()
  print 'getState is ok'

except Thrift.TException, tx:
  
  print '%s' % (tx.message)
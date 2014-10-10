import sys, glob, time
sys.path.append('gen-py')

from livetex.dialog.ttypes import *
from livetex.operator.ttypes import *
from livetex.department.ttypes import *
from livetex.dialog_state.ttypes import *
from livetex.conversation.ttypes import *
from livetex.message.ttypes import *

class DialogHandler:
  operator1 = Operator()
  operator2 = Operator()
  department = Department()

  def __init__(self):
    self.operator1.id = '5745'
    self.operator1.status = 'some_status_1'
    self.operator1.firstname = 'Piter'
    self.operator1.lastname = 'Parker'
    self.operator1.avatar = 'http://billing.env-02.unstable/Images/icons/icon-no-oper.png'
    self.operator1.phone = '545-8874-854'
    self.operator1.email = 'example@example.example'
    self.operator1.options = { 'opt1': 'val1' }

    self.operator2.id = '5744'
    self.operator2.status = 'some_status_2'
    self.operator2.firstname = 'Marry'
    self.operator2.lastname = 'Jane'
    self.operator2.avatar = 'http://billing.env-02.unstable/Images/icons/icon-no-oper.png'
    self.operator2.phone = '145-8874-854'
    self.operator2.email = 'example@example.example'
    self.operator2.options = { 'opt1': 'val1' }

    self.department.id = '557'
    self.department.name = 'some_name'
    self.department.options = { 'opt1': 'val1' }

  def request(self, attributes):
    return DialogState(Conversation(self.operator1, self.department), self.operator2)

  def requestOperator(self, operator, attributes):
    return DialogState(Conversation(operator, self.department), self.operator2)

  def requestDepartment(self, department, attributes):
    return DialogState(Conversation(self.operator1, department), self.operator2)

  def close(self):
    return DialogState(Conversation(self.operator2, self.department), self.operator1)

  def vote(self, vote):
    pass
  def typing(self, message):
    pass
  def sendTextMessage(self, text):
    textMessage = TextMessage()
    textMessage.id = '546'
    textMessage.text = text
    textMessage.timestamp = str(time.time())
    return textMessage

  def confirmTextMessage(self, message):
    pass

  def messageHistory(self, limit, offset):
    textMessage1 = TextMessage()
    textMessage1.id = '547'
    textMessage1.text = 'Hi there!'
    textMessage1.timestamp = str(time.time() - 500)
    textMessage1.source = self.operator1
    textMessage1.target = self.operator2

    textMessage2 = TextMessage()
    textMessage2.id = '548'
    textMessage2.text = 'Can i help you?'
    textMessage2.timestamp = str(time.time())
    textMessage2.source = self.operator2
    textMessage2.target = self.operator1
    return [textMessage1, textMessage2]

  def getState(self):
    return DialogState(Conversation(self.operator1, self.department), self.operator2)
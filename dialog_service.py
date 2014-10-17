import sys, glob, time
sys.path.append('gen-py')

from livetex.dialog.ttypes import *
from livetex.employee.ttypes import *
from livetex.department.ttypes import *
from livetex.dialog_state.ttypes import *
from livetex.conversation.ttypes import *
from livetex.message.ttypes import *

class DialogHandler:
  employee1 = Employee()
  employee2 = Employee()
  department = Department()

  def __init__(self):
    self.employee1.id = '5745'
    self.employee1.status = 'some_status_1'
    self.employee1.firstname = 'Piter'
    self.employee1.lastname = 'Parker'
    self.employee1.avatar = 'http://billing.env-02.unstable/Images/icons/icon-no-oper.png'
    self.employee1.phone = '545-8874-854'
    self.employee1.email = 'example@example.example'
    self.employee1.options = { 'opt1': 'val1' }

    self.employee2.id = '5744'
    self.employee2.status = 'some_status_2'
    self.employee2.firstname = 'Marry'
    self.employee2.lastname = 'Jane'
    self.employee2.avatar = 'http://billing.env-02.unstable/Images/icons/icon-no-oper.png'
    self.employee2.phone = '145-8874-854'
    self.employee2.email = 'example@example.example'
    self.employee2.options = { 'opt1': 'val1' }

    self.department.id = '557'
    self.department.name = 'some_name'
    self.department.options = { 'opt1': 'val1' }

  def request(self, attributes):
    return DialogState(Conversation(self.employee1, self.department), self.employee2)

  def requestEmployee(self, operator, attributes):
    return DialogState(Conversation(self.employee1, self.department), self.employee2)

  def requestDepartment(self, department, attributes):
    return DialogState(Conversation(self.employee1, self.department), self.employee2)

  def close(self):
    return DialogState(Conversation(self.employee2, self.department), self.employee1)

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
    textMessage1.sender = self.employee1

    textMessage2 = TextMessage()
    textMessage2.id = '548'
    textMessage2.text = 'Can i help you?'
    textMessage2.timestamp = str(time.time())
    textMessage2.sender = self.employee2
    return [textMessage1, textMessage2]

  def getState(self):
    return DialogState(Conversation(self.employee1, self.department), self.employee2)

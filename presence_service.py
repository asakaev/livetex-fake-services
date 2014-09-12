import sys, glob, time
sys.path.append('gen-py')

from livetex.presence.ttypes import *
from livetex.operator.ttypes import *
from livetex.department.ttypes import *

class PresenceHandler:
  operator1 = Operator()
  operator2 = Operator()

  department1 = Department()
  department2 = Department()

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

    self.department1.id = '554'
    self.department1.name = 'Some Department'
    self.department1.options = { 'opt1': 'val1' }

    self.department2.id = '555'
    self.department2.name = 'Another Department'
    self.department2.options = { 'opt1': 'val1' }

  def getOperators(self, status):
    return [self.operator1, self.operator2]

  def getDepartments(self, status):
    return [self.department1, self.department2]

  def getDepartmentOperators(self, status): 
    return [self.operator1, self. operator2]


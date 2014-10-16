import sys, glob, time
sys.path.append('gen-py')

from livetex.presence.ttypes import *
from livetex.employee.ttypes import *
from livetex.department.ttypes import *

class PresenceHandler:
  employee1 = Employee()
  employee2 = Employee()

  department1 = Department()
  department2 = Department()

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

    self.department1.id = '554'
    self.department1.name = 'Some Department'
    self.department1.options = { 'opt1': 'val1' }

    self.department2.id = '555'
    self.department2.name = 'Another Department'
    self.department2.options = { 'opt1': 'val1' }

  def getEmployees(self, status):
    return [self.employee1, self.employee2]

  def getDepartments(self, status):
    return [self.department1, self.department2]

  def getDepartmentEmployees(self, status): 
    return [self.employee1, self. employee2]

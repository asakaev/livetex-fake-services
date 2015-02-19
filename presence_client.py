import sys, glob
sys.path.append('gen-py')

from pprint import pprint

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

from livetex.presence import Presence

try:

  transport = THttpClient.THttpClient('http://sdk-prerelease.livetex.ru:10060/account:126927:site:91605:visitor:0n9gsn0guzugnwmi')
  # transport = THttpClient.THttpClient('http://sdk.livetex.ru:10060/account:123445:site:89200:visitor:ggrh5reh2cutmx6r')
  # transport = THttpClient.THttpClient('http://192.168.78.14:10060/account:5832:site:10005638:visitor:edww0pjo8pno2yb9')
  # transport = THttpClient.THttpClient('http://localhost:10050/account:5832:site:10005638:visitor:psuq6erx8brwl8fr')
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  client = Presence.Client(protocol)
  
  transport.open()

  department = Department('56', 'some_name', { 'opt1': 'val1' })
  status = 'online'

  operators = client.getEmployees(status)
  print 'operators are'
  pprint(operators)

  print '---'

  departments = client.getDepartments(status)
  print 'departments are '
  pprint(departments)

  print '---'

  employee = client.getEmployee('5833')
  print 'eployee is'
  print pprint(employee)

  print '---'

  departmentOperators = client.getDepartmentEmployees('7115')
  print 'departments employees are'
  pprint(departmentOperators)


except Thrift.TException, tx:
  
  print '%s' % (tx.message)